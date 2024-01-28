import React, { useState } from 'react';
import LawyerCard from './LawyerCard';
import { FaChevronRight } from 'react-icons/fa';
import { FaChevronLeft } from 'react-icons/fa';
import '../home.css';
import { Link } from 'react-router-dom/cjs/react-router-dom.min';

const LawyersList = ({ lawyers }) => {
 const [currentIndex, setCurrentIndex] = useState(0);

 const prevPage = (event) => {
    event.preventDefault();
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 3);
    }
 };

 const nextPage = (event) => {
    event.preventDefault();
    if (currentIndex < lawyers.length - 3) {
      setCurrentIndex(currentIndex + 3);
    }
 };

 const displayedLawyers = lawyers.slice(currentIndex, currentIndex + 3);

 return (
    <div className='aaaaaa'>
      {displayedLawyers.map((lawyer, index) => (
        <Link to={`/${lawyer.id}/${lawyer.name}`} className='Cards' key={index}>
          <LawyerCard 
             name = {lawyer.name}
             img = {lawyer.img}
             value={lawyer.value}
             location={lawyer.location}
          />
        </Link>
      ))}
      <button
         onClick={prevPage}
         id='prev'>
        <FaChevronLeft/>
      </button>
     <button
        onClick={nextPage}
        id='next'>
        <FaChevronRight/>
     </button>
    </div>
 );
};

export default LawyersList;