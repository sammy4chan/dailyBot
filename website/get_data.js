const sqlite3 = require('sqlite3').verbose();

// open database in memory
let db = new sqlite3.Database('/Users/sam/Desktop/projects/dailyBot/db_folder/flights.db', sqlite3.OPEN_READONLY, (err) => {
  if (err) {
    return console.error(err.message);
  }
  console.log('Connected to the in-memory SQlite database.');
});

let sql = `SELECT * FROM flights`;

db.all(sql, [], (err, rows) => {
  if (err) {
    throw err;
  }
  //console.log(rows); or
  rows.forEach((row) => {
    console.log(row);
  });
});

// close the database connection
db.close((err) => {
  if (err) {
    return console.error(err.message);
  }
  console.log('Close the database connection.');
});