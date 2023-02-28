import FormLogIn from './components/FormLogIn';
import FormSignUp from './components/FormSignUp';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import Home from './components/landingpage/Home.js';

function App() {
  return (
    <BrowserRouter>
      <div className='login-container'>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/login' element={<FormLogIn />} />
          <Route path='/signup' element={<FormSignUp />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
