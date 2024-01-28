import Button from '@mui/material/Button';

const Buttonn = (props) => {
  return (
    <div className={props.class}>
       <Button onClick={props.onClick} id={props.id} variant="contained">{props.label}</Button>
    </div>
  )
}

export default Buttonn;