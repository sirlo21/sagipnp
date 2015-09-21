// JavaScript Document
//buscador de la pregunta
$(function(){
$(".search").keyup(function() 
{ 
var searchid = $(this).val();
var dataString = 'search='+ searchid;
if(searchid!='')
{
	$.ajax({
	type: "POST",
	url: "libs/search.php",
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

///////////// buscador del codigo
$(function(){
$(".search2").keyup(function() 
{ 
var searchid2 = $(this).val();
var dataString = 'search2='+ searchid2;
if(searchid2!='')
{
	$.ajax({
	type: "POST",
	url: "libs/search2.php",
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

$(document).ready(function() {
	$('#esperar_1').hide();
	$('#anio').change(function(){
	  $('#esperar_1').show();
	  $('#result_1').hide();
      $.get("libs/func.php", {
		func: "anio",
		anio_var: $('#anio').val()
      }, function(response){
        $('#result_1').fadeOut();
        setTimeout("finishAjax('result_1', '"+escape(response)+"')", 400);
      });
    	return false;
	});
});

function finishAjax(id, response) {
  $('#esperar_1').hide();
  $('#'+id).html(unescape(response));
  $('#'+id).fadeIn();
}

///////////////// ocultar columnas en una tabla
function OcultarColumnaTema(numeroColumna) {               
                var form = document.form;
                fila = document.getElementById('tabla').getElementsByTagName('tr');
                
				ultimaColumna=fila.length
for(var i=0;i<ultimaColumna;i++)
	
				
				if(form.ck.checked == true) {     
				
                  fila[i].getElementsByTagName('td')[numeroColumna].style.display='';  
                } else {                  
				fila[i].getElementsByTagName('td')[numeroColumna].style.display="none";

                }         
            }
			function OcultarColumnaEstudio(numeroColumna) {               
                var form = document.form;
                fila = document.getElementById('tabla').getElementsByTagName('tr');
                
				ultimaColumna=fila.length
for(var i=0;i<ultimaColumna;i++)
	
				
				if(form.ck1.checked == true) {     
				fila[i].getElementsByTagName('td')[numeroColumna].style.display='';
                    
                } else {                  
				
				fila[i].getElementsByTagName('td')[numeroColumna].style.display="none";
                }         
            }
			function OcultarColumnaAnio(numeroColumna) {               
                var form = document.form;
                fila = document.getElementById('tabla').getElementsByTagName('tr');
                
				ultimaColumna=fila.length
for(var i=0;i<ultimaColumna;i++)
	
				
				if(form.ck2.checked == true) {     
				fila[i].getElementsByTagName('td')[numeroColumna].style.display='';
                    
                } else {                  
				
				fila[i].getElementsByTagName('td')[numeroColumna].style.display="none";
                }         
            }
			function OcultarColumnaAplicado(numeroColumna) {               
                var form = document.form;
                fila = document.getElementById('tabla').getElementsByTagName('tr');
                
				ultimaColumna=fila.length
for(var i=0;i<ultimaColumna;i++)
	
				
				if(form.ck3.checked == true) {     
				fila[i].getElementsByTagName('td')[numeroColumna].style.display='';
                    
                } else {                  
				
				fila[i].getElementsByTagName('td')[numeroColumna].style.display="none";
                }         
            }

	
	//popup de las preguntas que ha seleccionado
	function popup(url,ancho,alto) {
		var posicion_x; 
		var posicion_y; 
		posicion_x=(screen.width/2)-(ancho/2); 
		posicion_y=(screen.height/2)-(alto/2); 
		window.open(url, "leonpurpura.com", "width="+ancho+",height="+alto+",menubar=0,toolbar=0,directories=0,scrollbars=no,resizable=no,left="+posicion_x+",top="+posicion_y+"");
}

//} recargar paginacion

$(document).ready(function() {	
	$('.paginate').live('click', function(){
		
		$('#contenido').html('<div class="loading"><img src="images/loading.gif" width="70px" height="70px"/></div>');

		var page = $(this).attr('data');		
		var dataString = 'page='+page;
		
		$.ajax({
            type: "GET",
            url: "pagination.php",
            data: dataString,
            success: function(data) {
				$('#contenido').fadeIn(1000).html(data);
            }
        });
    });              
}); 

