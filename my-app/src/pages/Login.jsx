import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    if (email.trim() && password.trim()) {
      navigate("/home");
    } else {
      alert("Please enter valid credentials.");
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen w-screen bg-gradient-to-b from-black to-gray-900 text-white">
      <div className="w-full max-w-lg bg-gray-800 p-8 rounded-lg shadow-lg mx-4">
        <h1 className="text-4xl font-extrabold text-purple-400 text-center mb-6">
          Login to Groovy
        </h1>
        <form onSubmit={handleLogin} className="flex flex-col gap-4">
          <input
            type="email"
            placeholder="Email"
            className="w-full p-3 border border-gray-600 rounded-lg bg-gray-900 text-white placeholder-gray-400 focus:ring-2 focus:ring-purple-500"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            className="w-full p-3 border border-gray-600 rounded-lg bg-gray-900 text-white placeholder-gray-400 focus:ring-2 focus:ring-purple-500"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button
            type="submit"
            className="w-full bg-purple-500 text-white p-3 rounded-lg font-semibold hover:bg-purple-700 transition shadow-lg"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
