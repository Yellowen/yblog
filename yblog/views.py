from django.views.decorators.cache import cache_page
from django.shortcuts import render_to_response as rr
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings


def index(request):
    return rr("index.html",
              {},
              context_instance=RequestContext(request))


#@cache_page(60 * 60)
def socket(request):

    JS = """
    window.SOCKET = "http://%s:%s/";
    """ % (request.META["HTTP_HOST"].split(":")[0], settings.WEBSOCKET_PORT)

    return HttpResponse(JS,
                        mimetype="text/javascript")


def about_me(request):
    return rr("about_me.html",
              {},
              context_instance=RequestContext(request))

"""
    function setCookie(c_name,value,exdays)
    {
    var exdate=new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value=escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
    document.cookie=c_name + "=" + c_value;
    }
    function getCookie(c_name)
    {
    var i,x,y,ARRcookies=document.cookie.split(";");
    for (i=0;i<ARRcookies.length;i++)
    {
    x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
    y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
    x=x.replace(/^\s+|\s+$/g,"");
    if (x==c_name)
    {
    return unescape(y);
    }
    }
    }

    var a = getCookie('sid');
    console.log(">>> " + typeof a + " " +  a);
    if (a == 'undefined' || a === undefined) {
    var socket = io.connect(\"http://%s/\", {reconnecting: true});
    setCookie("sid", "123", 333);
    }
    else
    {
    console.log("<<< " + a);
    }
"""
