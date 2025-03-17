import os
from dotenv import load_dotenv
import gridfs
from pymongo import MongoClient
from datetime import datetime

# Load environment variables
load_dotenv()

# MongoDB Atlas Connection
MONGO_USER = os.getenv('MONGO_USER', 'your_username')  # Replace with your Atlas username
MONGO_PASS = os.getenv('MONGO_PASS', 'your_password')  # Replace with your Atlas password
MONGO_CLUSTER = os.getenv('MONGO_CLUSTER', 'your_cluster_url')  # Replace with your Atlas cluster URL

# Construct the connection string
MONGO_URI = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_CLUSTER}/?retryWrites=true&w=majority"
DB_NAME = "AI_DJ_Database"

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    fs = gridfs.GridFS(db)
    # Test the connection
    client.admin.command('ping')
    print("Successfully connected to MongoDB Atlas!")
except Exception as e:
    print(f"Error connecting to MongoDB Atlas: {str(e)}")

# Songs collection for metadata
songs_collection = db["Songs"]

def save_audio_to_mongodb(file_path, filename, song_metadata):
    """
    Save an audio file to MongoDB using GridFS and store metadata in the Songs collection.
    """
    try:
        with open(file_path, "rb") as f:
            file_id = fs.put(f, filename=filename)
        
        # Add metadata (including timestamp)
        song_metadata["filename"] = filename
        song_metadata["file_id"] = str(file_id)  # Convert ObjectId to string
        song_metadata["stored_date"] = datetime.utcnow().isoformat()

        # Save metadata to MongoDB
        song_entry_id = songs_collection.insert_one(song_metadata).inserted_id
        print(f"Saved {filename} to MongoDB with ID: {file_id}")

        return song_entry_id

    except Exception as e:
        print(f"Error saving {filename}: {str(e)}")
        return None

def retrieve_audio_from_mongodb(filename, output_path):
    """
    Retrieve an audio file from MongoDB and save it locally.
    """
    try:
        file_data = fs.find_one({"filename": filename})
        if file_data:
            with open(output_path, "wb") as f:
                f.write(file_data.read())
            print(f"Retrieved {filename} from MongoDB and saved to {output_path}")
        else:
            print(f"File {filename} not found in MongoDB.")

    except Exception as e:
        print(f"Error retrieving {filename}: {str(e)}")

def list_stored_files():
    """
    List all stored files in MongoDB.
    """
    files = songs_collection.find({}, {"filename": 1, "stored_date": 1})
    return [{"filename": file["filename"], "stored_date": file["stored_date"]} for file in files]

if __name__ == "__main__":
    # Example retrieval
    retrieve_audio_from_mongodb("mixed_output.mp3", "retrieved_mixed_output.mp3")
