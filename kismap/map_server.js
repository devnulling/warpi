var express = require("express");
var app = express();
var port = 7000;
var fs = require("fs");
var redis = require("redis");

var http = require('http');
http.createServer(function(req, res) {
});

app.set('views', __dirname + '/tpl');
app.set('view engine', "jade");
app.engine('jade', require('jade').__express);

app.get("/", function(req, res) {
    res.render("maps");
});

app.get("/data", function(req, res) {
    res.render("data");
});

app.get("/post", function(req, res) {
    publishMsg('the_channel', req.param("lat"), req.param("long"));
    res.send(200);
});

app.post("/check", function(req, res) {
   res.json({ data: 'OK' });
});

app.get("/check", function(req, res) {
  res.json({ data: 'OK' });
});

app.use(express.static(__dirname + '/public'));
var io = require('socket.io').listen(app.listen(port));
io.sockets.on('connection', function(socket) {
    socket.on('send', function(data) {
        io.sockets.emit('message', data);
    });
});

console.log("Listening on port " + port);

var clientSusbcribe = redis.createClient();
clientSusbcribe.subscribe("the_channel");
clientSusbcribe.on("message", function(channel, message) {
    console.log("client channel recieve from channel : %s, the message : %s", channel, message);
    io.sockets.emit('message', {message: message});
});

function publishMsg(channel, lat, long) {
    var redisClient = redis.createClient();
    message = new Object;
    message.lat = lat;
    message.long = long;
    redisClient.publish(channel,  JSON.stringify(message));
}