$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
$(function(){
    $("menu").prev().css("opacity", 0);
    $(".hiddeninfo").hide();
    $("menu section").hide();
    $("msg").hide();
    //$('.comments').hide();

    // Show post details when mouse moved to article tag
    $("article").hover(function(){
	$(this).find(".hiddeninfo").fadeIn(300);
    },
    function(){
	$(this).find(".hiddeninfo").hide();
    });

    $("menu").hover(function(){
	$(this).prev().css("opacity", 1);
    }, function(){
	$(this).prev().css("opacity", 0);
    });

    // display comment dialog
    $('#microblog').on('click', '.micro span.text', function(){
	setTimeout(function(){$('#commentform').fadeOut('slow');}, 60000);
	$(".wait").css("display", "none");
	var pk = $(this).parent().find('.data input[name="object_pk"]').attr("value");
	var ts = $(this).parent().find('.data input[name="timestamp"]').attr("value");
	var sh = $(this).parent().find('.data input[name="security_hash"]').attr("value");
	//var csrf = $(this).parent().find('input[name="csrfmiddlewaretoken"]').attr("value");
	$('#commentform input[name="object_pk"]').attr("value", pk);
	//$('#commentform input[name="csrfmiddlewaretoken"]').attr("value", pk);
	$('#commentform input[name="timestamp"]').attr("value", ts);
	$('#commentform input[name="security_hash"]').attr("value", sh);
	$('#commentform').fadeOut();
	$('#commentform').fadeIn('slow');
    });
    $('#microblog').on('click', '.cancel', function(){
	$("#commentform").fadeOut('slow');
	$('#commentform input[name="name"]').val("");
	$('#commentform textarea').val("");

    });

    // post button
    $('#microblog').on('click', '.post', function() {
	var str = $(this).parent().serializeArray();
	var self = this;
	$(".wait").fadeIn();
	$.ajax({url: "/comments/post/",
		type: "POST",
		data: str,
		success: function(data, status, xhr){
		    notify("Your comment sent. Thanks buddy.", "success");
		    $("#commentform").fadeOut('slow');
		    $('#commentform input[name="name"]').val("");
		    $('#commentform textarea').val("");
		},
	       });
	return true;
    }); 

    // time display animation
    $("time").hover(function(){
	var width = 0;
	if (! ($(this).attr("slidewidth"))) {
	    width = $(this).find("timestring").width();
	    $(this).attr('slidewidth', width);
	}
	else {
	    width = $(this).attr('slidewidth');
	}

	if ((! $(this).attr('over') || ($(this).attr('over') == 'false'))) {
	    $(this).animate({left: '-=' + width,
			     width: '+='+ width
			    },
			    200,
			    'linear',
			    function(){
				$(this).find("timestring").fadeIn();
			    });
	}
	$(this).attr('over', true);
    }, function(){
	$(this).find("timestring").fadeOut();
	$(this).animate({right: '0',
			 width: '0',
			},
			300,
			'swing',
			function(){
			    $(this).attr('over', false);
			});
    });
    
    
    // Menu section 
    $("menu item").click(function(){
	var h = $(this).next().height()
	$(this).next().children().hide();
	$(this).next().css("height", h);
	$(this).next().slideToggle(400);
	$(this).next().find("ul:first").delay(450).fadeToggle();
    });
    
    $("menu item").hover(function(){
	$("menu section ul").fadeOut();
	$("menu section").slideUp();
    }, function(){});

    $("menu section").hover(function(){}, function(){
	$(this).slideToggle('normal', 'linear', function(){});
    });

    // Setting up the socket event handlers
    window.socket.on('connect', function (cc) {

	socket.on('new_comment', function (data) {
	    var comment = $.parseJSON(data);
	    if (comment.model == "MicroPost") {
		var micro = $('#micro_' + comment.object_id);
		var last_comment = $("#commentshell").clone(true, true);
		$(last_comment).attr("id", "");
		$(last_comment).addClass("comment");
		var mh = $(micro).height();
		$(last_comment).hide();
		$(last_comment).find(".commentcontent").html(comment.content);
		$(last_comment).find("b").html(comment.user);
		$(last_comment).find(".logtime").html(comment.date);
		$(micro).find(".comments").append(last_comment);
		var ch = $(micro).find(".comments .comment:last-child").height();
		$(micro).height(ch + mh);
		if ($(micro).find(".comments").is(":visible")){
		    $(last_comment).fadeIn(2000);
		}
		else {
		    $(last_comment).hide();
		}
		var cc = parseInt($(micro).find(".commentcount b").text()) + 1;
		$(micro).find(".commentcount b").html(cc);
	    }
	});
	
	socket.on("new_log", function(data){
	    var node = $.parseJSON(data);
	    $("#microblog").prepend(node.html);
	    $(node.id).hide();
	    $(node.id).fadeIn(600);
	    setup_microblog_js();
 	    
	});
    });



});
