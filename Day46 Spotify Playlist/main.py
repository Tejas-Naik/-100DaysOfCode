from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from bs4 import BeautifulSoup
import requests

SPOTIPY_CLIENT_ID = '41e55bfb05fc40a9993e47948de4f720'
SPOTIPY_CLIENT_SECRET = '750ccf714aa247a6820fc3e9405f2954'

user_year = input("what year you would like to travel to? Type your anser in YYYY-MM-DD format:  ")

link_to_search = f'https://www.billboard.com/charts/hot-100/{user_year}'
response = requests.get(link_to_search)
print(response.status_code)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
