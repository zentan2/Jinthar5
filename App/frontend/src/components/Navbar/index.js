import React from 'react';
import {
  Nav,
  NavLink,
  // Bars,
  NavMenu,
  NavBtn,
  NavBtnLink
} from './NavbarElements';
import logo from '../../assets/citi.png';

const Navbar = () => {
  return (
    <>
      <Nav>
        <NavLink to='/'>
          <img src={logo} alt='logo' />
        </NavLink>
        {/* <Bars /> */}
        <NavMenu>
          <NavLink to='/portfolio' activeStyle>
            Portfolio
          </NavLink>
          <NavLink to='/markets' activeStyle>
            Markets
          </NavLink>
        </NavMenu>
      </Nav>
    </>
  );
};

export default Navbar;