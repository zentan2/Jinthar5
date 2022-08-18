import React, { useState, useCallback } from "react";
import api from "../api";
import Navbar from "../../components/Navbar";
import Collapsible from "../../components/Collapsible/Collapsible";
import "./portfolio.css";
import { Nav } from "../../components/Navbar/NavbarElements";

var SGList = new Array();
var SGtable = new Array();
var USList = new Array();
var UStable = new Array();

/********************************** SG TABLE **********************************/

// function getSG() {
// fetch("http://linuxapacgtcb46.conygre.com:8081/api/portfolio")
//  .then(response => {response.json(); })
//  .then((data) => {
//     data.Portfolio.forEach((item, index) => {
    
//           var SGlist= "";
//           if (item.Country == "SGD") {
         
//             SGlist+="<table>"
//             SGlist += "<tr>";
//             SGlist += "<td>"+item.Name+"</td>";
//             SGlist+= "<td>" + item.MarketValue + "/" + item.Quantity + "</td>";
//             SGlist+=  "<td>" + item.Price + "</td>";
//             SGlist+= "<td>" + item.DailyPnL + "</td>";
//             SGlist+="<td>" + item.UnrealisedPnL + "</td>";
//             SGlist += "</tr>";
//             SGlist+= "</table>"
        
//       }
//       document.getElementById("tbodyitems").innerHTML = SGlist;
//     });
    
//   })
//   .catch((error) => console.error(error));
// }

 fetch("http://linuxapacgtcb46.conygre.com:8081/api/portfolio")
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

fetch("http://linuxapacgtcb46.conygre.com:8081/api/portfolio/total/SGD")
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

 fetch("http://linuxapacgtcb46.conygre.com:8081/api/portfolio")
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

fetch("http://linuxapacgtcb46.conygre.com:8081/api/portfolio/total/USD")
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

  document.title = 'Portfolio';
  return (
    <div className="Portfolio">
    <Navbar/>
      <table>{SGtable}</table>
      <hr></hr>
      <table>{UStable}</table>
    </div>
    
  );
};

export default Portfolio;
