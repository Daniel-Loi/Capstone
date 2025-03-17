import { Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Playlists from "./pages/Playlists";
import Mix from "./pages/Mix";
import Profile from "./pages/Profile";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Login />} />
        <Route path="home" element={<Home />} />
        <Route path="login" element={<Login />} />
        <Route path="playlists" element={<Playlists />} />
        <Route path="mix" element={<Mix />} />
        <Route path="profile" element={<Profile />} />
      </Route>
    </Routes>
  );
};

export default App;
