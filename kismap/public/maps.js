var $_GET = {};
var poly;
var map;

document.location.search.replace(/\??(?:([^=]+)=([^&]*)&?)/g, function() {
    function decode(s) {
        return decodeURIComponent(s.split("+").join(" "));
    }

    $_GET[decode(arguments[1])] = decode(arguments[2]);
});

function initialize() {
    var mapOptions = {
        zoom: 15,
//        zoom: 12,
        center: new google.maps.LatLng($_GET["lat"], $_GET["long"]),
        //mapTypeId: google.maps.MapTypeId.HYBRID
        mapTypeId: google.maps.MapTypeId.TERRAIN
    };
    map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    var polyOptions = {
        strokeColor: '#000000',
        strokeOpacity: 1.0,
        strokeWeight: 3
    };
    poly = new google.maps.Polyline(polyOptions);
    poly.setMap(map);

}

function runlink(lat, long) {
    var path = poly.getPath();
    path.push(new google.maps.LatLng(lat, long));
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(lat, long),
        title: '#' + path.getLength() + ' ' + lat + ',' + long,
        map: map
    });
    map.setCenter(marker.getPosition());
}
google.maps.event.addDomListener(window, 'load', initialize);

window.onload = function() {
    var socket = io.connect('http://wpi:7000');
    socket.on('message', function(data) {
        if (data.message) {
            var msg = JSON.parse(data.message);
            console.log("New Msg: ", JSON.stringify(data.message));
            console.log("New Lat: ", msg.lat);
            console.log("New Long: ", msg.long);
            runlink(msg.lat, msg.long);
        } else {
            console.log("There is a problem:", JSON.stringify(data));
        }
    });
}
