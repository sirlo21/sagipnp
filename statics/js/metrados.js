$(document).ready(function(){
	$("#id_metrado1").change(function(ev){
		var url = "/metrado/?metrado1_id="+$(this).val();
		$.getJSON(url,function(data){
			$("#id_metrado2").children("option[value]").remove();
			$("#id_metrado3").children("option[value]").remove();
			$("#id_metrado4").children("option[value]").remove();
			var metrado2 = data["metrado2"];
			for(var i=0;i<metrado2.length;i++){
				var id = metrado2[i]["id"];
				var name = metrado2[i]["name"]
				var option = "<option value='"+id+"'>"+name+"</option>"
				$("#id_metrado2").append(option);
			}
		});
	});
	$("#id_metrado2").change(function(ev){
		var url = "/metrado/?metrado2_id="+$(this).val();
		$.getJSON(url,function(data){
			$("#id_metrado3").children("option[value]").remove();
			$("#id_metrado4").children("option[value]").remove();
			var metrado3 = data["metrado3"];
			for(var i=0;i<metrado3.length;i++){
				var id = metrado3[i]["id"];
				var name = metrado3[i]["name"]
				var option = "<option value='"+id+"'>"+name+"</option>"
				$("#id_metrado3").append(option);
			}
		});
	});
	$("#id_metrado3").change(function(ev){
		var url = "/metrado/?metrado3_id="+$(this).val();
		$.getJSON(url,function(data){
			$("#id_metrado4").children("option[value]").remove();
			var metrado4 = data["metrado4"];
			for(var i=0;i<metrado4.length;i++){
				var id = metrado4[i]["id"];
				var name = metrado4[i]["name"]
				var option = "<option value='"+id+"'>"+name+"</option>"
				$("#id_metrado4").append(option);
			}
		});
	});
	$("#agregar").click(function(ev){
		$("#id_metrado4").children().each(function(index){
			if($(this).prop("selected"))
				$(".td-partida").text($(this).text());
		});
		$(".td-numero-veces").text($("#id_numero").val());
		$(".td-dimensiones-largo").text("Hola ponys!");
		$(".td-dimensiones-ancho").text("Hola ponys!");
		$(".td-dimensiones-altura").text("Hola ponys!");
		$(".td-parcial").text("Hola ponys!");
		$(".td-total").text("Hola ponys!");
		$(".td-unidad").text("Hola ponys!");
		$(".td-precio-unitario").text("Hola ponys!");
		$(".td-precio-total").text("Hola ponys!");
	});
	$(".td-borrar").click(function(ev){
		$(".td-partida").text("");
		$(".td-numero-veces").text("");
		$(".td-dimensiones-largo").text("");
		$(".td-dimensiones-ancho").text("");
		$(".td-dimensiones-altura").text("");
		$(".td-parcial").text("");
		$(".td-total").text("");
		$(".td-unidad").text("");
		$(".td-precio-unitario").text("");
		$(".td-precio-total").text("");
	});
	$("#ficha-tecnica-form").submit(function(ev){
		return ev.preventDefault();
	});
});