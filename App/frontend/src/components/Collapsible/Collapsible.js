import React, { useState, useRef } from 'react';

const Collapsible = (props) => {
    const [open, setOPen] = useState(false);
    const toggle = () => {setOPen(!open)};
    return (
        <div className="collapsible">
            <div className={ open ? "content-show" : "content-parent"} >
                <button onClick={toggle}> {props.label} </button>
                {open && <div className="content"> {props.children} </div>}
            </div>
        </div>
    );
};

export default Collapsible;


{/*/div><button className="toggle" onClick={toggle}>{props.label}</button>
          {open && (
            <div className="toggle">
              <h4>more details</h4>
            </div>
          )}
          </div>*/}