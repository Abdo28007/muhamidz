import { Rating } from '@mui/material';
import './lawyercard.css';
import { FaMapMarkerAlt } from 'react-icons/fa';

const LawyerCard = (props) => {
  return (
    <div className='Card'> 
        <img src={props.img} className='l-pic'/>
        <p className='l-name'>{props.name}</p>
        <Rating className='l-rate'name="read-only" value={props.value} readOnly />
        <p className='l-loc'><FaMapMarkerAlt/>&nbsp;&nbsp; {props.location}</p>
    </div>
  )
}

export default LawyerCard;