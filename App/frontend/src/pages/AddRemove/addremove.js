import React from "react";
import api from '../api'
import Navbar from '../../components/Navbar'
import './addremove.css';
import { useNavigate } from 'react-router-dom';


const AddRemove = () => {
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
    alert(text);   
  };

  function statusUD(e) {
    e.preventDefault();
    let text;
    alert("Update Succesfull!")
    text = ticker + " (" + country + ") with a quantity value of " + quantity + " at $" + price + " each!"; 
    alert(text)    
  };
 
  
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
          
          postData(url = '', data = {})

          </form>
          
          <button className="Status" onClick={statusUD}>
            Status
          </button>        
                 
               
          </div>
                 
    );
  
}

export default AddRemove;