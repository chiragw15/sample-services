require('dotenv').config();
const express = require('express');
const mysql = require('mysql');
const redis = require('redis');

const app = express();

// MySQL Configuration
const db = mysql.createConnection({
  host: process.env.MYSQL_DATABASE_HOST,
  user: process.env.MYSQL_DATABASE_USER,
  password: process.env.MYSQL_DATABASE_PASSWORD,
  database: process.env.MYSQL_DATABASE_DB
});

db.connect((err) => {
  if(err) throw err;
  console.log('MySQL Connected...');
});

// Redis Configuration
const client = redis.createClient(process.env.REDIS_URL);

client.on("error", function(error) {
  console.error('Redis error: ', error);
});

app.get('/ping', (req, res) => {
  db.query('SELECT 1', (err, result) => {
    if(err) {
      res.status(500).json({mysql: 'unavailable'});
      return;
    }

    client.ping((err, result) => {
      if(err || result !== 'PONG') {
        res.status(500).json({redis: 'unavailable'});
      } else {
        res.status(200).json({status: 'success'});
      }
    });
  });
});

app.listen(5000, () => {
  console.log('Server started on port 5000');
});
