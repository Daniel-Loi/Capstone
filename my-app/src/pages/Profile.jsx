import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Profile = () => {
  const navigate = useNavigate();

  const [editMode, setEditMode] = useState(false);
  const [profile, setProfile] = useState({
    username: "GroovyUser",
    email: "user@groovyapp.com",
    password: "••••••••",
    accountCreated: "January 1, 2023", // New field
    favoritePlaylist: "Chill Vibes", // New field
    totalRemixes: 15, // New field
  });

  const handleChange = (e) => {
    setProfile({ ...profile, [e.target.name]: e.target.value });
  };

  const handleSave = () => {
    setEditMode(false);
    // Saving logic placeholder
  };

  const handleLogout = () => {
    navigate("/"); // Redirect to login page
  };

  return (
    <div className="flex flex-col items-center p-8 pb-24 w-full">
      <h1 className="text-4xl font-bold mb-10 text-purple-400">Your Profile</h1>

      <div className="relative bg-gray-800 p-8 rounded-2xl shadow-lg w-full max-w-4xl flex flex-col lg:flex-row items-center gap-8">
        {/* Profile Picture */}
        <div className="w-40 h-40 rounded-full bg-purple-500 flex items-center justify-center text-white text-3xl font-semibold">
          GU
        </div>

        {/* User Info Section */}
        <div className="flex flex-col w-full gap-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Username */}
            <div>
              <label className="block text-sm font-bold text-purple-500 mb-2">Username</label>
              {editMode ? (
                <input
                  type="text"
                  name="username"
                  value={profile.username}
                  onChange={handleChange}
                  className="w-full p-2 rounded bg-gray-700 text-white"
                />
              ) : (
                <p className="text-lg">{profile.username}</p>
              )}
            </div>

            {/* Email */}
            <div>
              <label className="block text-sm font-bold text-purple-500 mb-2">Email</label>
              {editMode ? (
                <input
                  type="email"
                  name="email"
                  value={profile.email}
                  onChange={handleChange}
                  className="w-full p-2 rounded bg-gray-700 text-white"
                />
              ) : (
                <p className="text-lg">{profile.email}</p>
              )}
            </div>

            {/* Password */}
            <div>
              <label className="block text-sm font-bold text-purple-500 mb-2">Password</label>
              {editMode ? (
                <input
                  type="password"
                  name="password"
                  value={profile.password}
                  onChange={handleChange}
                  className="w-full p-2 rounded bg-gray-700 text-white"
                />
              ) : (
                <p className="text-lg">{profile.password}</p>
              )}
            </div>

            {/* Account Created On */}
            <div>
              <label className="block text-sm font-bold text-purple-500 mb-2">Account Created On</label>
              <p className="text-lg">{profile.accountCreated}</p>
            </div>

            {/* Favorite Playlist */}
            <div>
              <label className="block text-sm font-bold text-purple-500 mb-2">Favorite Playlist</label>
              <p className="text-lg">{profile.favoritePlaylist}</p>
            </div>

            {/* Total Remixes Created */}
            <div>
              <label className="block text-sm font-bold text-purple-500 mb-2">Total Remixes Created</label>
              <p className="text-lg">{profile.totalRemixes}</p>
            </div>
          </div>

          {/* Edit / Save / Cancel Buttons */}
          <div className="flex justify-end gap-4 mt-4">
            {editMode ? (
              <>
                <button
                  onClick={handleSave}
                  className="bg-green-500 text-white p-2 px-4 rounded-lg hover:bg-green-600"
                >
                  Save
                </button>
                <button
                  onClick={() => setEditMode(false)}
                  className="bg-gray-600 text-white p-2 px-4 rounded-lg hover:bg-gray-500"
                >
                  Cancel
                </button>
              </>
            ) : (
              <button
                onClick={() => setEditMode(true)}
                className="bg-purple-500 text-white p-2 px-4 rounded-lg hover:bg-purple-600"
              >
                Edit Profile
              </button>
            )}
          </div>

          {/* Logout Button */}
          <div className="flex justify-end mt-6">
            <button
              onClick={handleLogout}
              className="bg-red-500 text-white p-2 px-4 rounded-lg hover:bg-red-600 transition"
            >
              Logout
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;