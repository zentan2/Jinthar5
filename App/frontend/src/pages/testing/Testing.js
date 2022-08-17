import React, { useEffect } from "react";
import api from "../api";
import Navbar from "../../components/Navbar";
import Collapsible from "../../components/Collapsible/Collapsible";

var SGList = new Array();
var my_SG;

    fetch("http://127.0.0.1:5000/api/portfolio")
    .then((response) => response.json()) // one extra step
    .then((data) => {
      /**aggregate data here**/
  
      data.Portfolio.forEach((item, index) => {
        if (item.Country == "SGD") {
            SGList = Object.values(data.Portfolio).map(Object.values)
  
            //   for (var key of Object.keys(item)) {
            // SGList.push([item.id, item[key]]);
          // }
        }
      
      });
      
    })
    .catch((error) => console.error(error));


console.log("obj", SGList);
console.log(SGList.length);


const Testing = () => {
  return (
    <div className="Testing">
      <Navbar />
      
      <ul>{SGList}</ul>
    </div>
  );
};

export default Testing;
