import { useState } from "react";
import React from "react";
import logo from "../../assets/citi.png";

import { useNavigate } from 'react-router-dom';

function Example2() {
  const [ticker, setTicker] = useState("");
  const [quantity, setQuantity] = useState("");
  const [country, setCountry] = useState("");
  const [price, setPrice] = useState("");
  const [status, setStatus] = useState("");

  let handleSubmit = async (e) => {
    e.preventDefault();
    try {
      let res = await fetch("http://127.0.0.1:5000/api/portfolio/add", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ticker: ticker,
          quantity: quantity,
          country: country,
          price: price,
        }),
      });
      let resJson = await res.json();
      if (res.status === 200) {
        setTicker("");
        setQuantity("");
        setCountry("");
        setPrice("");
        setStatus("Stock created successfully");
      } else {
        setStatus("Some error occured");
      }
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="Example2">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={ticker}
          placeholder="Ticker"
          onChange={(e) => setTicker(e.target.value)}
        />
        <input
          type="number"
          value={price}
          placeholder="Price"
          onChange={(e) => setPrice(e.target.value)}
        />
        <input
          type="number"
          value={quantity}
          placeholder="Quantity"
          onChange={(e) => setQuantity(e.target.value)}
        />
        <input
          type="text"
          value={country}
          placeholder="Country"
          onChange={(e) => setCountry(e.target.value)}
        />

        <button type="submit">Create</button>

        <div className="message">{status ? <p>{status}</p> : null}</div>
      </form>
    </div>
  );
}

export default Example2;