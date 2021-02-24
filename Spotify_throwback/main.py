import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "9a36a06c65214f69ac7c3a909c41fecc"
CLIENT_SECRET = "0d4223d337bc478cbe4f7b60e0c6bf2d"

date = input("What year would you like to travel to (YYYY-MM-DD)? ")

URl = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URl)

html_format = response.text

# print(html_format)

soup = BeautifulSoup(html_format, "html.parser")
titles = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_names = []
# print(titles)

for elem in titles:
    text = elem.getText()
    song_names.append(text)

print(song_names)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
