var G = 9.8;

// Character Weight  k
var CW = 1
// wind speed km/h
var WIND = 159;

var SW = window.screen.availWidth
var SH = window.screen.availHeight
// we used WIND speed to calculate a duration
var SPEED = WIND * 1000 / 3600;

function weight(element){
    var len = element.text().length || 1;
    return len * CW;
}

// Setup the Y axis of each cloud
function set_y(element){
    var w = (weight(element)/CW);
    w = w * 100 * 7  / SH;
    console.log(w);
    console.log(w  >= SH - 50);

    if (w >= 90) {
	w = 90;
    }

    element.css('top', w.toString() + "%"); 
}

// Setup the X axis
function set_x(element, direction){
    var rand = Math.floor(Math.random()* (SW / 2));
    if (direction == 1) {
	rand = rand + (SW / 2) - element.width();
    }
    element.css('left', rand);
}

$(function(){

    // Setting up the socket event handlers
    socket.on('connect', function (cc) {
	console.dir(cc);
	console.log("connected");
	socket.on('message', function (msg) {
	    console.log(msg);
	});
    });

    // Setup the cloud actions
    $('cloud').each(function(){
	set_y($(this));
	var random = Math.floor(Math.random()*2);
	$(this).attr("direction", random);
	var anim_speed = (SW * 1000 / SPEED) * (G * weight($(this)) / 10);

	var x = (SW - $(this).width() - 20);
	if (random == 1){
	    x = 0;
	}

	set_x($(this), random);
//	console.log($("cloud").css('padding'));
	$(this).animate({'left': x }, anim_speed , 'linear');
    });
    
});


function aa(){
    console.log(typeof socket.disconnect);
    socket.disconnect();
    console.log("closed");
};
window.onUnload  = aa();
window.onBeforeupdate = aa();
