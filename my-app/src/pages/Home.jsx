const Home = () => {
  return (
    <div className="flex flex-col items-center justify-center text-center p-8 pb-24">
      <h1 className="text-5xl font-bold text-purple-400 mb-8">Welcome to Groovy</h1>
      
      {/* Logo Placeholder */}
      <div className="w-40 h-40 bg-purple-600 rounded-full flex items-center justify-center mb-6 transition duration-300 hover:shadow-[0_0_25px_5px_rgba(255,255,255,0.7)]">
        <span className="text-white text-2xl">Logo</span>
      </div>

      {/* Description Placeholder */}
      <p className="max-w-xl font-bold mb-20 text-lg text-gray-300">
        Your personal AI powered DJ ready to remix your favorite songs with the click of a button!
      </p>

      <p className="text-lg font-bold text-white mb-2">To get started, press one of the buttons below ⬇️ </p>
    </div>
  );
};

export default Home;
