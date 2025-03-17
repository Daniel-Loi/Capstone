import { Outlet, useLocation } from "react-router-dom";
import NavButtons from "./NavButtons";

const Layout = () => {
  const location = useLocation();
  const isLoginPage = location.pathname === "/";

  return (
    <div className="min-h-screen w-full flex flex-col justify-between bg-gradient-to-b from-black to-gray-900 text-white">
      {/* Main content area */}
      <div className="flex-grow flex items-center justify-center w-full">
        <Outlet />
      </div>

      {/* Show NavButtons only if NOT on the login page */}
      {!isLoginPage && <NavButtons />}
    </div>
  );
};

export default Layout;
