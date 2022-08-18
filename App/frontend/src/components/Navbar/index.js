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


const Navbar = () => {

  return (
    <>
      <Nav>
        <NavLink to="/">
          <img src={logo} alt="logo" width="150" height="110" />
        </NavLink>
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
