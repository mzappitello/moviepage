from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Iterable

import pydantic
import requests
from bs4 import BeautifulSoup


class Screening(pydantic.BaseModel):
    movie_title: str
    theater: str
    showtime: datetime


class Theater(ABC):
    def get_screenings(self) -> List[Screening]:
        """
        A list of movies playing in the theater.
        """
        all_screenings: List[Screening] = []
        for url in self.get_urls():
            response = requests.get(url)
            theater_soup = BeautifulSoup(response.content, "html.parser")
            all_screenings += self.scrape_for_screenings(theater_soup)

        return all_screenings

    @abstractmethod
    def get_urls(self) -> Iterable[str]:
        """
        yields urls for the next two weeks of movies
        """
        pass

    @abstractmethod
    def scrape_for_screenings(
        self, theater_soup: BeautifulSoup
    ) -> List[Screening]:
        pass
