import os
import json

VALID_EXTENSIONS = [".m4a", ".mp3", ".wav", ".flac", ".ogg", ".aac"]

def is_audio_file(filename):
    return any(filename.lower().endswith(ext) for ext in VALID_EXTENSIONS)

def get_audio_files_in_root():
    songs = []
    for file in os.listdir("."):
        if os.path.isfile(file) and is_audio_file(file):
            songs.append({
                "title": os.path.splitext(file)[0],
                "filename": file
            })
    return songs

if __name__ == "__main__":
    songs = get_audio_files_in_root()
    with open("song_list.json", "w", encoding="utf-8") as f:
        json.dump(songs, f, indent=2, ensure_ascii=False)
    print(f"Generated song_list.json with {len(songs)} entries.")
