import React, {useState} from "react";
import {
  Nav,
  NavLink,
  // Bars,
  NavMenu,
  NavBtn,
  NavBtnLink,
} from "./NavbarElements";
import logo from "../../assets/citi.png";
import Collapsible from "../../components/Collapsible/Collapsible";
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";
import { FiAlignRight, FiXCircle, FiChevronDown } from "react-icons/fi";
import {Link} from 'react-router-dom';


const Navbar = () => {


  return (
    <>
      <Nav>
        <NavLink to="/">
          <img src={logo} alt="logo" width="150" height="110" />
        </NavLink>
        {/* <Bars /> */}
        <NavMenu>
          <NavLink to="/portfolio" activeStyle>
            Portfolio
          </NavLink>
          <NavLink to="/markets" activeStyle>
            Markets
          </NavLink>
          <NavLink to="/addremove" activeStyle>
            Update Stock
          </NavLink>
          <NavLink to="/" activeStyle>
            
           


            Log Out
          </NavLink>
        </NavMenu>
      </Nav>
    </>
  );
};

export default Navbar;
