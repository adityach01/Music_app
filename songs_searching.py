# SC_Q3.py

def load_database():
    """
    Load songs from songs_database.txt into a nested dictionary.
    Key: artist (string)
    Value: list of song dicts with keys: title, album, genre, duration
    """
    songs_database = {}
    try:
        with open("songs_database.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = [p.strip().strip('"') for p in line.strip().split(",")]
                if len(parts) != 5:
                    continue
                title, artist, album, genre, duration = parts
                songs_database.setdefault(artist, []).append({
                    "title": title,
                    "album": album,
                    "genre": genre,
                    "duration": duration
                })
    except FileNotFoundError:
        print("Error: songs_database.txt file not found.")
    return songs_database

def search_by_title(songs_database):
    title_input = input("Enter the song title to search: ").strip()
    print(f"\nSearching for songs with title: '{title_input}'")
    title_lower = title_input.lower()
    for artist, songs in songs_database.items():
        for song in songs:
            if song["title"].lower() == title_lower:
                print(f"Found: '{song['title']}' by {artist} (Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']})")
                return
    print(f"Song title '{title_input}' does not exist in the database.")

def search_by_artist(songs_database):
    artist_input = input("Enter the artist's name to search: ").strip()
    print(f"\nSearching for songs by artist: '{artist_input}'")
    artist_lower = artist_input.lower()
    found = False
    for artist, songs in songs_database.items():
        if artist.lower() == artist_lower:
            for song in songs:
                print(f"Found: '{song['title']}' (Album: {song['album']}, Genre: {song['genre']}, Duration: {song['duration']})")
            found = True
            break
    if not found:
        print(f"No songs found for artist '{artist_input}'.")

def main():
    songs_database = load_database()
    while True:
        print("\n--- User Menu ---\n")
        print("1. Search for a Song by Title")
        print("2. Search for All Songs by an Artist")
        print("3. Exit\n")
        try:
            choice = input("Select an option: ").strip()
        except EOFError:
            # Graceful exit if no more input
            break

        if choice == "1":
            search_by_title(songs_database)
        elif choice == "2":
            search_by_artist(songs_database)
        elif choice == "3":
            print("\nExiting the Songs Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
