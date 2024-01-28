import React from "react";
import Logo from "../comp/Logo";
import img from "../images/pexels-ekaterina-bolovtsova-6077089 1.png";
import "./lawyerprofil.css";
import img1 from "../images/user.jpeg";
import img2 from "../images/lawyer_beth_bloom_31366_1700609055.jpg"
import { Rating } from "@mui/material";
import Mapp from "../comp/map/Mapp";
import Buttonn from "../comp/Buttonn";
import { useState } from "react";
import LawyerComents from "./lawyer_coments/LawyerComents";
import Input from "../comp/Input";
import Modal from "react-modal";
import { useRef } from "react";
import { useEffect } from "react";

const LawyerProfil = (props) => {
  const [comments, setComments] = useState(null);
  const [commentValue , setCommentValue] = useState("")
  const [modal, setModal] = useState(false);

  const toggleModal = () => {
    setModal(!modal);
  };
  const onSubmitComments = (e) => {
    e.preventDefault();
    setComments((comments) => [...comments, commentValue]);
    console.log(comments)
  };
  const [value, setValue] = useState(2);
  console.log(props.match.params.id);
  console.log(props.match.params.lawyername);
  useEffect(() => {
    const fetchComments = async () => {
      await Promise.resolve((resolve) => setTimeout(() => resolve(), 2000));
      setComments([]);
    };

    fetchComments();
  }, []);
  return (
    <div className="lawyer-profile">
      <div className="top">
        <img src={img} alt="background" className="image" />
        
        <Logo />
      </div>
      <div className="informations">
        <div className="pic-rate">
          <img src={img2} alt="profil-pic" className="l-imggg" />
          <Rating className="l-rateee" name="read-only" value="4" readOnly />
        </div>
        <div className="name-info">
          <h2>Maria Garcia</h2>
          <h3>Numero de telephone :</h3>
          <p>0656789012</p>
          <h3>Email :</h3>
          <p>maria.garcia@gmail.com</p>
          <h3>Langue :</h3>
          <p>Spanish, Catalan</p>
          <h3>Specialites :</h3>
          <p>Employment Law</p>
          <p>Consumer Law</p>
          <p>Healthcare Law</p>
        </div>
        <div className="map-reserve">
          <Mapp />
          <Buttonn
            onClick={toggleModal}
            id="res"
            clas="res"
            label="Prendre un Rendez-vous"
          />
          <div className="rank-me">
            <span>Rate Me :</span>
            <Rating
              id="r"
              name="simple-controlled"
              value={value}
              onChange={(event, newValue) => {
                setValue(newValue);
              }}
            />
          </div>
        </div>
      </div>
      <div className="Evaluations">
        <h3 className="h3">Evaluations :</h3>
        <div className="comments">
          {comments ? (
            comments.length > 0 ? (
              comments.map((comment, index) => (
                <LawyerComents
                  key={index}
                  img={img1}
                  name="Bafdel moufdi"
                  value="4"
                  comment={comment}
                />
              ))
            ) : (
              <p>No comments yet</p>
            )
          ) : (
            <p>Loading</p>
          )}
        </div>
      </div>
      <form className="add-com">
        <Input class="Comment-bare" label="Add Comment..." onChange={(e)=>setCommentValue(e.target.value)} />
        <div>
          <Buttonn id="com-btn" label="Submit" onClick={onSubmitComments} />
        </div>
      </form>

      {modal && (
        <div className="modal">
          <div className="overlay">
            <Modal
              className="modal-content"
              isOpen={modal}
              onRequestClose={toggleModal}
              contentLabel="Example Modal"
            >
              <h3 id="rend-text">Prendre un Rendez-vous</h3>
              <div className="rend-form">
                <Input
                  id="rend-input"
                  label="Name"
                  style={{ width: 75 + "%", margin: 20 + "px" }}
                />
                <Input
                  id="rend-input"
                  label="Email"
                  style={{ width: 75 + "%", margin: 20 + "px" }}
                />
                <Input
                  id="rend-input"
                  label="Phone Number"
                  style={{ width: 75 + "%", margin: 20 + "px" }}
                />
                <Input
                  id="rend-input"
                  label="Description..."
                  style={{ width: "75%", margin: "20px", height: "200px" }}
                />
                <input type="date" id="dateInput" name="dateInput" />
              </div>
              <Buttonn onClick={toggleModal} id="rend-submit" label="Submit" />
            </Modal>
          </div>
        </div>
      )}
    </div>
  );
};

export default LawyerProfil;
