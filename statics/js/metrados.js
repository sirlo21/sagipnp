$(document).ready(function(){
	function addOptions(id_metrado,args){
		if(args.length > 0){
			$(id_metrado).append("<option value selected='selected'>---------</option>");
			for(i in args){
				var id = args[i]["id"];
				var descripcion = args[i]["descripcion"];
				var option = "<option value='"+id+"'>"+descripcion+"</option>";
				$(id_metrado).append(option);
			}
		}
	}
	function getCodigosMetrado(args){
		var codigos = {};
		if(args.length > 0){
			for(i in args){
				var id = args[i]["id"];
				codigos[id] = args[i]["codigo"];
			}
		}
		return codigos;
	}
	function rollback(url,id_m){
		$.getJSON(url,function(data){
			var back = data["back"]
			var m = $(id_m).children("option[value="+back["id"]+"]");
			m.attr({selected: ""});
		});
	}
	var codigo_metrado2,codigo_metrado3,codigo_metrado4;
	$("select").change(function(ev){
		var id_select = $(this).attr("id");
		var value_select = $(this).val();
		if(id_select.endsWith("metrado1")){
			var url = "/metrado/?metrado1_id="+value_select;
			$.getJSON(url,function(data){
				var id_tabla = "#"+id_select.replace("metrado1","tabla");
				var id_metrado2 = "#"+id_select.replace("metrado1","metrado2");
				var id_metrado3 = "#"+id_select.replace("metrado1","metrado3");
				var id_metrado4 = "#"+id_select.replace("metrado1","metrado4");
				$(id_metrado2).children().remove();
				$(id_metrado3).children().remove();
				$(id_metrado4).children().remove();
				addOptions(id_metrado2,data["metrado2"]);
				codigo_metrado2 = getCodigosMetrado(data["metrado2"]);
				if($(id_metrado2).children().length > 1){
					if($(id_metrado2).val()){
						$(id_metrado2).children().each(function(index){
							if($(this).prop("selected"))
								$(" #td-partida").text(codigo_metrado2[$(this).val()]);
						});
					}
				}
			});
		}
		else if(id_select.endsWith("metrado2")){
			var url = "/metrado/?metrado2_id="+value_select;
			$.getJSON(url,function(data){
				var id_tabla = "#"+id_select.replace("metrado2","tabla");
				var id_metrado1 = "#"+id_select.replace("metrado2","metrado1");

				var id_metrado3 = "#"+id_select.replace("metrado2","metrado3");
				var id_metrado4 = "#"+id_select.replace("metrado2","metrado4");
				$(id_metrado3).children().remove();
				$(id_metrado4).children().remove();
				addOptions(id_metrado3,data["metrado3"]);
				codigo_metrado3 = getCodigosMetrado(data["metrado3"]);
				var url = "/metrado/?rollback_m1="+value_select;
				rollback(url,id_metrado1);
				if($(id_metrado3).children().length > 1){
					if($(id_metrado3).val()){
						$(id_metrado3).children().each(function(index){
							if($(this).prop("selected"))
								$(id_tabla+" #td-partida").text(codigo_metrado3[$(this).val()]);
						});
					}
				}
				else{
					if(value_select)
						$(id_tabla+" #td-partida").text(codigo_metrado2[value_select]);
				}
			});
		}
		else if(id_select.endsWith("metrado3")){
			var url = "/metrado/?metrado3_id="+value_select;
			$.getJSON(url,function(data){
				var id_tabla = "#"+id_select.replace("metrado3","tabla");
				var id_metrado1 = "#"+id_select.replace("metrado3","metrado1");
				var id_metrado2 = "#"+id_select.replace("metrado3","metrado2");
				var id_metrado4 = "#"+id_select.replace("metrado3","metrado4");
				$(id_metrado4).children().remove();
				addOptions(id_metrado4,data["metrado4"]);
				codigo_metrado4 = getCodigosMetrado(data["metrado4"]);
				var url = "/metrado/?rollback_m2="+value_select;
				rollback(url,id_metrado2);
				var m2 = $(id_metrado2);
				url = "/metrado/?rollback_m1="+m2.val();
				rollback(url,id_metrado1);
				if($(id_metrado4).children().length > 1){
					if($(id_metrado4).val()){
						$(id_metrado4).children().each(function(index){
							if($(this).prop("selected"))
								$(id_tabla+" #td-partida").text(codigo_metrado4[$(this).val()]);
						});
					}
				}
				else{
					if(value_select)
						$(id_tabla+" #td-partida").text(codigo_metrado3[value_select]);
				}
			});
		}
		else if(id_select.endsWith("metrado4")){
			var id_tabla = "#"+id_select.replace("metrado4","tabla");
			var id_metrado1 = "#"+id_select.replace("metrado4","metrado1");
			var id_metrado2 = "#"+id_select.replace("metrado4","metrado2");
			var id_metrado3 = "#"+id_select.replace("metrado4","metrado3");
			var url = "/metrado/?rollback_m3="+value_select;
			rollback(url,id_metrado3,value_select);
			var m1 = $(id_metrado1);
			var url = "/metrado/?rollback_m2="+m1.val();
			rollback(url,id_metrado2);
			var m2 = $(id_metrado2);
			url = "/metrado/?rollback_m1="+m2.val();
				rollback(url,id_metrado1);
			if($(this).children().length > 1){
				if(value_select)
					$(id_tabla+" #td-partida").text(codigo_metrado4[value_select]);
			}
		}
	});
	var val_numero=0,val_parcial=0,val_unidad=0,val_punitario=0;
	$("input").change(function(ev){
		var id_input = $(this).attr("id");
		var val_input = $(this).val();
		if(id_input.endsWith("numero")){
			var id_tabla = "#"+id_input.replace("numero","tabla");
			val_numero = val_input;
			$(id_tabla+" #td-numero-veces").text(val_input);
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
		var total = val_numero*val_parcial;
		$(id_tabla+" #td-total").text(total);
		var precio_total = val_unidad*val_punitario;
		$(id_tabla+" #td-precio-total").text(precio_total);
	});
});