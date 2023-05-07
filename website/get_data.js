import sqlite3 from 'sqlite3';

function arrayEquals(a, b) {
  return Array.isArray(a) &&
      Array.isArray(b) &&
      a.length === b.length &&
      a.every((val, index) => val === b[index]);
}

export default function getData(date){

  let db = new sqlite3.Database('/Users/sam/Desktop/projects/dailyBot/db_folder/flights.db', sqlite3.OPEN_READONLY, (err) => {
    if (err) {
      return console.error(err.message);
    }
    console.log('Connected to the in-memory SQlite database.');
  });
  
  let sql = `SELECT * FROM flights WHERE flightDate =?;`;

  var flightTimes = [];
  var prices = [];
  var queryTime = [];
  db.all(sql, [date], (err, rows) => {
    if (err) {
      throw err;
    };
    //iterate through every row
    rows.forEach((row) => {
      let depArrTime = [row.depTime, row.arrTime];
      //console.log(depArrTime);
      if (flightTimes.length <= 0){
        flightTimes.push(depArrTime);
      };
      for (let i = 0; i < flightTimes.length-1; i++){
        //compare INDIVIDUAL VALUES BECAUSE JS IS BAD
        if ((flightTimes[i][0] == depArrTime[0]) && (flightTimes[i][1] == depArrTime[1])){
          return;
        };
      };
      flightTimes.push(depArrTime);
    });
    console.log(flightTimes);
  });
  // close the database connection
  db.close((err) => {
    if (err) {
      return console.error(err.message);
    }
    console.log('Close the database connection.');
  });
};