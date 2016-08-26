const GAUGE_SIZE = 500;
const API_SCALE = 110;
const API_VERSITON = 'v1_1';
const MY_URL = window.location.href;

function GetGrumpinessID(myUrl, apiVersion, callback) {
    var client = new XMLHttpRequest();
    client.open("GET", myUrl + 'api/' + apiVersion + '/grumpyID/', true);
    client.responseType = 'json';
    client.onload = function() {
        if (client.status == 200) {
            callback(null, client.response);
        } else {
            callback(client.status);
        }
    };
    client.send();
}

function getStoredUID() {
    var UUID = null;
    if (localStorage.getItem('grantometerUID')) 
    {
        UUID = localStorage.getItem('grantometerUID');
    } 
    else {
        GetGrumpinessID(MY_URL, API_VERSITON,
            function(err, data) {
                if (err != null) {
                    alert('Something went wrong: ' + err);
                } else {
                    console.log(data.guid);
                    localStorage.setItem('grantometerUID', data.guid);
                }
             });
    }
    return UUID;
}

function GetGrumpiness(myUrl, apiVersion, callback) {
    var client = new XMLHttpRequest();
    client.open("GET", myUrl + 'api/' + apiVersion + '/grumpy/', true);
    client.responseType = 'json';
    client.onload = function() {
        if (client.status == 200) {
            callback(null, client.response);
        } else {
            callback(client.status);
        }
    };
    client.send();
}

function PostGrumpiness(myUrl, apiVersion, callback, action) {
    var client = new XMLHttpRequest();
    client.open("POST", myUrl +  'api/' + apiVersion + '/grumpy/', true);
    client.responseType = 'json';
    client.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    client.onload = function() {
        if (client.status == 200) {
            callback(null, client.response);
        } else { 
            callback(client.status);
        }
    };
    client.send(JSON.stringify({"action" : action, "guid" : getStoredUID()}));
}

function drawGrantOMeter(grumpy) {
    var scale = GAUGE_SIZE / API_SCALE;
    ctx.clearRect(0, 0, 120, GAUGE_SIZE);
    ctx.fillRect(0, GAUGE_SIZE - (grumpy * scale), 120, GAUGE_SIZE);
}

function increasGrantigkeit() {
    PostGrumpiness(MY_URL, API_VERSITON, function(err, data){
        if (err != null) {
            alert('Something went wrong ' + err);
            drawGrantOMeter(60);
        } else {
            drawGrantOMeter(data.grumpiness);
        }
    }, 'increase');
}

function decreaseGrantigkeit() {
    PostGrumpiness(MY_URL, API_VERSITON, function(err, data){
        if (err != null) {
            alert('Something went wrong ' + err);
            drawGrantOMeter(60);
        } else {
            drawGrantOMeter(data.grumpiness);
        }
    }, 'decrease');
}

var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
// Create gradient
var grd = ctx.createLinearGradient(0, 1.2 * GAUGE_SIZE, 0, 0);
grd.addColorStop(0,"green");
grd.addColorStop(0.1,"yellow");
grd.addColorStop(1,"red");

ctx.fillStyle = 'white';
// Fill with gradient
//ctx.fillStyle = grd;
ctx.lineWidth = 4;
ctx.strokeStyle = 'black';


function refreshGrantometer() {
    GetGrumpiness(MY_URL, API_VERSITON,
        function(err, data) {
            if (err != null) {
                alert('Something went wrong: ' + err);
                drawGrantOMeter(0);
            } else {
                drawGrantOMeter(data.grumpiness);
            }
         });
    setTimeout(refreshGrantometer, 20000);
}

drawGrantOMeter(110);
//refreshGrantometer();
console.log(getStoredUID());
