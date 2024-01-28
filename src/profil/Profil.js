import React from 'react'
import Logo from '../comp/Logo';
import img from '../images/pexels-ekaterina-bolovtsova-6077089 1.png'
import imgProfil from '../images/user.jpeg'
import './profil.css'

const Profil = () => {
  return (
    <div>
       <div className='top'>
      <img src={img} alt='background' className='image'/>
      <h3 className='welcome'>Welcome to DZ Mouhami,<br></br> your trusted guide to legal expertise in Algeria.<br></br> Connect with the finest legal minds nationwide, ensuring you find the right<br></br> advocate for your unique needs</h3>
      <Logo/>
      </div>
      
      <div className='profil-info'>
        <div className='profil-img'>
            <img src={imgProfil} className='profil-imgg' />

        </div>
        <div className='profil-text'>
        <h3>Full Name :</h3>
        <h2>Bafdel moufdi</h2>
          <h3>Email :</h3>
          <h2>moufdibaf@gmail.com</h2>
        </div>
      </div>
    </div>
  )
}

export default Profil;