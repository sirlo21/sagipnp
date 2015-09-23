$(document).ready(function(){
	$("#submit").hide();
	$("#id_metrado1").change(function(ev){
		var url = "/metrado/?metrado1_id="+$(this).val();
		$.getJSON(url,function(data){
			$("#id_metrado2").children("option[value]").remove();
			$("#id_metrado3").children("option[value]").remove();
			$("#id_metrado4").children("option[value]").remove();
			var metrado2 = data["metrado2"];
			for(var i=0;i<metrado2.length;i++){
				var id = metrado2[i]["id"];
				var descripcion = metrado2[i]["descripcion"]
				var option = "<option value='"+id+"'>"+descripcion+"</option>"
				$("#id_metrado2").append(option);
				codigo_metrado2 = metrado2[i]["codigo"];
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
				var descripcion = metrado3[i]["descripcion"]
				var option = "<option value='"+id+"'>"+descripcion+"</option>"
				$("#id_metrado3").append(option);
				codigo_metrado3 = metrado3[i]["codigo"];
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
				var descripcion = metrado4[i]["descripcion"]
				var option = "<option value='"+id+"'>"+descripcion+"</option>"
				$("#id_metrado4").append(option);
				codigo_metrado4 = metrado4[i]["codigo"];
			}
		});
	});
	$("#agregar").click(function(ev){
		$("#submit").show();
		var val_numero = $("#id_numero").val();
		var val_parcial = $("#id_parcial").val();
		var total = val_numero*val_parcial;
		var val_unidad = $("#id_unidad").val();
		var val_punitario = $("#id_punitario").val();
		var precio_total = val_unidad*val_punitario;
		if($("#id_metrado4").children().length > 1){
			$("#id_metrado4").children().each(function(index){
				if($(this).prop("selected"))
					$(".td-partida").text(codigo_metrado2);
			});
		}
		else if($("#id_metrado3").children().length > 1){
			$("#id_metrado3").children().each(function(index){
				if($(this).prop("selected"))
					$(".td-partida").text(codigo_metrado3);
			});
		}
		else{
			$("#id_metrado2").children().each(function(index){
				if($(this).prop("selected"))
					$(".td-partida").text(codigo_metrado4);
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
		$("#submit").hide();
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
	// $("#ficha-tecnica-form").submit(function(ev){
	// 	return ev.preventDefault();
	// });
});