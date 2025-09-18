# Playlist-Platform-Transfer-Project

### Goal
 - transfer playlists accurately from multiple platfroms to Spotify

## Dependencies
 - node.js
 - python
     - packages: "ytmusicapi", "spotipy", "flask", and "flask-cors"

## How to Run
 - Setup:
    - Put the client secret in backend/Creds.py
      - example format specified in CredsExample.py
    - "npm install" in folder: frontend
    - Ensure you have the python packages: "ytmusicapi", "spotipy", "flask", and "flask-cors"
 - to Run:
    - run "backend/TransferPlaylistMain.py"
    - change directory to "frontend"
    - If first time running: 
      - ```Bash 
        npm i
        ```
    - Every time:
      ```bash
      npm run dev
      ```

## Contributors:
 - Alex Young (front-end)
 - Kevin Dillenburg 
 - Lucas Horn