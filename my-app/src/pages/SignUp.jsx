import { useState } from "react";
import { useNavigate } from "react-router-dom";

const SignUp = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const navigate = useNavigate();

  const handleSignUp = (e) => {
    e.preventDefault();

    if (!username.trim() || !email.trim() || !password.trim() || !confirmPassword.trim()) {
      alert("Please fill out all fields.");
      return;
    }

    if (password !== confirmPassword) {
      alert("Passwords do not match.");
      return;
    }

    alert("Account created successfully!");
    navigate("/");
  };

  return (
    <div className="flex items-center justify-center min-h-screen w-screen bg-gradient-to-b from-black to-gray-900 text-white p-4">
      <div className="w-full max-w-lg bg-gray-800 p-10 rounded-2xl shadow-xl flex flex-col items-center gap-6">
        {/* Logo Placeholder */}
        <div className="w-20 h-20 bg-purple-500 rounded-full flex items-center justify-center shadow-md hover:shadow-lg transition">
          <span className="text-white text-2xl font-bold">Logo</span>
        </div>

        <h1 className="text-3xl font-extrabold text-purple-400 text-center">Create Your Account</h1>

        <form onSubmit={handleSignUp} className="flex flex-col gap-4 w-full">
          <input
            type="text"
            placeholder="Username"
            className="w-full p-3 border border-gray-600 rounded-lg bg-gray-900 text-white placeholder-gray-400 focus:ring-2 focus:ring-purple-500 focus:outline-none transition"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <input
            type="email"
            placeholder="Email"
            className="w-full p-3 border border-gray-600 rounded-lg bg-gray-900 text-white placeholder-gray-400 focus:ring-2 focus:ring-purple-500 focus:outline-none transition"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <input
            type="password"
            placeholder="Password"
            className="w-full p-3 border border-gray-600 rounded-lg bg-gray-900 text-white placeholder-gray-400 focus:ring-2 focus:ring-purple-500 focus:outline-none transition"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          {/* Confirm Password Field */}
          <input
            type="password"
            placeholder="Confirm Password"
            className="w-full p-3 border border-gray-600 rounded-lg bg-gray-900 text-white placeholder-gray-400 focus:ring-2 focus:ring-purple-500 focus:outline-none transition"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
          />

          <button
            type="submit"
            className="w-full bg-purple-500 text-white p-3 rounded-lg font-semibold hover:bg-purple-700 transition shadow-md"
          >
            Sign Up
          </button>
        </form>

        <div className="text-center mt-4">
          <p className="text-gray-400">Already have an account?</p>
          <button
            onClick={() => navigate("/")}
            className="mt-2 text-purple-400 hover:underline font-semibold"
          >
            Login
          </button>
        </div>
      </div>
    </div>
  );
};

export default SignUp;
