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
		var val_numero = $("#id_numero").val();
		var val_parcial = $("#id_parcial").val();
		var total = val_numero*val_parcial;
		var val_unidad = $("#id_unidad").val();
		var val_punitario = $("#id_punitario").val();
		var precio_total = val_unidad*val_punitario;
		if($("#id_metrado4").children().length > 1){
			$("#id_metrado4").children().each(function(index){
				if($(this).prop("selected"))
					$(".td-partida").text($(this).text());
			});
		}
		else if($("#id_metrado3").children().length > 1){
			$("#id_metrado3").children().each(function(index){
				if($(this).prop("selected"))
					$(".td-partida").text($(this).text());
			});
		}
		else{
			$("#id_metrado2").children().each(function(index){
				if($(this).prop("selected"))
					$(".td-partida").text($(this).text());
			});
		}
		$(".td-numero-veces").text(val_numero);
		$(".td-dimensiones-largo").text($("#id_largo").val());
		$(".td-dimensiones-ancho").text($("#id_ancho").val());
		$(".td-dimensiones-altura").text($("#id_alto").val());
		$(".td-parcial").text(val_parcial);
		$(".td-total").text(total);
		$(".td-unidad").text(val_unidad);
		$(".td-precio-unitario").text(val_punitario);
		$(".td-precio-total").text(precio_total);
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