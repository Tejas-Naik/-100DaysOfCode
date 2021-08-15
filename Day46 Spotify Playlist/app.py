from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotipy
import requests
from bs4 import BeautifulSoup

SPOTIPY_CLIENT_ID = '578b27b62009460eb7ab31926fbcfa06'
SPOTIPY_CLIENT_SECRET = 'edb1ac1af35543be8db7ea9cd1c096bc'

date = input("Please enter the date you want the top 100 songs! in YYYY-MM-DD format!! :")
response_songs = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')

songs_html = response_songs.content

soup = BeautifulSoup(songs_html, 'html.parser')

all_song_names = soup.find_all(name='span', class_="chart-element__information__song text--truncate color--primary")
song_names = [song.get_text() for song in all_song_names]
"""tHIS IS SPOTU=IPY OCDE"""

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

song_uris = []
year = date.split('-')[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(playlist)

