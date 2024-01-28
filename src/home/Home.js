import Buttonn from "../comp/Buttonn";
import Input from "../comp/Input";
import Logo from "../comp/Logo";
import img from "../images/pexels-ekaterina-bolovtsova-6077089 1.png";
import img1 from "../images/lawyer_beth_bloom_31366_1700609055.jpg";
import img2 from "../images/picture_147913h.jpeg";
import img3 from "../images/picture_141176h.png";
import img4 from "../images/Rectangle 16.png";
import img6 from "../images/Rectangle 16.png";
import "./home.css";
import HomeNavbar from "./home_navbar/HomeNavbar";
import LawyersList from "./top_lawyers/LawyersList";
import { MdEmail, MdFacebook, MdPhone, MdLocationOn } from "react-icons/md";
import img5 from "../images/imageshh.png";
import { Link } from "react-router-dom";

const Home = () => {
  const lawyers = [
    {
      name: "Maria Garcia",
      img: img1,
      value: "4",
      location: "Barcelona, Spain",
    },
    { name: "FOUAD TAREK", img: img2, value: "4", location: "BOUABSA, Batna" },
    {
      name: "ZEGH ABDELKADER",
      img: img3,
      value: "3",
      location: "Tissemsilt Algérie",
    },
    { name: "Azizi Faho", img: img4, value: "5", location: "Germany, Munich" },
    { name: "Sophie Martin", img: img5, value: "4", location: "Paris, France" },
    { name: "Mohammed Ahmed", img: img6, value: "3", location: "Cairo, Egypt" },
  ];
  return (
    <div className="home">
      <div className="home-pic">
        <img src={img} alt="background" className="home-picc" />
        <Logo className="logo" />
        <Link to="#">
          {" "}
          <Buttonn id="Connexion" class="Connexion-submit" label="welcome Bafdel moufdi" />
        </Link>
        <div className="diff">
          <h3>
            Welcome to DZ Mouhami, your trusted guide to legal expertise in
            Algeria. Connect with the finest legal minds nationwide, ensuring
            you find the right advocate for your unique needs
          </h3>
        </div>
        <div className="content">
          <div className="recherch">
            <div className="r1">
              <h1>
                Experienced lawyers are<br></br> ready to help.
              </h1>
            </div>
            <div className="r2">
              <h3>Find a lawyer</h3>
              <Input class="serche-bare" label="Search..." />
              <Buttonn id="recherche" class="recherche-submit" label="Submit" />
            </div>
          </div>
        </div>
        <div className="content2">
          <div className="home-navbar">
            <HomeNavbar />
          </div>
          <div className="khat"></div>
          <div className="Top-lawyers">
            <h3 className="h3-text">Top-rated lawyers near you</h3>
            <LawyersList lawyers={lawyers} />
          </div>
        </div>
        <div className="about">
          <div className="khat2"></div>
          <div className="abt">
            <div className="DZ-Mouhami">
              <h3>About DZ-Mouhami</h3>
              <p>
                Welcome to DZ-Mouhami, your go-to platform for connecting with
                skilled lawyers in Algeria. Whether you're seeking legal advice,
                representation, or consultation, we're here to simplify the
                process of finding the right legal professional for your needs.
                <br />
                <br />
                At DZ-Mouhami, our mission is to bridge the gap between
                individuals seeking legal assistance and experienced lawyers in
                Algeria. We strive to provide a user-friendly platform that
                empowers users to make informed decisions when choosing legal
                representation.{" "}
              </p>
            </div>
            <div className="Offer">
              <h3>What We Offer</h3>
              <p>
                <span>Comprehensive Lawyer Profiles:</span>
                <br />
                Browse through detailed profiles of registered lawyers,
                including their specializations, experience, and contact
                information.
                <br />
                <br />
                <span>Advanced Search Functionality:</span>
                <br />
                Use our advanced search features to find lawyers based on
                specializations, locations, language preferences, and more.
                <br />
                <br />
                <span>Transparent Reviews and Ratings:</span>
                <br />
                Make confident decisions by reading reviews and ratings from
                other users who have engaged with the lawyers on our platform.
                <br />
                <br />
                <span>Effortless Appointment Scheduling:</span>
                <br />
                Seamlessly schedule appointments with lawyers through our
                intuitive booking system.
              </p>
            </div>
          </div>
          <div className="contact">
            <h3>Our Contact:</h3>
            <ul className="ul">
              <li className="li">
                <a href={`mailto:team_member1@example.com`}>
                  <MdEmail />
                </a>
              </li>
              <li className="li">
                <a href={`mailto:team_member2@example.com`}>
                  <MdPhone />
                </a>
              </li>
              <li className="li">
                <a href={`mailto:team_member3@example.com`}>
                  <MdLocationOn />
                </a>
              </li>
              <li className="li">
                <a href={`mailto:team_member4@example.com`}>
                  <MdFacebook />
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div className="khat3"></div>
      </div>
    </div>
  );
};

export default Home;
