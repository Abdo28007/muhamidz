import { FaStar } from 'react-icons/fa';
import './lawyercoments.css';

const LawyerComents = (props) => {
  return (
    <div className='com'>
     <img  className='c-img' src={props.img} alt='user-image'/>
     <h3 className='c-name'>{props.name}</h3>
      <p className='c-rate'><FaStar color='#165386'/><span>{props.value} Etoiles</span></p>
      <p className='c-com'>{props.comment}</p>
    </div>
  )
}

export default LawyerComents;