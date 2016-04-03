Array.prototype.inArray = function(comparer) {
    for (var i = 0; i < this.length; i++) {
        if (comparer(this[i]))
            return true;
    }
    return false;
};

Array.prototype.pushIfNotExist = function(element, comparer) {
    if (!this.inArray(comparer)) {
        this.push(element);
    }
};

var ssids = [{ssid: "test", mac: "test"}]

window.onload = function() {
    $('#content').append('<div id="c1"></div>');
    $('#content').append('<div id="c2"></div>');
    $('#content').append('<div id="c3"></div>');
    $('#content').append('<div id="c4"></div>');

    $('#c1').html('c1');
    $('#c2').html('c2');
    $('#c3').html('c3');
    $('#c4').html('c4');

    $('#c4').empty();
    var ct = 0;
    var socket = io.connect('http://wpi:7000');
    socket.on('message', function(data) {
        if (data.message) {
            var msg = JSON.parse(data.message);
            var type = msg.handle_type;
            if (type === 'gps') {
                console.log("New Msg: ", JSON.stringify(data.message));
                console.log("New Lat: ", msg.lat);
                console.log("New Long: ", msg.lon);
                $('#c1').empty();
                $('#c1').html("Lat: " + msg.lat + " Long: " + msg.lon + "Alt: " + msg.alt + "Speed: " + msg.spd + "Head: " + msg.heading + "Fix: " + msg.fix);
                $('#c2').empty();
                $('#c2').html("New Lat: " + ct.toString());
            } else if (type === 'ssid') {
                console.log("New Msg: ", JSON.stringify(data.message));
                console.log("New SSID: ", msg.ssid);
                var ssid = new Object;
                ssid.ssid = msg.ssid;
                ssid.mac = msg.mac;
                ssids.pushIfNotExist(ssid, function(e) {
                    return e.ssid === ssid.ssid && e.mac === ssid.mac;
                });

                
                var oh = '';
                $.each(ssids, function(key, value) {
                    oh += value.ssid + " MAC: " + value.mac + "<br>\n";
                });
                $('#c4').empty();
                $('#c4').html(oh);
                $('#c3').empty();
                $('#c3').html('SSID CT: ' + ssids.length.toString());


            } else {
                console.log('new message ', JSON.stringify(data.message));
            }

        } else {
            console.log("There is a problem:", JSON.stringify(data));
        }
        ct++;
    });
};

