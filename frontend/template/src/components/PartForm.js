import axios from 'axios';
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

function PartForm() {
  // deklarasi hooks
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  // pasang useNavigate from react-router-dom
  const navigate = useNavigate();
  // function untuk form submit
  const handleLogin = (e) => {
    e.preventDefault();
    if (!username || !password) {
      alert('Username dan Password harus di isi');
      return;
    }
    axios
      .post(`http://localhost:3001/users`, { username, password })
      .then((res) => {
        alert('Login Berhasil!');
        navigate('/');
      })
      .catch((err) => {
        alert('Login Gagal!');
        console.log(err);
      });
  };
  return (
    // panggil semua function dengan onSubmit & onChange
    <form onSubmit={handleLogin}>
      <label for='username'>Username:</label>
      <input
        type='text'
        value={username}
        placeholder='Enter username'
        onChange={(e) => setUsername(e.target.value)}
        id='username'
        required
      />
      <label for='password'>Password:</label>
      <input
        type='password'
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder='Enter password'
        id='password'
        required
      />
      <div className='right'>
        <Link to='/forgot-password' className='link'>
          Forgot Password?
        </Link>
      </div>
      <input type='submit' value='Log In' className='login-btn' />
      <div className='center'>
        Do not have an account?{' '}
        <Link to='/signup' className='link'>
          Create an account
        </Link>
      </div>
    </form>
  );
}

export default PartForm;
