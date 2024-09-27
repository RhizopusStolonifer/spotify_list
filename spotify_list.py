import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# Replace these with your credentials
SPOTIPY_CLIENT_ID = '7ad3d4ecef4c4339955acd74f356f3e8'
SPOTIPY_CLIENT_SECRET = 'dfcaf9b8dedb498b94284fd3a3c494c5'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

# Set up authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-read-private"))

# Playlist ID (you can get this from Spotify's share link)
playlist_id = 'https://open.spotify.com/playlist/4zWZvBihm6BjSHwqc9rloG?si=1f6c75d1bfb64e28'

# Fetch playlist tracks
results = sp.playlist_tracks(playlist_id)

# Extract data (song name, artist, album)
tracks = []
for item in results['items']:
    track = item['track']
    song_name = track['name']
    artist_name = ', '.join([artist['name'] for artist in track['artists']])
    album_name = track['album']['name']
    tracks.append([song_name, artist_name, album_name])

# Convert to a DataFrame
df = pd.DataFrame(tracks, columns=['Song Name', 'Artist', 'Album'])

# Save to CSV
df.to_csv('playlist.csv', index=False)

print("Playlist exported to playlist.csv")
