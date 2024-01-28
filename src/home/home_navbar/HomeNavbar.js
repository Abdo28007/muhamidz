import { Link } from 'react-router-dom';
import { FaHome } from 'react-icons/fa';
import { FaGavel } from 'react-icons/fa';
import { FaUser } from 'react-icons/fa';
import { FaSignOutAlt } from 'react-icons/fa';
import './homenavbar.css'

const HomeNavbar = () => {
  return (
    <div className='home-navbar'>
        <ul>
          <li><Link to="/" className='nav-link'><FaHome/></Link></li>
          <li><Link to="/Lawyers" className='nav-link'><FaGavel /></Link></li>
          <li><Link to="/Profil" className='nav-link'><FaUser/></Link></li>
          <li><Link to="/" className='nav-link'><FaSignOutAlt/></Link></li>
 </ul>
    </div>
  )
}

export default HomeNavbar;