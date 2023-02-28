import React from 'react';
import './home.css';
import cons from '../asset/Group1.png';
import { useNavigate } from 'react-router-dom';
import tol from '../asset/tol.png'

const Home = () => {
  const navigasi = useNavigate();
  return (
    
    <div>
      {/* <nav>
        <div className='gede'>
          <img src={tol} width='50px' height='auto'/>
        </div>
        <div>
          <a href='/login'>Login</a>
          <a href='/singup'>Register</a>
        </div>
      </nav> */}
      <div className='tytyd' >
        <img src={cons} />
      
      <div className ="tyts">
        <h1>Selamat Datang</h1>
        
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ut nisl
          sed dolor dapibus aliquet. Donec vestibulum fringilla nibh, vel
          malesuada urna tristique vel.
        </p>
        <div className='butt'>
          <button onClick={()=> navigasi ('/login')}>Login</button>
          <button onClick={()=> navigasi('/singup')}>Register</button>
      
        </div>
      </div>
    </div>
    </div>
  )
}

export default Home