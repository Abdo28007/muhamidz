import Buttonn from '../comp/Buttonn';
import Input from '../comp/Input';
import Logo from '../comp/Logo';
import img from '../images/pexels-ekaterina-bolovtsova-6077089 1.png';
import img1 from '../images/picture_147913h.jpeg'
import img2 from '../images/picture_141200h.jpeg'
import img3 from '../images/picture_141176h.jpeg'
import img4 from '../images/imagesh.jpeg'
import img5 from '../images/user.jpeg'
import img6 from '../images/imageshhh.jpeg'
import img7 from '../images/lawyer_beth_bloom_31366_1700609055.jpg'
import img8 from '../images/imageshh.jpeg'
import img9 from '../images/téléchargéf.jpeg'
import img10 from '../images/téléchargf.jpeg'
import img11 from '../images/picture_123983h.jpeg'
import img12 from '../images/téléchargéh.jpeg'
import img13 from '../images/picture_64719.jpeg'
import '../home/home.css';
import HomeNavbar from '../home/home_navbar/HomeNavbar';
import LowyerCard from './LowyerCard';
import './lawyerpage.css';
import { useEffect, useState } from 'react';
import axios from 'axios';

const LawyerPage = () => {

  const lawyers = [
    { id:'1',name: ' FOUAD TAREK',img:img1, email: 'BENFOUD1@gmail.com',location:'"N⁰ 30, Rue des Frères BOUABSA, Batna',rate:'3',phone:'0646589001',lat:'35.55597',long:'6.17414',lang:'French,Arabic,English',cat1:'Droit administratif',cat2:'Droit bancaire',cat3:'Droit commercial' },
    { id:'2',name: 'Maitre MOHAMED DIF',img:img2, email: 'MOHAD12@gmail.com',location:'Hassi Bahbah 17000, Djelfa, Algérie',rate:'3',phone:'072882900',lat:'34.66666670',long:'3.25000000',lang:'French,Arabic',cat1:' Droit familial',cat2:'Droit commercial',cat3:'Droit administratif' } ,
    { id:'3',name: 'Maitre ZEGHBA ABDELKADER',img:img3, email: 'zaghbaal@gmail.com',location:'N°6 Rue 8  Tissemsilt Algérie',rate:'3',phone:'0546589001',lat:'35.60722',long:'1.81081',lang:'French,English',cat1:'Droit civil',cat2:'Droit bancaire',cat3:'Droit administratif' },
    { id:'4', name: 'John Doe', img:img4, email: 'john.doe@gmail.com', location: 'New York, USA', rate: '4', phone: '1234567890', lat: '40.7128', long: '-74.0060', lang: 'English, Spanish', cat1: 'Criminal Law', cat2: 'Personal Injury', cat3: 'Family Law' },
    { id:'5', name: 'Alice Johnson', img:img5, email: 'alice.johnson@gmail.com', location: 'Los Angeles, USA', rate: '5', phone: '9876543210', lat: '34.0522', long: '-118.2437', lang: 'English, French', cat1: 'Real Estate Law', cat2: 'Immigration Law', cat3: 'Corporate Law' },
    { id:'6', name: 'Robert Smith', img:img6, email: 'robert.smith@gmail.com', location: 'London, UK', rate: '3', phone: '3456789012', lat: '51.5074', long: '-0.1278', lang: 'English, German', cat1: 'Intellectual Property', cat2: 'Tax Law', cat3: 'Environmental Law' },
    { id:'7', name: 'Maria Garcia', img:img7, email: 'maria.garcia@gmail.com', location: 'Barcelona, Spain', rate: '4', phone: '4567890123', lat: '41.3851', long: '2.1734', lang: 'Spanish, Catalan', cat1: 'Employment Law', cat2: 'Consumer Law', cat3: 'Healthcare Law' },
    { id:'8', name: 'Mohammed Ahmed', img:'', email: 'mohammed.ahmed@gmail.com', location: 'Cairo, Egypt', rate: '5', phone: '7890123456', lat: '30.0444', long: '31.2357', lang: 'Arabic, English', cat1: 'Islamic Law', cat2: 'Property Law', cat3: 'Commercial Law' },
    { id:'9', name: 'Sophie Martin', img:img8, email: 'sophie.martin@gmail.com', location: 'Paris, France', rate: '3', phone: '9876543210', lat: '48.8566', long: '2.3522', lang: 'French, German', cat1: 'Intellectual Property', cat2: 'Privacy Law', cat3: 'Family Law' },
    { id:'10', name: 'Daniel Kim', img:'', email: 'daniel.kim@gmail.com', location: 'Seoul, South Korea', rate: '4', phone: '1234567890', lat: '37.5665', long: '126.9780', lang: 'Korean, English', cat1: 'Technology Law', cat2: 'Data Protection', cat3: 'International Trade Law' },
    { id:'11', name: 'Isabel Hernandez', img:'', email: 'isabel.hernandez@gmail.com', location: 'Mexico City, Mexico', rate: '5', phone: '2345678901', lat: '19.4326', long: '-99.1332', lang: 'Spanish, English', cat1: 'Environmental Law', cat2: 'Human Rights Law', cat3: 'Corporate Law' },
    { id:'12', name: 'Rahul Sharma', img:'', email: 'rahul.sharma@gmail.com', location: 'Mumbai, India', rate: '3', phone: '3456789012', lat: '19.0760', long: '72.8777', lang: 'Hindi, English', cat1: 'Constitutional Law', cat2: 'Immigration Law', cat3: 'Labor Law' },
    { id:'13', name: 'Olga Ivanova', img:img9, email: 'olga.ivanova@gmail.com', location: 'Moscow, Russia', rate: '4', phone: '4567890123', lat: '55.7558', long: '37.6176', lang: 'Russian, English', cat1: 'Family Law', cat2: 'Criminal Law', cat3: 'Real Estate Law' },
    { id:'14', name: 'Diego Fernandez', img:'', email: 'diego.fernandez@gmail.com', location: 'Buenos Aires, Argentina', rate: '5', phone: '5678901234', lat: '-34.6118', long: '-58.4173', lang: 'Spanish, Portuguese', cat1: 'Bankruptcy Law', cat2: 'International Law', cat3: 'Tax Law' },
    { id:'15', name: 'Aisha Al-Mansoori', img:img10, email: 'aisha.almansoori@gmail.com', location: 'Dubai, UAE', rate: '3', phone: '6789012345', lat: '25.276987', long: '55.296249', lang: 'Arabic, English', cat1: 'Islamic Finance Law', cat2: 'Maritime Law', cat3: 'Arbitration Law' },
    { id:'16', name: 'Carlos Rodriguez', img:img11, email: 'carlos.rodriguez@gmail.com', location: 'Santiago, Chile', rate: '4', phone: '7890123456', lat: '-33.4489', long: '-70.6693', lang: 'Spanish, English', cat1: 'Consumer Protection', cat2: 'Intellectual Property', cat3: 'Civil Rights Law' },
    { id:'17', name: 'Yuki Tanaka', img:'', email: 'yuki.tanaka@gmail.com', location: 'Tokyo, Japan', rate: '5', phone: '8901234567', lat: '35.6895', long: '139.6917', lang: 'Japanese, English', cat1: 'Cybersecurity Law', cat2: 'Technology Law', cat3: 'Privacy Law' },
    { id:'18', name: 'Antonio Silva', img:img12, email: 'antonio.silva@gmail.com', location: 'Lisbon, Portugal', rate: '3', phone: '0123456789', lat: '38.7223', long: '-9.1393', lang: 'Portuguese, Spanish', cat1: 'Real Estate Law', cat2: 'Employment Law', cat3: 'Family Law' },
    { id:'19', name: 'Nadia Ahmedov', img:img13, email: 'nadia.ahmedov@gmail.com', location: 'Baku, Azerbaijan', rate: '4', phone: '2345678901', lat: '40.4093', long: '49.8671', lang: 'Azerbaijani, Russian', cat1: 'Oil and Gas Law', cat2: 'Contracts Law', cat3: 'International Trade Law' },
    { id:'20', name: 'Seung-Ho Kim', img:'', email: 'seungho.kim@gmail.com', location: 'Seoul, South Korea', rate: '5', phone: '3456789012', lat: '37.5665', long: '126.9780', lang: 'Korean, English', cat1: 'Corporate Law', cat2: 'Mergers and Acquisitions', cat3: 'International Business Law' }
];
 {/*
const [lawyers, setLawyers] = useState([]);
useEffect(() => {
  // Use Axios to fetch lawyer data
  const fetchLawyers = async () => {
    try {
      // Replace the URL below with the actual endpoint of your lawyer data API
      const response = await axios.get('https://muhami.onrender.com/lawyers/');
      setLawyers(response.data);
      console.log(response);
    } catch (error) {
      console.error('Error fetching lawyers:', error);
    }
  };

  // Call the fetchLawyers function when the component mounts
  fetchLawyers();
}, []);
*/}
  return (
    <div className="home">
    <div className="home-pic">
       <img src={img} alt="background" className='home-picc'/>
       <Logo className='logo'/>
       <Buttonn 
           id='Connexion'
           class='Connexion-submit'
           label='Connexion'
          />
       <div className='diff'>
         <h3>Welcome to DZ Mouhami, your trusted guide to legal expertise in Algeria. Connect with the finest legal minds nationwide, ensuring you find the right advocate for your unique needs</h3>
       </div>
       <div className='content'>
        <div className='recherch'>
            <div className='r1'>
            <h1>Experienced lawyers are<br></br> ready to help.</h1>   
            </div>
            <div className='r2' >
              <h3>Find a lawyer</h3>
              <Input
                  class="serche-bare"
                  label='Search...'
                 />
              <Buttonn
                  id='recherche'
                  class='recherche-submit'
                  label='Submit'
              />
            </div>
        </div>

       </div>
       <div className='content2'>
         <div className='home-navbar'>
           <HomeNavbar />
         </div>
         <div className='khat'></div>

         <div className='lowyerlist'>
         {lawyers.map(lawyer => (
        <LowyerCard
          id={lawyer.id}
          img={lawyer.img}
          name={lawyer.name}
          adr={lawyer.email}
          location={lawyer.location}
          value={lawyer.rate}
        />
      ))}
        </div>
       </div>
    </div>

    </div>
  )
}

export default  LawyerPage;
    