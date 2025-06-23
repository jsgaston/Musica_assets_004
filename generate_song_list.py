import os
import json

VALID_EXTENSIONS = [".m4a", ".mp3", ".wav", ".flac", ".ogg", ".aac"]

# Reemplaza con tu propio usuario y repo si es necesario:
GITHUB_USER = "jsgaston"
GITHUB_REPO = "Musica_assets_004"
GITHUB_BRANCH = "main"

RAW_BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/"

def is_audio_file(filename):
    return any(filename.lower().endswith(ext) for ext in VALID_EXTENSIONS)

def get_audio_files_in_root():
    songs = []
    for file in os.listdir("."):
        if os.path.isfile(file) and is_audio_file(file):
            songs.append({
                "title": os.path.splitext(file)[0],
                "filename": file,
                "url": RAW_BASE_URL + file.replace(" ", "%20")
            })
    return songs

if __name__ == "__main__":
    songs = get_audio_files_in_root()
    with open("song_list004.json", "w", encoding="utf-8") as f:
        json.dump(songs, f, indent=2, ensure_ascii=False)
    print(f"Generated song_list004.json with {len(songs)} entries.")
