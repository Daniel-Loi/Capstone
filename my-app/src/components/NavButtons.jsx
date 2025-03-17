import { NavLink } from "react-router-dom";

const NavButtons = () => {
  return (
    <div className="fixed bottom-6 flex gap-4 justify-center w-full">
      <NavLink to="/home">
        <button className="bg-purple-500 text-white py-2 px-6 rounded-xl shadow-lg hover:shadow-purple-500/50 transition">
          Home
        </button>
      </NavLink>
      <NavLink to="/playlists">
        <button className="bg-purple-500 text-white py-2 px-6 rounded-xl shadow-lg hover:shadow-purple-500/50 transition">
          Playlists
        </button>
      </NavLink>
      <NavLink to="/mix">
        <button className="bg-purple-500 text-white py-2 px-6 rounded-xl shadow-lg hover:shadow-purple-500/50 transition">
          Mix
        </button>
      </NavLink>
      <NavLink to="/profile">
        <button className="bg-purple-500 text-white py-2 px-6 rounded-xl shadow-lg hover:shadow-purple-500/50 transition">
          Profile
        </button>
      </NavLink>
    </div>
  );
};

export default NavButtons;