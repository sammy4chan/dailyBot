import getData from "./get_data.js";

function parser(data){
  var flightTimes = [];
  var prices = [];
  var queryTime = [];
  data.forEach((key) => {
    let depArrTime = [key.depTime, key.arrTime];
    //console.log(depArrTime);
    if (flightTimes.length <= 0){
      flightTimes.push(depArrTime);
      prices.push(key.price);
      queryTime.push(key.queryTime);
    };
    for (let i = 0; i < flightTimes.length-1; i++){
      //compare INDIVIDUAL VALUES BECAUSE JS IS BAD
      if ((flightTimes[i][0] == key.depTime) && (flightTimes[i][1] == key.arrTime)){
        break;
      };
    };
    flightTimes.push(depArrTime);
    prices.push(key.price);
    queryTime.push(key.queryTime);
  });
  return {flightTimes, prices, queryTime};
};

getData("13/06/2023").then((rows) => {
  //do smth with rows: we are going to parse it in another function: might make a new module of that
  //console.log(parser(rows));
  console.log(parser(rows));
});