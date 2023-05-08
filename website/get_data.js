import sqlite3 from 'sqlite3';

export default function getData(date) {
  return new Promise((resolve, reject) => {
    const db = new sqlite3.Database('/Users/sam/Desktop/projects/dailyBot/db_folder/flights.db', sqlite3.OPEN_READONLY, (err) => {
      if (err) {
        reject(err);
      } else {
        console.log('Connected to the SQlite database.');
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
        console.log('Close the database connection.');
      }
    });
  });
}
