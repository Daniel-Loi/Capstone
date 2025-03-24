import React from 'react'
import { useParams, useLocation  } from 'react-router-dom'
import { useState, useEffect } from "react";

const Playlist_page = () => {
	const { id } = useParams();
	const [data, setData] = useState([]);
	const [del, setDelete] = useState(null);
	const [song, setSong] = useState(null);
	const [key, setKey] = useState(0); // Used to force reloading the audio player
	const location = useLocation();
	const playlistName = location.state?.name || "Unknown Playlist";


	const list_songs = () => {
		fetch("http://127.0.0.1:5000/api/list_songs")
		.then((response) => response.json())
		.then((data) => setData(data))
		.catch((error) => console.error("Upload error:", error));
	};

	const get_song_db = (filename) => {
		const audioUrl = `http://127.0.0.1:5000/api/get_song_db/${filename}`;
		setSong(audioUrl);
		setKey((prevKey) => prevKey + 1);
	};

	const delete_song_db = (filename) => {
		fetch(`http://127.0.0.1:5000/api/delete_song_db/${filename}`)
		.then((response) => response.json())
		.then((data) => {
			setDelete(data.message);
			list_songs();
		})
		.catch((error) => console.error("Upload error:", error));
	};

	useEffect(() => {
    list_songs(); // Fetch data when the component mounts
  }, []);


	return(
		<div>
    	<h1 className="text-1xl font-bold text-purple-400">Playlist {playlistName}</h1> {/* Fixed closing tag */}
    	<p className="text-purple-400">Playlist ID: {id}</p>

    	{data.length > 0 ? (
    	  <ul className="mt-4 p-4 rounded-lg">
    	    {data.map((item, index) => (
    	      <li key={index} className="text-md">
    	        <h1 className="text-1xl font-bold text-blue-400 display: inline" onClick={() => get_song_db(item.filename)}>{item.filename} </h1> 
							<h1 className="text-1xl font-bold text-purple-400 display: inline" > Stored Date: {item.stored_date} </h1>
							<h1 className="text-1xl font-bold text-blue-400 display: inline" onClick={() => delete_song_db(item.filename)}> Remove from playlist </h1>
    	      </li>
    	    ))}
    	  </ul>
    	) : (
    	  <p>Loading...</p>
    	)}
		{song && (
		<div className="text-4xl font-bold text-purple-400">
  		<h1 className="text-lg font-bold">Received MP3 File</h1>
			<audio key={key} controls>
			  <source src={song} type="audio/mpeg" />
			  Your browser does not support the audio element.
			</audio>
		</div>
		)}
  </div>
	)
}

export default Playlist_page