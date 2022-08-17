import React from 'react'
import api from '../api'
import Navbar from '../../components/Navbar'
import Collapsible from '../../components/Collapsible/Collapsible'

var countryList = [];

fetch("http://127.0.0.1:5000/api/portfolio/SGD")
  .then((response) => response.json()) // one extra step
  .then((data) => {
    /**aggregate data here**/
    // console.log("HELO",data.Portfolio[0].Country)
    data.Portfolio.forEach((item, index) => {
        // console.log(item.DailyPnL)

      countryList.push(
        <Collapsible label={item.DailyPnL}>
          <table>
            <tr>
              <td>Country</td>
              <td>Market Value</td>
              <td>Name</td>
            </tr>
            <tr>
              <td>{item.Country}</td>
              <td>{item.MarketValue}</td>
              <td>{item.Name}</td>
            </tr>
          </table>
        </Collapsible>
      );
    });
  })
  .catch((error) => console.error(error));
console.log(countryList)

const Portfolio = () => {
    return (
      <div className="Portfolio">
        <Navbar/>
  
        <ul>{countryList}</ul>
        <Collapsible>
          <h1>introduction</h1>
          <p>
            The collapsible component puts long sections of the information under
            a block enabling users to expand or collapse to access its details.
          </p>
    </Collapsible>
      </div>
    );
  };

{/*const Portfolio = () => {
    return (
        <div>
            <Navbar/>
            <p>
                US Market Value (USD)   Total Assets:
                <Collapsible label="US"/>
            </p>
            <p>
                SG Market Value (SGD)   Total Assets:
                <Collapsible label="SG"/>
            </p>
            <p>
                HK Market Value (HKD)   Total Assets:
                <Collapsible label="HK"/>
            </p>
        </div>
    )
}
*/}
export default Portfolio