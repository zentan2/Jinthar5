import React from 'react'
import api from '../api'
import Navbar from '../../components/Navbar'
import {
  LineChart,
  XAxis,
  CartesianGrid,
  Line,
  Tooltip,
  YAxis,
  Label
} from 'recharts'  

const Example = () => {
    // Create state variables
    let [responseData, setResponseData] = React.useState('')
    let [ticker, setTicker] = React.useState('')
    let [message, setMessage] = React.useState('')
    // fetches stock data based on parameters
    const fetchData = (e) => {
        e.preventDefault()
        setMessage('Loading...')
        api.stockTimeSeries(ticker)
        .then((response)=>{
           setResponseData(response.data)
           setMessage('')
           console.log(response)
        })
        .catch((error) => {
           setMessage('Error')
           console.log(error)
        })
        }
        
        function handleClick (e){
            e.preventDefault();        
            alert("Place Holder for Pop Up");
          };
          
        function promptbs() {
            let text;
            let quantity = prompt("Quantity:", "Min Value 1");
            if (quantity == null || quantity == "") {
              text = "User cancelled the prompt.";
            } else {
              text = "You have updated quantiy value of " + quantity + "!";
            }
            document.getElementById("quantityinput").innerHTML = text;
          }

        function openForm() {
            document.getElementById("loginPopup").style.display = "block";
          }
          function closeForm() {
            document.getElementById("loginPopup").style.display = "none";
          }
          // When the user clicks anywhere outside of the modal, close it
          window.onclick = function (event) {
            let modal = document.getElementById('loginPopup');
            if (event.target == modal) {
              closeForm();
            }
          }

          var popupWindow = null;


    return (
        <div
            style={{
                background: '#EEE',
                padding: '10%',
            }}
            >
            <Navbar/>
            <h1
                style={{
                    background: 'black',
                    color: 'white',
                    padding: '1rem',
                    display: 'inline-block'
                }}>Stock Market</h1>
            <h2>Analyze Stock Data</h2>
            <form onSubmit={fetchData}>
                <fieldset style={{padding:4}}>
                    <legend>Search Stock Market</legend>
                    <label style = {{ 
                        paddingLeft: 10,
                        // paddingRight: 450,
                        }}htmlFor="ticker">
                Enter Here:    
                        <input
                            style={{
                                marginInline: 10,
                                inlineSize: 624
                            }}
                            required
                            name="ticker"
                            id="ticker"
                            type='text'
                            placeholder='Insert stock ticker such as AAPL, TSLA etc.'
                            value={ticker}
                            onChange={(e) => setTicker(e.target.value)}
                        />
                    </label>
                    <button type='submit'
                    style={{
                        borderRadius: 5,
                        marginBottom: 10,
                        cursor: PointerEvent,
                        maxWidth: 150,
                        background: '#0e6d8a'}}>Submit</button>
                </fieldset>
            </form>
            <p>{message}</p>
            <h3>Symbol: {responseData ? responseData.symbol : ''}</h3>
            <p>Daily Time Series with Splits and Dividend Events</p>
            <small>Last Refresh: {responseData ? responseData.refreshed : ''}</small>
            <LineChart
                width={900}
                height={400}
                data={responseData.closePrices}
                margin={{ top: 50, right: 20, left: 10, bottom: 5 }}
                >
                <YAxis tickCount={10} type="number" width={80}>
                    <Label value="Close Price" position="insideLeft" angle={270} />
                </YAxis>
                <Tooltip />
                <XAxis padding={{left: 5, right: 5}} tickCount={10} angle={-60} height={90} dataKey="date" />
                <CartesianGrid stroke="#f5f5f5" />
                <Line type="monotone" dataKey="close" stroke="#ff7300" yAxisId={0} />
            </LineChart>

            {/*} <button type='buysell'
                    style={{
                        borderRadius: 5,
                        marginBottom: 10,
                        justifyContent: 'center',
                        alignItems: 'center',
                        position: 'relative',
                        cursor: PointerEvent,
                        maxWidth: 150,
                        background: '#d4281c'}}>Buy / Sell Stock
                    </button> */} 
             
            <button className="bullsellb" 
            style={{background: '#d4281c'}}
            onClick={promptbs} >
            Buy / Sell Stock Button 1
            </button>
            <p id="quantityinput"></p>  
            

            <button className="bullsellbb" 
            style={{background: '#d4281c'}}
            onClick={openForm} >
            Buy / Sell Stock Button 2
            </button>
            <p id="quantityinput"></p>  
        
           {/* Click for Redirect*/}
            <p><a href="http://localhost:3000/" onclick="centeredPopup(this.href,'myWindow','700','300','yes');return false">Home Page Redirect</a></p>        
            
            {/* need create new function and don't use on submit to update*/}                    
            <form onSubmit={fetchData}> 
                <fieldset style={{padding:4}}>
                    <legend>Update Stock Quantity</legend>
                    <label style = {{ 
                        paddingLeft: 10,
                        // paddingRight: 450,
                        }}htmlFor="ticker">
                   
                       
                    </label>
                    Quantity: 
                    <input style={{
                                marginInline: 10,
                                inlineSize: 100
                            }} type="number" id="Quantity" />
                    Cost:
                    <input style={{
                                marginInline: 10,
                                inlineSize: 100
                            }} type="number" id="Cost" />        

                    <button type='submit'
                    style={{
                        borderRadius: 5,
                        marginBottom: 10,
                        cursor: PointerEvent,
                        maxWidth: 150,
                        background: '#0e6d8a'}}>Update</button>
                </fieldset>
            </form>
        </div>        
    )
}

export default Example