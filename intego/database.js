const mysql = require("mysql");

const conn = mysql.createConnection({
  host: "localhost",
  user: "admin",
  password: "NS8kXhbC$f64Di9o",
  database: "users",
});

conn.connect(function (err) {
  if (err) throw err;
  console.log("Database is connected successfully !");
});

module.exports = conn;
