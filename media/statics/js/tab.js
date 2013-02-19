$(function(){
    var def_container = $("tab.select").attr("container");
    $("container").each(function(){
	if($(this).attr("id") != def_container){
	    $(this).hide();
	}
    });

    $("tab").click(function(){
	$('#' + def_container).fadeOut(300);
	$('#' + def_container).hide();
	mine_container = $(this).attr("container");
	$("#" + mine_container).delay(300).fadeIn();
	$("tab.select").removeClass("select");
	$(this).addClass("select");
	def_container = mine_container;
    });
});