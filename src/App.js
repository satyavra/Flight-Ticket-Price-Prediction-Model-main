import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Flight Price Prediction</h1>
        <p>Use the form below to predict flight ticket prices</p>
      </header>
      <main>
        <iframe 
          src="/index.html" 
          style={{width: '100%', height: '100vh', border: 'none'}}
          title="Flight Price Prediction Form"
        />
      </main>
    </div>
  );
}

export default App;
