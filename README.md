This project is mostly meant for screwing around with web architecture, but also something that i hope can serve a purpose.

# Goals

I'd like to be able to see all the movie times at theaters around me for the next two weeks to help me plan out what I'm going to see. Currently, that means having a folder of bookmarks in a browser that I check all the time. While fun, it can be quite time consuming. Automating the scanning of these pages and collecting the results in one spot should help me out quite a bit.

Further, I'd like to connect this to my LetterBoxd account so that I can add a sort feature to show movies that are on my Watch List.

Eventually, I'd like a section that collects various reviews and podcasts from movies that I've seen in the last week so that I can explore them.

# Architecture

I want to keep this fairly simple while also exploring the latest tooling. The site is to be a single page with external links.

The application will be generated using Flask in a poetry managed python package. The code for that can be found in `src/moviepate/` with they pyproject and poetry files found at the root directory.

The frontend of the application will be driven by react. It will live in `frontend/`. When built, the build files will be moved to `src/moviepage/static/` where it will be served by flask.