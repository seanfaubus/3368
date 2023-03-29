// load the things we need
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');

// required module to make calls to a REST API
const axios = require('axios');
const {response} = require("express");

app.use(bodyParser.urlencoded());

// set the view engine to ejs
app.set('view engine', 'ejs');

// use res.render to load up an ejs view file

// index page 
app.get('/', function(req, res) {
    res.render("pages/index.ejs", {});
});

// planes page
app.get('/planes', function(req, res) {

    return axios.get("http://127.0.0.1:5000/api/planes")
        .then((response)=>{
            let planes = response.data

            res.render("pages/planes.ejs", {
            planes: planes
            });
        })
});

// ADD A PLANE
app.post('/process_form_add_plane', function (req,res){
    var plane = req.body;
    var add = "added a plane"
    console.log(plane)

    axios.post('http://127.0.0.1:5000/api/plane', plane)
        .then(function (response) {
            // console.log(response)
        })

    res.render('pages/welcome.ejs', {
                plane: plane,
                add: add
            });
})

// UPDATE A PLANE
app.post('/process_form_update_plane', function (req,res){
    var plane = req.body;
    var update = "updated a plane"
    console.log("xxxx"+plane)
    for (const x in plane) {
        if (plane[x] === '') {
            delete plane[x]
        }
    }

    axios.put('http://127.0.0.1:5000/api/plane',  plane)
        .then(function (response) {
             // console.log(response)
        })

    res.render('pages/welcome.ejs', {
                plane: plane,
                update: update
            });
})

// THIS IS TO DELETE PLANES ONLY
app.post('/process_form_DELETE_PLANE', function(req, res){
    var plane = req.body;
    console.log(`plane id to delete = ${plane}`)

    axios.delete('http://127.0.0.1:5000/api/plane', {data: plane})
        .then(function (response) {
            // console.log(response)
        })

    res.render('pages/welcome.ejs', {
                plane: plane
            });
  })


// airports page
app.get('/airports', function(req, res) {

    return axios.get("http://127.0.0.1:5000/api/airports")
        .then((response)=>{
            let airports = response.data

            res.render("pages/airports.ejs", {
            airports: airports
            });
        })
});

// ADD AN AIRPORT
app.post('/process_form_add_airport', function (req,res){
    var airport = req.body;
    var add = "added an airport"
    console.log(airport)

    axios.post('http://127.0.0.1:5000/api/airport', airport)
        .then(function (response) {
            // console.log(response)
        })

    res.render('pages/welcome.ejs', {
                airport: airport,
                add: add
            });
})


// UPDATE AN AIRPORT
app.post('/process_form_update_airport', function (req,res){
    var airport = req.body;
    var update = "updated an airport"
    console.log("xxxx"+airport)
    for (const x in airport) {
        if (airport[x] === '') {
            delete airport[x]
        }
    }

    axios.put('http://127.0.0.1:5000/api/airport',  airport)
        .then(function (response) {
             // console.log(response)
        })

    res.render('pages/welcome.ejs', {
                airport: airport,
                update: update
            });
})

// THIS IS TO DELETE AIRPORTS ONLY
app.post('/process_form_DELETE_AIRPORT', function(req, res){
    var airport = req.body;
    console.log(`airport id to delete = ${airport}`)

    axios.delete('http://127.0.0.1:5000/api/airport', {data: airport})
        .then(function (response) {
            // console.log(response)
        })

    res.render('pages/welcome.ejs', {
                airport: airport
            });
  })




// flights page
app.get('/flights', function(req, res) {
            let reqOne = axios.get("http://127.0.0.1:5000/api/flights")
            let reqTwo = axios.get("http://127.0.0.1:5000/api/airports")
            let reqThree = axios.get("http://127.0.0.1:5000/api/planes")

            return axios.all([reqOne, reqTwo, reqThree])
                .then(axios.spread(function (res1, res2, res3) {
                    // console.log(res1.data);
                    // console.log(res2.data);
                    // console.log(res3.data);
                    let flightsArray = res1.data;
                    let airportsArray = res2.data;
                    let planesArray = res3.data;
                    res.render('pages/flights.ejs', {
                        // plane: plane,
                        // user: user,
                        // response: response,
                        flightsArray: flightsArray,
                        airportsArray: airportsArray,
                        planesArray: planesArray,
                        auth: true
                    })
                }))
});


// THIS IS TO ADD FLIGHTS ONLY
app.post('/process_form_add_flight', function(req, res){
    var flight = req.body;
    console.log(flight)

    axios.post('http://127.0.0.1:5000/api/flight', flight)
        .then(function (response) {
            // console.log(response)
        })

    res.render('pages/welcome.ejs', {
                flight: flight
            });
  })

// THIS IS TO DELETE FLIGHTS ONLY
app.post('/process_form_DELETE_FLIGHT', function(req, res){
    var flight = req.body;
    console.log(`flight id to delete = ${flight}`)

    axios.delete('http://127.0.0.1:5000/api/flight', {data: flight})
        .then(function (response) {
            // console.log(response)
        })

    res.render('pages/welcome.ejs', {
                flight: flight
            });
  })

// axios.all

app.post('/process_login', function(req, res){
    var user = req.body.username;
    var password = req.body.password;

    if(user === 'admin' && password === 'password') {
            let reqOne = axios.get("http://127.0.0.1:5000/api/flights")
            let reqTwo = axios.get("http://127.0.0.1:5000/api/airports")
            let reqThree = axios.get("http://127.0.0.1:5000/api/planes")

            return axios.all([reqOne, reqTwo, reqThree])
                .then(axios.spread(function (res1, res2, res3) {
                    console.log(res1.data);
                    console.log(res2.data);
                    console.log(res3.data);
                    let flightsArray = res1.data;
                    let airportsArray = res2.data;
                    let planesArray = res3.data;
                    res.render('pages/flights.ejs', {
                        flightsArray: flightsArray,
                        airportsArray: airportsArray,
                        planesArray: planesArray,
                        auth: true
                    })
                }))
    }
    else
    {
        res.render('pages/index.ejs', {
            user: 'UNAUTHORIZED',
            auth: false
        });
    }
  })



app.listen(8080);
console.log('8080 is the magic port');
