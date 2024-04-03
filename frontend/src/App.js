import React from 'react';
import WebcamCapture from './WebcamCapture';
import Navbar from './components/Navbar'


function App() {
  return (
    <div className="App">
      <Navbar />
      <main>
        <WebcamCapture />
      </main>
    </div>
  );
}

export default App;
