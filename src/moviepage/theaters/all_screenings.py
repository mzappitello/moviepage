from typing import List
import json
import argparse

from .theater import Screening, Theater
from .nitehawk import Nighthawk


def get_all_screenings() -> List[Screening]:
    all_theaters: List[Theater] = [Nighthawk()]

    all_screenings: List[Screening] = []

    for theater in all_theaters:
        all_screenings += theater.get_screenings()

    return all_screenings



def write_screenings() -> None:
    parser = argparse.ArgumentParser(
        description="Write Screenings to Disc"
    )
    parser.add_argument(
        "--output-file",
        default="screenings.json",
        type=str,
        required=True,
        help="File to write screenings json string to"
    )
    
    args = parser.parse_args()
    screenings = get_all_screenings()

    # Convert each Screening object to a dict
    screenings_dicts = [screening.dict() for screening in screenings]
    screenings_json = json.dumps(screenings_dicts, default=str)

    with open(args.output_file, 'w') as file:
        file.write(screenings_json)
