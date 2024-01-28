import React from 'react';
import logo from '../images/logoo.png';
import './logo.css';

const Logo = () => {
  return (
    <div className='logo'>
        <img src={logo} alt='logo'/>
    </div>
  )
}

export default Logo;