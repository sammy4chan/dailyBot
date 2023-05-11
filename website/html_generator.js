//1. display html code according to corresponding date button pressed
//the only way to maintain scalable code for different days
//-- add code to render number of buttons depending on length of flightdate queries

import { getData, parser } from "./get_data.js";

function button_handler(date){
  //date param is a value which can be substituted to a date

  //obtain values to be useed in making the div rows
  getData(date).then((data) => {
    console.log(parser(data));
    });
};

function clicked(){
  console.log("clicked");
}

export {button_handler, clicked};