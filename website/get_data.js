import sqlite3 from 'sqlite3';

function getData(date) {
  return new Promise((resolve, reject) => {
    const db = new sqlite3.Database('/Users/sam/Desktop/projects/dailyBot/db_folder/flights.db', sqlite3.OPEN_READONLY, (err) => {
      if (err) {
        reject(err);
      } else {
        //console.log('Connected to the SQlite database.');
      }
    });

    const sql = `SELECT * FROM flights WHERE flightDate = ?;`;

    db.all(sql, [date], (err, rows) => {
      if (err) {
        reject(err);
      } else {
        resolve(rows);
      }
    });

    db.close((err) => {
      if (err) {
        console.error(err.message);
      } else {
        //console.log('Close the database connection.');
      }
    });
  });
};

//function takes in json data in the form of an object and returns preferred values and format

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

export {getData, parser};
/*
let date = ["10/06/2023", "12/06/2023", "13/06/2023", "14/06/2023", "15/06/2023", "16/06/2023", "17/06/2023", "18/06/2023", "19/06/2023", "20/06/2023", "21/06/2023", "22/06/2023", "23/06/2023", "24/06/2023"]
date.forEach((key) => {
  getData(key).then((data) => {
   console.log(parser(data));
  });
});
*/