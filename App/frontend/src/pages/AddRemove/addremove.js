import React from "react";
import api from "../api";
import Navbar from "../../components/Navbar";
import "./addremove.css";
import { useNavigate } from "react-router-dom";

function refreshPage() {
  window.location.reload(false);
}

const AddRemove = () => {
  document.title = "Update";

  let [ticker, setTicker] = React.useState("");
  let [country, setCountry] = React.useState("");
  let [quantity, setQuantity] = React.useState("");
  let [price, setPrice] = React.useState("");
  let [status, setStatus] = React.useState(" ");

  let handleSubmitAdd = async (e) => {
    e.preventDefault();
    try {

      let res = await fetch(
        "http://linuxapacgtcb46.conygre.com:8081/api/portfolio/add",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            ticker: ticker,
            quantity: quantity,
            country: country,
            price: price,
          }),
        }
      );
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

    let text;
    alert("Update - Add Successful!");
    text =
      "You have added " +
      quantity +
      " " +
      ticker +
      " (" +
      country +
      ")" +
      " at $" +
      price +
      " each!";
    alert(text);
    refreshPage()
  };

  let handleSubmitRemove = async (e) => {
    e.preventDefault();
    try {

      let res = await fetch(
        "http://linuxapacgtcb46.conygre.com:8081/api/portfolio/delete",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            ticker: ticker,
            quantity: quantity,
            country: country,
            price: price,
          }),
        }
      );
      let resJson = await res.json();
      if (res.status === 200) {
        setTicker("");

        setCountry("");

        setStatus("Stock removed successfully");
      } else {
        setStatus("Some error occured");
      }
    } catch (err) {
      console.log(err);
    }

    let text;
    alert("Update - Remove Successful!");
    text = "You have removed all " + ticker + " (" + country + ")" + "!";
    alert(text);
    refreshPage()
  };

  let handleSubmitEdit = async (e) => {
    e.preventDefault();
    try {

      let res = await fetch(
        "http://linuxapacgtcb46.conygre.com:8081/api/portfolio/update",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            ticker: ticker,
            quantity: quantity,
            country: country,
            price: price,
          }),
        }
      );
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

    let text;
    alert("Update - Edit Successful!");
    text =
      "You now have " +
      quantity +
      " of " +
      ticker +
      " (" +
      country +
      ")" +
      " at $" +
      price +
      " each!";
    alert(text);
    refreshPage()
  };

  return (
    <div className="Stocks">
      <Navbar />
      <form className="form" onSubmit={handleSubmitAdd}>
        <div className="input-group">
          <label htmlFor="ticker">Ticker </label>
          <input
            required
            id="ticker"
            type="ticker"
            name="ticker"
            placeholder="Example: AAPL, TSLA"
            value={ticker}
            onChange={(e) => setTicker(e.target.value)}
          />
        </div>

        <div className="input-group">
          <label htmlFor="Country">Country </label>
          <input
            id="country"
            type="text"
            name="country"
            placeholder="USD or SGD only"
            required
            value={country}
            onChange={(e) => setCountry(e.target.value)}
          />
        </div>

        <div className="input-group">
          <label htmlFor="quantity">Quantity </label>
          <input
            required
            id="quantity"
            type="number"
            name="quantity"
            placeholder="Numerical values only"
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
          />
        </div>

        <div className="input-group">
          <label htmlFor="price">Price </label>
          <input
            required
            id="price"
            type="number"
            name="price"
            placeholder="Numerical values only"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
          />
        </div>

        <button className="Add">Add</button>

        <button className="Remove" onClick={handleSubmitRemove}>
          Remove
        </button>

        <button className="Status" onClick={handleSubmitEdit}>
          Edit
        </button>

        <div className="message">{status ? <p>{status}</p> : null}</div>
      </form>
    </div>
  );
};

export default AddRemove;
