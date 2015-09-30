var metrados = {};
function addOptions(id_metrado,args,rollback){
	if(args.length > 0){
		for(i in args){
			var id = args[i]["id"];
			var descripcion = args[i]["descripcion"];
			if(rollback){
				if(id == rollback)
					var option = "<option value='"+id+"' selected>"+descripcion+"</option>";
				else
					var option = "<option value='"+id+"'>"+descripcion+"</option>";
			}
			else
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
function removeTr(id){
	if(confirm("¿Estas seguro(a) de querer borrar esta fila?")){
		if(id in metrados)
			metrados[id] = undefined;
		$("#"+id).remove();
	}
}
$(document).ready(function(){
	var codigo_metrado2,codigo_metrado3,codigo_metrado4;
	$("#id_buscar").click(function(event){
		var input_nombre_id = "#id_nombre";
		var url = "/metrado/json/?rollback="+$(input_nombre_id).val();
		var id_tabla = input_nombre_id.replace("nombre","tabla");
		var id_metrado2 = input_nombre_id.replace("nombre","metrado2");
		var id_metrado3 = input_nombre_id.replace("nombre","metrado3");
		var id_metrado4 = input_nombre_id.replace("nombre","metrado4");
		var tr = "#"+$("#tm > tbody tr").last().attr("id");
		$.getJSON(url,function(data){
			var rollback = data["rollback"]
			$(id_metrado1).children("option[value="+rollback["metrado1_id"]+"]").attr({selected: ""});
			var url = "/metrado/json/?metrado1_id="+$(id_metrado1).val();
			$.getJSON(url,function(data){
				$(id_metrado2).children("option[value]").remove();
				$(id_metrado3).children("option[value]").remove();
				$(id_metrado4).children("option[value]").remove();
				addOptions(id_metrado2,data["metrado2"],rollback["metrado2_id"]);
				codigo_metrado2 = getCodigosMetrado(data["metrado2"]);
				if("metrado3_id" in rollback){
					var url = "/metrado/json/?metrado2_id="+$(id_metrado2).val();
					$.getJSON(url,function(data){
						$(id_metrado3).children("option[value]").remove();
						$(id_metrado4).children("option[value]").remove();
						addOptions(id_metrado3,data["metrado3"],rollback["metrado3_id"]);
						codigo_metrado3 = getCodigosMetrado(data["metrado3"]);
						if("metrado4_id" in rollback){
							var url = "/metrado/json/?metrado3_id="+$(id_metrado3).val();
							$.getJSON(url,function(data){
								$(id_metrado4).children("option[value]").remove();
								addOptions(id_metrado4,data["metrado4"],rollback["metrado4_id"]);
								codigo_metrado4 = getCodigosMetrado(data["metrado4"]);
								$(id_metrado4).trigger("change");
							});
						}
						else
							$(id_metrado3).trigger("change");
					});
				}
				else
					$(id_metrado2).trigger("change");
			});
		});
		$(input_nombre_id).val("");
	});
	$("select").change(function(ev){
		var id_select = "#"+$(this).attr("id");
		var value_select = $(this).val();
		var id_metrado1 = "#id_metrado1";
		var id_metrado2 = "#id_metrado2";
		var id_metrado3 = "#id_metrado3";
		var id_metrado4 = "#id_metrado4";
		var tr = $("#tm > tbody tr").last().children(".td-partida");
		var tr_id = $("#tm > tbody tr").last().attr("id");
		if(id_select == id_metrado1){
			$(id_metrado2).children("option[value]").remove();
			$(id_metrado3).children("option[value]").remove();
			$(id_metrado4).children("option[value]").remove();
			var url = "/metrado/json/?metrado1_id="+value_select;
			$.getJSON(url,function(data){
				addOptions(id_metrado2,data["metrado2"]);
				codigo_metrado2 = getCodigosMetrado(data["metrado2"]);
			});
		}
		else if(id_select == id_metrado2){
			$(id_metrado3).children("option[value]").remove();
			$(id_metrado4).children("option[value]").remove();
			var url = "/metrado/json/?metrado2_id="+value_select;
			$.getJSON(url,function(data){
				addOptions(id_metrado3,data["metrado3"]);
				codigo_metrado3 = getCodigosMetrado(data["metrado3"]);
				if($(id_metrado3).children().length > 1){
					if($(id_metrado3).val()){
						$(id_metrado3).children().each(function(index){
							if($(this).prop("selected"))
								tr.text(codigo_metrado3[$(this).val()]);
						});
					}
				}
				else{
					if(value_select)
						tr.text(codigo_metrado2[value_select]);
				}
			});
		}
		else if(id_select == id_metrado3){
			$(id_metrado4).children("option[value]").remove();
			var url = "/metrado/json/?metrado3_id="+value_select;
			$.getJSON(url,function(data){
				addOptions(id_metrado4,data["metrado4"]);
				codigo_metrado4 = getCodigosMetrado(data["metrado4"]);
				if($(id_metrado4).children().length > 1){
					if($(id_metrado4).val()){
						$(id_metrado4).children().each(function(index){
							if($(this).prop("selected"))
								tr.text(codigo_metrado4[$(this).val()]);
						});
					}
				}
				else{
					if(value_select)
						tr.text(codigo_metrado3[value_select]);
				}
			});
		}
		else if(id_select == id_metrado4){
			if($(this).children().length > 1){
				if(value_select)
					tr.text(codigo_metrado4[value_select]);
			}
		}
		metrados[tr_id] = $("#ficha-tecnica-form").serialize();
		$("input").trigger("change");
	});
	$("#add").click(function(ev){
		var tr_id = $("#tm > tbody > tr").last().attr("id");
		if(tr_id in metrados){
			$.ajax({
				url: $("#ficha-tecnica-form").attr("action"),
				data: metrados[tr_id]+"&valid=true",
				type: "POST",
				success: function(data){
					if(data["valid"]){
						$(".erros_metrado .error").remove();
						if($("#tm > tbody > tr").length > 0)
							var new_tr_id = tr_id.replace(/\d+/g,parseInt(tr_id.match(/\d+/g))+1);
						else
							var new_tr_id = "id_ficha_tecnica-0-tr";
						var new_tr = '<tr id="'+new_tr_id+'">\n';
						new_tr += '<td class="td-partida"></td>\n';
						new_tr += '<td class="td-numero-veces"></td>\n';
						new_tr += '<td class="td-dimensiones-largo"></td>\n';
						new_tr += '<td class="td-dimensiones-ancho"></td>\n';
						new_tr += '<td class="td-dimensiones-altura"></td>\n';
						new_tr += '<td class="td-parcial"></td>\n';
						new_tr += '<td class="td-total"></td>\n';
						new_tr += '<td class="td-unidad"></td>\n';
						new_tr += '<td class="td-precio-unitario"></td>\n';
						new_tr += '<td class="td-precio-total"></td>\n';
						new_tr += '<td>\n<button type="button" onclick="removeTr(\''+new_tr_id+'\');" class="btn btn-danger">Borrar</button>\n</td>\n';
						new_tr += '</tr>';
						$("#tm > tbody").append($(new_tr));
					}
					else{
						$(".erros_metrado .error").remove();
						$.each(data,function(key,value){
							if(typeof(value) == "object"){
								$.each(value,function(key,value){
									var error = "<p class='help-block'>"+value+"</p>";
									$(".erros_metrado").append("\n<div class='col-lg-3 error'>\n"+error+"\n</div>");
								});
							}
						});
					}
				}
			});
		}
		else
			alert("Llene el formulario primero");
	});
	$("input").change(function(ev){
		var tr = $("#tm > tbody > tr").last();
		var tr_id = tr.attr("id");
		var $numero = $("#id_numero");
		var $val_numero = $numero.val();
		tr.children(".td-numero-veces").text($val_numero);
		var $largo = $("#id_largo");
		var $val_largo = $largo.val();
		tr.children(".td-dimensiones-largo").text($val_largo);
		var $ancho = $("#id_ancho");
		var $val_ancho = $ancho.val();
		tr.children(".td-dimensiones-ancho").text($val_ancho);
		var $alto = $("#id_alto");
		var $val_alto = $alto.val();
		tr.children(".td-dimensiones-altura").text($val_alto);
		var $parcial = $("#id_parcial");
		var $val_parcial = $parcial.val();
		tr.children(".td-parcial").text($val_parcial);
		var $unidad = $("#id_unidad");
		var $val_unidad = $unidad.val();
		tr.children(".td-unidad").text($val_unidad);
		var $punitario = $("#id_punitario");
		var $val_punitario = $punitario.val();
		tr.children(".td-precio-unitario").text($val_punitario);
		var total = $val_numero*$val_parcial;
		tr.children(".td-total").text(total);
		var precio_total = $val_unidad*$val_punitario;
		tr.children(".td-precio-total").text(precio_total);
		metrados[tr_id] = $("#ficha-tecnica-form").serialize();
	});
	$("#ficha-tecnica-form").submit(function(ev){
		if(confirm("¿Estas seguro de que quiere guardar por que es gay?")){
			$.each(metrados,function(key,value){
				if(value != undefined){
					$.ajax({
						url: $(this).attr("action"),
						data: value+"&value=false",
						type: "POST",
					});
				}
			});
		}
		window.history.go("/");
		ev.preventDefault();
	});
});