import React from 'react'
import './lowyercard.css'
import { Rating } from '@mui/material';
import { FaMapMarkerAlt } from 'react-icons/fa';
import { Link } from 'react-router-dom';

const LowyerCard = (props) => {
  return (
    <Link to={`/${props.id}/${props.name}`} className='l-card'>
         <img className='l-imgg' src={props.img} alt='lawyer-pic'/>
         <h3 className='l-namee'>{props.name}</h3> 
         <p className='l-adrr'>{props.adr}</p>
         <p className='l-locc'><FaMapMarkerAlt/>&nbsp;&nbsp; {props.location}</p>
         <Rating className='l-ratee' name="read-only" value={props.value} readOnly />
         <p className='more'>Show More...</p>
    </Link>
  )
}

export default LowyerCard;