import argparse
import os

from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


@app.route("/")
def home():
    return render_template("index.html")


def save_static_site(output_dir: str = "static_site") -> None:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with app.app_context():
        with open(os.path.join(output_dir, "index.html"), "w") as file:
            file.write(home())


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate static site from Flask app."
    )

    parser.add_argument(
        "--screenings-file",
        type=str,
        default="screenings.json",
        help=
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="static_site",
        help="Output directory for the static site",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    save_static_site(output_dir=args.output_dir)
