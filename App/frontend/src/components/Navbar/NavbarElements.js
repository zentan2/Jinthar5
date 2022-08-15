// import { FaBars } from 'react-icons/fa';
import { NavLink as Link } from 'react-router-dom';
import styled from 'styled-components';

//Navigation Bar
export const Nav = styled.nav`
  background: #003B70;
  height: 64px;
  display: flex;
  justify-content: space-between;
  padding: 0.5rem calc((100vw - 1000px) / 2);
  z-index: 10;
  width: 100vw;
`;

//Overview, Usage, Error Links
export const NavLink = styled(Link)`
  color: #fff;
  display: flex;
  align-items: center;
  text-decoration: none;
  font-family: 'Roboto', sans-serif;
  padding: 0 1rem;
  height: 100%;
  cursor: pointer;

  &:hover {
    text-decoration: underline;
    text-decoration-thickness: 2px;
    text-decoration-color: #fff;
    text-underline-offset: 8px;
  }
`;

//Overview, Usage, Error
export const NavMenu = styled.div`
  display: flex;
  align-items: center;
  margin-right: 40vh;
  font-size: 14px;
  text-transform: uppercase;

  @media screen and (max-width: 1024px) {
    display: none;
  }
`;
