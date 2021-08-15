import requests
from bs4 import BeautifulSoup

URL = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="a", class_="xs-text-charcoal decoration-none")
with open('movies.txt', 'w') as file:
    for movie in all_movies:
        movie_name = movie.getText()
        file.write(movie_name)

