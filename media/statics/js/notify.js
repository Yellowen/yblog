function notify(msg, klass) {
    klass = typeof(klass) != 'undefined' ? klass : 'notify';
    var r = Math.floor(Math.random()*1000000)
    var notify = $('notify');
    notify.addClass(klass);
    notify.html(msg);
    notify.fadeIn(800).delay(5000).fadeOut(800);
}

$(function(){
    $('notify').hide();
    var interval = $('notificationarea').attr('interval') || 30000;
    setInterval(function(){
	var url = $('notificationarea').attr('tips');
	if (url != undefined){
	    $.ajax({url: url,
		    method: "GET",
		    success: function (tip, a, b){
			if (tip != "") {
			    notify(tip);
			}
			
		    }
		   });
	}
    }, interval);
    $('notify').live("click", function(){$(this).fadeOut('slow');});
});