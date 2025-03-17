import { useState } from "react";
import { Upload } from "lucide-react";

const Mix = () => {
  const [song1, setSong1] = useState(null);
  const [song2, setSong2] = useState(null);

  const handleFileChange = (e, setSong) => {
    setSong(e.target.files[0]);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-b from-black to-gray-900 text-white px-4 pb-24">
      <h1 className="text-4xl font-bold mb-10 text-purple-400">Mix Your Songs</h1>

      <div className="flex flex-col md:flex-row gap-12 mb-8">
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
        className={`bg-purple-500 text-white px-6 py-2 rounded-2xl text-lg mt-8 ${
          !song1 || !song2 ? "opacity-50 cursor-not-allowed" : "hover:bg-purple-600"
        }`}
        disabled={!song1 || !song2}
      >
        Mix Songs
      </button>

      {/* Removed duplicate nav buttons */}
    </div>
  );
};

export default Mix;
