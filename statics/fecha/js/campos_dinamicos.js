// JavaScript Document
subpreguntas=0;
function agregar() {
	subpreguntas++;
	$("#campos").append('<p class="subpreguntas'+subpreguntas+'">'+subpreguntas+'.-&nbsp;<input type="text" name="opc[]" size="35" />&nbsp;&nbsp;<a href="#" onclick="javascript:borrar('+subpreguntas+');">Borrar</a></p>');
}

function borrar(cual) {
	subpreguntas--;
	$("p.subpreguntas"+cual).remove();
	return false;
}

respuestas=0;
function agregarrptas() {
	respuestas++;
	$("#campos2").append('<p class="respuestas'+respuestas+'">'+respuestas+'.-&nbsp;<input type="text" name="rpta[]" size="35" />&nbsp;&nbsp;<a href="#" onclick="javascript:borrarrptas('+respuestas+');">Borrar</a></p>');
}
function borrarrptas(cual) {
	respuestas--;
	$("p.respuestas"+cual).remove();
	return false;
}

$(function(){
$(".search").keyup(function() 
{ 
var searchid = $(this).val();
var dataString = 'search='+ searchid;
if(searchid!='')
{
	$.ajax({
	type: "POST",
	url: "search_codigo.php",
	data: dataString,
	cache: false,
	success: function(html)
	{
	$("#result").html(html).show();
	}
	});
}return false;    
});

jQuery("#result").live("click",function(e){ 
	var $clicked = $(e.target);
	var $name = $clicked.find('.name').html();
	var decoded = $("<div/>").html($name).text();
	$('#searchid').val(decoded);
});

jQuery(document).live("click", function(e) { 
	var $clicked = $(e.target);
	if (! $clicked.hasClass("search")){
	jQuery("#result").fadeOut(); 
	}
});
$('#searchid').click(function(){
	jQuery("#result").fadeIn();
});
});

/////////////

$(function(){
$(".search2").keyup(function() 
{ 
var searchid2 = $(this).val();
var dataString = 'search2='+ searchid2;
if(searchid2!='')
{
	$.ajax({
	type: "POST",
	url: "search.php",
	data: dataString,
	cache: false,
	success: function(html)
	{
	$("#result2").html(html).show();
	}
	});
}return false;    
});


jQuery("#result2").live("click",function(e){ 
	var $clicked = $(e.target);
	var $name = $clicked.find('.name2').html();
	var decoded = $("<div/>").html($name).text();
	$('#searchid2').val(decoded);
});

jQuery(document).live("click", function(e) { 
	var $clicked = $(e.target);
	if (! $clicked.hasClass("search2")){
	jQuery("#result2").fadeOut(); 
	}
});
$('#searchid2').click(function(){
	jQuery("#result2").fadeIn();
});

});
