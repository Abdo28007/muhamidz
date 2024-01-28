import './map.css';

const Mapp = () => {
  const coordinates = {
    latitude: 48.8566, // Paris latitude
    longitude: 2.3522, // Paris longitude
  };

  const iframeSrc = `https://maps.google.com/maps?q=${coordinates.latitude},${coordinates.longitude}&output=embed`;

  return (
    <div className="map">
      <iframe
        width="100%"
        height="300"
        frameBorder="0"
        scrolling="no"
        marginHeight="0"
        marginWidth="0"
        title="Google Map"
        src={iframeSrc}
      >
        <a href="https://www.maps.ie/population/">Population mapping</a>
      </iframe>
    </div>
  );
};

export default Mapp;
