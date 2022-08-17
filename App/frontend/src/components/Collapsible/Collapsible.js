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
          {props.label.Country} Total Market Value ({props.label.Country}):
          {props.label.PortfolioMarketValueTotal}
          Total Daily P&L: {props.label.PortfolioDailyPnLTotal}
          Total Unrealised P&L: {props.label.PortfolioUnrealisedPnLTotal}
        </button>

        <div>
          {open && (
            <div className="content">
              <table>
                <tr>
                  <th>Name/Ticker Symbol</th>
                  <th>MV/Qty</th>
                  <th>Price/Cost</th>
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
