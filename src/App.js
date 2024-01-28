import Home from "./home/Home";
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import LawyerPage from "./lawyers_page/LawyerPage";
import LawyerProfil from "./lawyer_profil/LawyerProfil";
import Profil from "./profil/Profil";
import LoginPage from "./log-in_sign-up/LoginPage";
import AvocatSignUp from './log-in_sign-up/AvocatSignUp'
import AccusedSignUp from './log-in_sign-up/AccusedSignUp'

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/Lawyers"  component={LawyerPage} />
          <Route path="/:id/:lawyername"  component={LawyerProfil} />
          <Route path="/Profil"  component={Profil} />
          <Route path="/AccusedSignUp"  component={AccusedSignUp} />
          <Route path="/AvocatSignUp"  component={AvocatSignUp} />
          <Route path="/LoginPage"  component={LoginPage} />



          
        </Switch>
    </div>
   </Router>
  );
}

export default App;
