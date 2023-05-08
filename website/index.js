import getData from "./get_data.js";

function parser(data){
  var flightTimes = [];
  var prices = [];
  var queryTime = [];
  //generating unrepeated flight times: updates flightTimes 
  data.forEach((key) => {
    let depArrTime = [key.depTime, key.arrTime];
    if (flightTimes.length == 0){ //idk why it has to be less than 0 i cannot think rn 
      flightTimes.push(depArrTime);
      prices.push([key.price]);
      queryTime.push([key.queryTime]);
      return;
    };
    for (let i = 0; i < flightTimes.length-0; i++){
      //compare INDIVIDUAL VALUES BECAUSE JS IS BAD
      if ((flightTimes[i][0] == key.depTime) && (flightTimes[i][1] == key.arrTime)){
        prices[i].push(key.price);
        queryTime[i].push(key.queryTime);
        return;
      };
    };
    flightTimes.push(depArrTime);
    prices.push([key.price]);
    queryTime.push([key.queryTime]);
  });


  return {flightTimes, prices, queryTime};
};

getData("13/06/2023").then((rows) => {
  //do smth with rows: we are going to parse it in another function: might make a new module of that
  //console.log(rows);
  console.log(parser(rows));
});