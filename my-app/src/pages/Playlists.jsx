import { useState } from "react";
import React, { Component } from 'react';
import Icon from '@mdi/react';
import { mdiPlaylistMusic } from '@mdi/js';
import { useNavigate } from "react-router-dom";

const Playlists = () => {
  const navigate = useNavigate();

  const [playlists, setPlaylists] = useState([
    { id: 1, name: "Chill" },
    { id: 2, name: "Workout" },
    { id: 3, name: "idk" },
    { id: 4, name: "idc" },
    { id: 5, name: "Top Hits 2025" },
    { id: 6, name: "something" },
    { id: 7, name: "something2" },
    { id: 8, name: "idk2" },
    { id: 9, name: "more" },
    { id: 10, name: "again" },
    { id: 11, name: "again2" },
    { id: 12, name: "last" },
    { id: 5, name: "Top Hits 2025" },
    { id: 6, name: "something" },
    { id: 7, name: "something2" },
    { id: 8, name: "idk2" },
    { id: 9, name: "more" },
    { id: 10, name: "again" },
    { id: 11, name: "again2" },
    { id: 12, name: "last" }
    //add more to test scrollbar functionality
  ]);

  return (
    <div className="flex flex-col items-center p-8 pb-20">
      <h1 className="text-4xl font-bold mb-8 text-purple-400">Your Playlists</h1>
      {/* Scrollable Grid Container */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 overflow-y-auto p-4 w-full max-h-[65vh]">
        {playlists.map((playlist) => (
          <div
            key={playlist.id}
            className="bg-gray-800 p-4 rounded-xl shadow-lg hover:shadow-purple-500/50 hover:scale-105 transition-all duration-300 flex flex-col items-center"
            onClick={() => navigate(`/playlists/${playlist.id}`, { state: { name: playlist.name } })}
          >
            <Icon
              path={mdiPlaylistMusic}
              title="Playlist Icon"
              size={3}
              color="#a855f7"
              horizontal
            />
            <h2 className="text-lg font-semibold">{playlist.name}</h2>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Playlists;
