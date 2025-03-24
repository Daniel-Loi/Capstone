import { useEffect,useState } from "react";
import { Upload } from "lucide-react";

const Mix = () => {
  const [song1, setSong1] = useState(null);
  const [song2, setSong2] = useState(null);
  const [data, setData] = useState(null);
  const [data1, setData1] = useState(null);
  const [mix_songs_out, setMix_songs] = useState(null);

  const handleFileChange = (e, setSong) => {
    setSong(e.target.files[0]);
  };


  const uploadFiles = () => {
    const formData = new FormData();
    formData.append("file1", song1);
    formData.append("file2", song2);

    fetch("http://127.0.0.1:5000/api/upload", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        setData(data.message);
        mix_songs();
      })
      .catch((error) => console.error("Upload error:", error));
  };

  const mix_songs = () => {
    fetch("http://127.0.0.1:5000/api/mix_songs")
    .then((response) => response.blob()) // Convert response to a blob
    .then((blob) => {
      const url = URL.createObjectURL(blob);
      setMix_songs(url);
    })
    .catch((error) => console.error("Received file error:", error));
  };

  const upload_to_db = () => {
    const formData = new FormData();
    formData.append("file1", song1);
    formData.append("file2", song2);
    fetch("http://127.0.0.1:5000/api/save_to_db", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => setData1(data.message))
      .catch((error) => console.error("Upload error:", error));
  };



  return (
    <div className="h-screen flex flex-col items-center justify-center bg-gradient-to-b from-black to-gray-900 text-white px-4">
      <h1 className="text-4xl font-bold mb-6 text-purple-400">Mix Your Songs</h1>

      <div>
            <p>{data}</p>
        </div>


      <div className="flex flex-col md:flex-row gap-8 mb-6">
        <div className="flex flex-col items-center gap-4">
          <span className="text-lg font-bold">Song 1</span>
          <label className="w-32 h-32 bg-gray-800 rounded-2xl flex flex-col items-center justify-center cursor-pointer hover:bg-gray-700">
            <Upload className="w-8 h-8 text-purple-400" />
            <span className="mt-2 text-sm">Upload</span>
            <input type="file" accept=".mp3" className="hidden" onChange={(e) => handleFileChange(e, setSong1)} />
          </label>
          {song1 && <p className="text-xs mt-2 text-gray-400">{song1.name}</p>}
        </div>

        <div className="flex flex-col items-center gap-4">
          <span className="text-lg font-bold">Song 2</span>
          <label className="w-32 h-32 bg-gray-800 rounded-2xl flex flex-col items-center justify-center cursor-pointer hover:bg-gray-700">
            <Upload className="w-8 h-8 text-purple-400" />
            <span className="mt-2 text-sm">Upload</span>
            <input type="file" accept=".mp3" className="hidden" onChange={(e) => handleFileChange(e, setSong2)} />
          </label>
          {song2 && <p className="text-xs mt-2 text-gray-400">{song2.name}</p>}
        </div>
      </div>

      {/* Mix Songs Button */}
      <button
        className={`bg-purple-500 text-white px-6 py-2 rounded-2xl text-lg ${
          !song1 || !song2 ? "opacity-50 cursor-not-allowed" : "hover:bg-purple-600"
        }`}
        disabled={!song1 || !song2}
        onClick={uploadFiles}
      >
        Mix Songs
      </button>

      {mix_songs_out && (
        <div className="text-4xl font-bold text-purple-400">
          <h1 className="text-lg font-bold">Received MP3 File</h1>
          <audio controls>
            <source src={mix_songs_out} type="audio/mpeg" />
            Your browser does not support the audio element.
          </audio>
          <a href={mix_songs_out} download="mixed_song.mp3" className="text-lg font-bold text-blue-400">
            Download MP3
          </a>
        </div>
      ) && (
      <button className="bg-purple-500 text-white px-6 py-2 rounded-2xl text-lg"
        onClick={upload_to_db}>
        Save song
      </button>
      )}
      
      {data1 && (
        <div className="text-4xl font-bold text-purple-400"> {data1} </div>
      )}


    </div>
  );
};

export default Mix;