import FormLogIn from "./components/FormLogIn";
import FormSignUp from "./components/FormSignUp";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <div className="login-container">
        <Routes>
          <Route path="/" element={<FormLogIn />} />
          <Route path="/signup" element={<FormSignUp />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
