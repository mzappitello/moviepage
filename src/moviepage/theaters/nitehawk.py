from bs4 import BeautifulSoup
from datetime import datetime, timedelta

from typing import List, Dict, Iterable
from .theater import Theater, Screening
import re


class Nighthawk(Theater):
    def get_urls(self) -> Iterable[str]:
        current_date = datetime.today()
        end_date = current_date + timedelta(days=2)
        while current_date < end_date:
            date_str = current_date.strftime("%Y-%m-%d")
            yield f"https://nitehawkcinema.com/prospectpark/{date_str}"
            current_date += timedelta(days=1)

    def scrape_for_screenings(
        self, theater_soup: BeautifulSoup
    ) -> List[Screening]:
        def parse_raw_showtime(raw_showtime: str):
            """
            raw showtimes are formatted
            'Buy tickets for <Movie Title> - MM/DD/YY @ HH:MM <am/pm>'
            """
            # Using regex to extract movie name and datetime
            regex_string = r"Buy tickets for (.+) - (\d{1,2}/\d{1,2}/\d{2} @ \d{1,2}:\d{2} [ap]m)"
            match = re.search(regex_string, raw_showtime)

            if match:
                # parse out the movie name and convert the showtime
                movie_name = match.group(1).strip()
                datetime_str = match.group(2).strip()
                showtime = datetime.strptime(
                    datetime_str, "%m/%d/%y @ %I:%M %p"
                )

                return Screening(
                    movie_title=movie_name,
                    theater="Nighthawk Prospect Park",
                    showtime=showtime,
                )

            raise Exception(f"couldn't parse {raw_showtime}")

        raw_showtimes = [
            a.get("aria-label")
            for a in theater_soup.find_all("a")
            if a.get("class") and "showtime" in a.get("class")
        ]

        return [parse_raw_showtime(rst) for rst in raw_showtimes]
