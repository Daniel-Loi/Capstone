from Ai_DJ_DB import save_audio_to_mongodb, retrieve_audio_from_mongodb, list_stored_files
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Atlas Connection
MONGO_USER = os.getenv('MONGO_USER', 'your_username')
MONGO_PASS = os.getenv('MONGO_PASS', 'your_password')
MONGO_CLUSTER = os.getenv('MONGO_CLUSTER', 'your_cluster_url')
MONGO_URI = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_CLUSTER}/?retryWrites=true&w=majority"
DB_NAME = "AI_DJ_Database"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
songs_collection = db["Songs"]

def delete_song(filename):
    """Delete a song from the database"""
    try:
        # Delete from Songs collection
        result = songs_collection.delete_one({"filename": filename})
        if result.deleted_count > 0:
            print(f"Successfully deleted {filename} from database")
            return True
        else:
            print(f"Song {filename} not found in database")
            return False
    except Exception as e:
        print(f"Error deleting song: {str(e)}")
        return False

def upload_song(file_path):
    """Upload a song to the database"""
    try:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return False
        
        filename = os.path.basename(file_path)
        # Basic metadata for manually uploaded songs
        song_metadata = {
            "original_songs": [filename],
            "upload_type": "manual",
            "description": "Manually uploaded song"
        }
        
        save_audio_to_mongodb(file_path, filename, song_metadata)
        return True
    except Exception as e:
        print(f"Error uploading song: {str(e)}")
        return False

def print_menu():
    print("\nDatabase Manager")
    print("1. List all songs")
    print("2. Delete a song")
    print("3. Download a song")
    print("4. Upload a song")
    print("5. Exit")

def main():
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            # List all songs
            songs = list_stored_files()
            if songs:
                print("\nAll Songs in Database:")
                for i, song in enumerate(songs, 1):
                    print(f"{i}. {song['filename']}")
                    print(f"   Stored on: {song['stored_date']}")
            else:
                print("No songs found in database.")

        elif choice == "2":
            # Delete a song
            songs = list_stored_files()
            if not songs:
                print("No songs found in database.")
                continue

            print("\nAvailable songs:")
            for i, song in enumerate(songs, 1):
                print(f"{i}. {song['filename']}")
            
            filename = input("\nEnter the filename to delete: ")
            confirm = input(f"Are you sure you want to delete {filename}? (yes/no): ")
            if confirm.lower() == 'yes':
                delete_song(filename)

        elif choice == "3":
            # Download a song
            songs = list_stored_files()
            if not songs:
                print("No songs found in database.")
                continue

            print("\nAvailable songs:")
            for i, song in enumerate(songs, 1):
                print(f"{i}. {song['filename']}")
            
            filename = input("\nEnter the filename to download: ")
            output_path = input("Enter the output path (e.g., downloaded_song.mp3): ")
            retrieve_audio_from_mongodb(filename, output_path)

        elif choice == "4":
            # Upload a song
            file_path = input("\nEnter the path to the song file (e.g., C:/Music/song.mp3): ")
            if upload_song(file_path):
                print("Song uploaded successfully!")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 