$(document).ready(function(){
	function addOptions(id_metrado,args){
		if(args.length > 0){
			var codigos = [];
			$(id_metrado).append("<option value selected='selected'>---------</option>");
			for(i in args){
				var id = args[i]["id"];
				var descripcion = args[i]["descripcion"];
				var option = "<option value='"+id+"'>"+descripcion+"</option>";
				$(id_metrado).append(option);
				codigos.push({id: args[i]["codigo"]});
			}
			return codigos;
		}
	}
	function addToTable(id_input,replace_text,id_td,val_input){
		var id_tabla = "#"+id_input.replace(replace_text,"tabla");
		$(id_tabla+" "+id_td).text(val_input);
	}
	$("select").change(function(ev){
		$(this).each(function(index){
			var id_select = $(this).attr("id");
			var value_select = $(this).val();
			if(id_select.endsWith("metrado1")){
				var url = "/metrado/?metrado1_id="+value_select;
				$.getJSON(url,function(data){
					var id_metrado2 = "#"+id_select.replace("metrado1","metrado2");
					var id_metrado3 = "#"+id_select.replace("metrado1","metrado3");
					var id_metrado4 = "#"+id_select.replace("metrado1","metrado4");
					$(id_metrado2).children().remove();
					$(id_metrado3).children().remove();
					$(id_metrado4).children().remove();
					addOptions(id_metrado2,data["metrado2"]);
				});
			}
			else if(id_select.endsWith("metrado2")){
				var url = "/metrado/?metrado2_id="+value_select;
				$.getJSON(url,function(data){
					var id_metrado3 = "#"+id_select.replace("metrado2","metrado3");
					var id_metrado4 = "#"+id_select.replace("metrado2","metrado4");
					$(id_metrado3).children().remove();
					$(id_metrado4).children().remove();
					addOptions(id_metrado3,data["metrado3"]);
				});
			}
			else if(id_select.endsWith("metrado3")){
				var url = "/metrado/?metrado3_id="+value_select;
				$.getJSON(url,function(data){
					var id_metrado4 = "#"+id_select.replace("metrado3","metrado4");
					$(id_metrado4).children().remove();
					addOptions(id_metrado4,data["metrado4"]);
				});
			}
		});
	});
	var val_numero,val_parcial,val_unidad,val_punitario;
	$("input").change(function(ev){
		var id_input = $(this).attr("id");
		var val_input = $(this).val();
		if(id_input.endsWith("numero")){
			// var id_tabla = "#"+id_input.replace("numero","tabla");
			val_numero = val_input;
			// $(id_tabla+" #td-numero-veces").text(val_input);
			addToTable(id_input,"numero","#td-numero-veces",val_input);
		}
		else if(id_input.endsWith("largo")){
			var id_tabla = "#"+id_input.replace("largo","tabla");
			$(id_tabla+" #td-dimensiones-largo").text(val_input);
		}
		else if(id_input.endsWith("ancho")){
			var id_tabla = "#"+id_input.replace("ancho","tabla");
			$(id_tabla+" #td-dimensiones-ancho").text(val_input);
		}
		else if(id_input.endsWith("alto")){
			var id_tabla = "#"+id_input.replace("alto","tabla");
			$(id_tabla+" #td-dimensiones-altura").text(val_input);
		}
		else if(id_input.endsWith("parcial")){
			var id_tabla = "#"+id_input.replace("parcial","tabla");
			val_parcial = val_input;
			$(id_tabla+" #td-parcial").text(val_input);
		}
		else if(id_input.endsWith("unidad")){
			var id_tabla = "#"+id_input.replace("unidad","tabla");
			val_unidad = val_input;
			$(id_tabla+" #td-unidad").text(val_input);
		}
		else if(id_input.endsWith("punitario")){
			var id_tabla = "#"+id_input.replace("punitario","tabla");
			val_punitario = val_input;
			$(id_tabla+" #td-precio-unitario").text(val_input);
		}
		
		if(val_numero && val_parcial){
			var total = val_numero*val_parcial;
			$(id_tabla+" #td-total").text(total);
		}
		if(val_unidad && val_punitario){
			var precio_total = val_unidad*val_punitario;
			$(id_tabla+" #td-precio-total").text(precio_total);
		}		
		// if($("#id_metrado4").children().length > 1){
		// 	$("#id_metrado4").children().each(function(index){
		// 		if($(this).prop("selected"))
		// 			$("#td-partida").text(codigo_metrado2);
		// 	});
		// }
		// else if($("#id_metrado3").children().length > 1){
		// 	$("#id_metrado3").children().each(function(index){
		// 		if($(this).prop("selected"))
		// 			$("#td-partida").text(codigo_metrado3);
		// 	});
		// }
		// else{
		// 	$("#id_metrado2").children().each(function(index){
		// 		if($(this).prop("selected"))
		// 			$("#td-partida").text(codigo_metrado4);
		// 	});
		// }
		
	});
});