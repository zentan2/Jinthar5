import React, { useEffect } from "react";
import api from "../api";
import Navbar from "../../components/Navbar";
import Collapsible from "../../components/Collapsible/Collapsible";

var SGList = new Array();
var SGtable = new Array();
var USList = new Array()
var UStable = new Array();

/********************************** SG TABLE **********************************/
fetch("http://127.0.0.1:5000/api/portfolio")
  .then((response) => response.json()) // one extra step
  .then((data) => {
    /**aggregate data here**/

    data.Portfolio.forEach((item, index) => {
      if (item.Country == "SGD") {
        SGList.push(
          <table>
            <tr>
              <td>{item.Name}</td>
              <td>
                {item.MarketValue} / {item.Quantity}
              </td>
              <td>{item.Price}</td>
              <td>{item.DailyPnL}</td>
              <td>{item.UnrealisedPnL}</td>
            </tr>
          </table>
        );
      }
    });
  })
  .catch((error) => console.error(error));

fetch("http://127.0.0.1:5000/api/portfolio/total/SGD")
  .then((response) => response.json()) // one extra step
  .then((data) => {
    /**aggregate data here**/
    SGtable.push(
      <Collapsible label={data}>
        <ul>{SGList}</ul>
      </Collapsible>
    );
  })
  .catch((error) => console.error(error));
/********************************** SG TABLE **********************************/

/********************************** US TABLE **********************************/

fetch("http://127.0.0.1:5000/api/portfolio")
  .then((response) => response.json()) // one extra step
  .then((data) => {
    /**aggregate data here**/

    data.Portfolio.forEach((item, index) => {
      if (item.Country == "USD") {
        USList.push(
          <table>
            <tr>
              <td>{item.Name}</td>
              <td>
                {item.MarketValue} / {item.Quantity}
              </td>
              <td>{item.Price}</td>
              <td>{item.DailyPnL}</td>
              <td>{item.UnrealisedPnL}</td>
            </tr>
          </table>
        );
      }
    });
  })
  .catch((error) => console.error(error));

fetch("http://127.0.0.1:5000/api/portfolio/total/USD")
  .then((response) => response.json()) // one extra step
  .then((data) => {
    /**aggregate data here**/
    UStable.push(
      <Collapsible label={data}>
        <ul>{USList}</ul>
      </Collapsible>
    );
  })
  .catch((error) => console.error(error));

  /********************************** US TABLE **********************************/



const Portfolio = () => {
  return (
    <div className="Portfolio">
      <Navbar />
      {/* <Collapsible/> */}
      {/* <ul>{countryList}</ul> */}
      <table>
        {SGtable}
        {UStable}
        </table>
    </div>
  );
};

export default Portfolio;
