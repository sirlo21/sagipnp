function mostrar(){
	$.post("mostrar.php", function(data){ 
		$("#contenido").html(data) 
	});
}

$(document).ready(function(){
	mostrar();
});

 

  