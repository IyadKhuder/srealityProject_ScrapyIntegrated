const express = require('express');
const { Pool } = require('pg');

const HOST = '0.0.0.0';
const PORT = 80;
const app = express();

// # In the next, user is the db user;
// # host is the name of the database container
const pool = new Pool({ user: 'postgres', host: 'aptsdb13'})
// # Thanks for the DNS resultion that the docker has,
// # we use the container's name of the database aptsdb13,
// # no need for the IP address

app.get('/', (req, res) => {
    pool.query('SELECT * FROM aptads', (error, response) =>{
        res.json(response.rows)
    });
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);