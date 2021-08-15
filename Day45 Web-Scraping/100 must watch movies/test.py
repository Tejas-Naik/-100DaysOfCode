from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")


def strip_enum(title):
    # If it doesn't start with a digit, just leave it as it is
    if not title[0].isdigit():
        return title
    # Otherwise, remove the enumeration
    return " ".join(title.split()[1:])


movies = [strip_enum(movie.getText())
          for movie in soup.select("h3.title")[::-1]]
with open("movies.txt", "w", encoding="ISO-8859-1") as file:
    for index, movie in enumerate(movies):
        file.write(f"{index + 1}) {movie}\n")
