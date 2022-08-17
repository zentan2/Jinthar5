import React from "react";
import api from '../api'
import Navbar from '../../components/Navbar'
import './bstest.css';
import { useNavigate } from 'react-router-dom';
import axios from "axios"

// var script = document.createElement('script');
// script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
// document.getElementsByTagName('head')[0].appendChild(script);

const BSTest = () => {
  let [ticker, setTicker] = React.useState('')
  let [country, setCountry] = React.useState('')
  let [quantity, setQuantity] = React.useState('')
  let [price, setPrice] = React.useState('')
  let [ar, setAr] = React.useState('')
  
  function submitAdd(e) {
    e.preventDefault();
    let text;
    alert("Update - Add Succesfull!")
    text = "You have added " + ticker + " (" + country + ") with a quantity value of " + quantity + " at $" + price + " each!";
    document.getElementById("udAdd").style.color = 'white';
    document.getElementById("udAdd").innerHTML = text;
  };

  function submitRemove(e) {
    e.preventDefault();
    let text;
    alert("Update - Remove Succesfull!")
    text = "You have removed " + ticker + " (" + country + ") with a quantity value of " + quantity + " at $" + price + " each!";
    document.getElementById("udRemove").style.color = 'white';
    document.getElementById("udRemove").innerHTML = text;    
  };

  // function overallUD(e) {
  //   e.preventDefault();
  //   let text;    
  //   text = "You have " + ar + " " + ticker + " (" + country + ") with a quantity value of " + quantity + " at $" + price + " each!";
  //   document.getElementById("oUD").style.color = 'white';
  //   document.getElementById("oUD").innerHTML = text;    
  // };

  // async function postData() {
  //   let user = {
  //     Id: 78912,
  //     Customer: "Jason Sweet",
  //     Quantity: 1
  //   }
  
  //   try {
  //     const response = await axios.post("https://reqbin.com/echo/post/json", user)
  //     console.log("Request successful!")
  //   } catch (error) {
  //     if (error.response) {
  //       console.log(error.reponse.status)
  //     } else {
  //       console.log(error.message)
  //     }
  //   }
  // }
  // postData();

  async function postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, *cors, same-origin
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'same-origin', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: 'follow', // manual, *follow, error
      referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }

  fetch("http://127.0.0.1:5000/api/portfolio")
  .then((response) => response.json()) // one extra step
  .then((data) => {
    /**aggregate data here**/

    var SGList = new Array();
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

  // $.ajax({
  //   type: "POST",
  //   url: "https://reqbin.com/echo/post/json",
  //   data: `{
  //     "Id": 78912,
  //     "Customer": "Jason Sweet",
  //   }`,
  //   success: function (result) {
  //      console.log(result);
  //   },
  //   dataType: "json"
  // });

          postData('http://127.0.0.1:5000/api/portfolio/add', { answer: 42 })
          .then((data) => {
          console.log(data); // JSON data parsed by `data.json()` call
          }); 
  
    return (
      <div className="Stocks">
        
         <form className="form" onSubmit={submitAdd}> 
         
         <div className="input-group">
            <label htmlFor="ticker">Ticker </label>
            <input required             
            id="ticker" 
            type="ticker" 
            name="ticker" 
            placeholder='Example: AAPL, TSLA'
            value={ticker} 
            onChange={(e) => setTicker(e.target.value)}            
            />
          </div>
          
          <div className="input-group">
            <label htmlFor="Country">Country </label>
            <input             
            id="country" 
            type="country" 
            name="country" 
            placeholder='USD or SGD only'
            required value={country}  
            onChange={(e) => setCountry(e.target.value)}
            />
          </div>        
                   
          <div className="input-group">
            <label htmlFor="quantity">Quantity </label>
            <input required  
            id="quantity" 
            type="quantity" 
            name="quantity" 
            placeholder='Numerical values only' 
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
            />
          </div>
          
          <div className="input-group">
            <label htmlFor="price">Price </label>
            <input  required 
            id="price" 
            type="price" 
            name="price" 
            placeholder='Numerical values only' 
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            />
          </div>
         
          <button className="Add"> 
            Update - Add
          </button>

          <button className="Remove" onClick={submitRemove}>
            Update - Remove 
          </button>

          {/* <button className="Remove" onChange={(e) => setAr(e.target.value)} ar = 'removed' onClick={overallUD}>
            Update - Remove Dynamic
          </button> */}

          <p id="udAdd"> </p> 

          <p id="udRemove"> </p>
          
          <p id="oUD"> </p>

          </form>

          
          {/* POST request using fetch()
          fetch("http://127.0.0.1:5000/api/portfolio/add",{
     
          
          method: "POST",
     
          // Adding body or contents to send
          body: JSON.stringify({
          title: "foo",
          body: "bar",
          userId: 1
          }),
     
          // Adding headers to the request
          headers: {
          "Content-type": "application/json; charset=UTF-8"
            }
          })

           {/* Converting to JSON */}
          {/* .then(response => response.json()) */}
 
           {/* Displaying results to console */}
          {/* .then(json => console.log(json)); */}                     
                  
          </div>
          

         
    );
  
}

export default BSTest;