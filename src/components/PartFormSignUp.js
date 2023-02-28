import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

function PartFormSignUp() {
  // deklarasi hooks
  const [inputData, setInputData] = useState({
    name: '',
    username: '',
    email: '',
    gender: '',
    password: '',
  });
  // pasang useNavigate from react-router-dom
  const navigate = useNavigate();
  // function untuk form submit
  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post(`http://localhost:3001/users`, inputData)
      .then((res) => {
        alert('Register Berhasil!');
        navigate('/');
      })
      .catch((err) => {
        console.log(err);
      });
  };
  // function untuk radio button
  const handleRadioChange = (e) => {
    setInputData({ ...inputData, gender: e.target.value });
  };
  return (
    // panggil semua function dengan onSubmit & onChange
    <form onSubmit={handleSubmit}>
      <label htmlFor='username'>Username:</label>
      <input
        type='text'
        onChange={(e) =>
          setInputData({ ...inputData, username: e.target.value })
        }
        placeholder='Username'
        id='username'
        required
      />
      <label htmlFor='password'>Password:</label>
      <input
        type='password'
        onChange={(e) =>
          setInputData({ ...inputData, password: e.target.value })
        }
        placeholder='Password'
        id='password'
        required
      />
      <label htmlFor='email'>Email:</label>
      <input
        type='text'
        onChange={(e) => setInputData({ ...inputData, email: e.target.value })}
        placeholder='Email'
        id='email'
        required
      />
      <label htmlFor='name'>Name:</label>

      <input
        type='text'
        onChange={(e) => setInputData({ ...inputData, name: e.target.value })}
        placeholder='Name'
        id='name'
        required
      />
      <label htmlFor='gender'>Gender:</label>
      <br />
      <br />
      <input
        type='radio'
        name='gender'
        id='male'
        onChange={handleRadioChange}
        value='male'
      />
      <label htmlFor='male'>Male</label>
      <br />
      <input
        type='radio'
        name='gender'
        id='female'
        onChange={handleRadioChange}
        value='female'
      />
      <label htmlFor='female'>Female</label>
      <br />
      <input type='submit' value='Sign Up' className='sign-up-btn' />
      <div className='center'>
        Already a user?{' '}
        <Link to='/' className='link'>
          Log in
        </Link>
      </div>
    </form>
  );
}

export default PartFormSignUp;
