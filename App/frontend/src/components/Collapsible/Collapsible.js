import React, { useState, useRef } from "react";
import "./Collapsible.css";
const Collapsible = (props) => {
  const [open, setOpen] = useState(false);
  const toggle = () => {
    setOpen(!open);
  };
  return (
    <div className="collapsible">
      <div className={open ? "content-show" : "content-parent"}>
        <button className="collapse-button" onClick={toggle}>
<<<<<<< HEAD
          {props.label.Country} Total Market Value ({props.label.Country}):
          {props.label.PortfolioMarketValueTotal}
          Total Daily P&L: {props.label.PortfolioDailyPnLTotal}
          Total Unrealised P&L: {props.label.PortfolioUnrealisedPnLTotal}
=======
          <p>
          {props.label.Country} Total Market Value ({props.label.Country}): {props.label.PortfolioMarketValueTotal}
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Total Daily P&L: {props.label.PortfolioDailyPnLTotal}
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Total Unrealised P&L: {props.label.PortfolioUnrealisedPnLTotal}
          </p>
>>>>>>> origin/janel-fe
        </button>

        <div>
          {open && (
            <div className="content">
              <table>
                <tr>
                  <th>Name/Ticker Symbol</th>
<<<<<<< HEAD
                  <th>MV/Qty</th>
                  <th>Price/Cost</th>
=======
                  <th>Price/Qty</th>
                  <th>Cost</th>
>>>>>>> origin/janel-fe
                  <th>Daily Profit and Loss</th>
                  <th>Unrealised Profit and Loss</th>
                </tr>
              </table>
              {props.children}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
export default Collapsible;
