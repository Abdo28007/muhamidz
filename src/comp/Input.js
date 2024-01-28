import TextField from '@mui/material/TextField';

const Input = (props) => {
  return (
    <div className='input'>
       <TextField {...props} style={props.style} className={props.className} label={props.label} variant={props.variant}  />
    </div>
  )
}

export default Input;