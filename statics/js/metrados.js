var metrados = {};
function numberWithCommas(number) {
    return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
function addOptions(id_metrado,args,rollback){
	$(id_metrado).append("<option></option>");
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
function getCodigosMetrado(args){
	var codigos = {};
	for(i in args){
		var id = args[i]["id"];
		codigos[id] = args[i]["codigo"];
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
		var id_metrado2 = "#id_metrado2";
		var id_metrado3 = "#id_metrado3";
		var id_metrado4 = "#id_metrado4";
		var tr = $("#tm > tbody tr").last().children(".td-partida");
		$.getJSON(url,function(data){
			var rollback = data["rollback"]
			$(id_metrado1).children("option[value="+rollback["metrado1_id"]+"]").attr({selected: ""});
			var url = "/metrado/json/?metrado1_id="+$(id_metrado1).val();
			$.getJSON(url,function(data){
				$(id_metrado2).children("option").remove();
				$(id_metrado3).children("option").remove();
				$(id_metrado4).children("option").remove();
				addOptions(id_metrado2,data["metrado2"],rollback["metrado2_id"]);
				codigo_metrado2 = getCodigosMetrado(data["metrado2"]);
				var m2 = $(id_metrado2).val();
				if("metrado3_id" in rollback){
					var url = "/metrado/json/?metrado2_id="+$(id_metrado2).val();
					$.getJSON(url,function(data){
						$(id_metrado3).children("option").remove();
						$(id_metrado4).children("option").remove();
						addOptions(id_metrado3,data["metrado3"],rollback["metrado3_id"]);
						codigo_metrado3 = getCodigosMetrado(data["metrado3"]);
						var m3_0 = data["metrado3"][0]["descripcion"];
						var m3 = $(id_metrado3).val();
						var m4_0;
						if(m3_0 == "N/A"){
							var text = $(id_metrado3).children("option").get(1).text
							if($(id_metrado3).val() && text != "N/A"){
								$(id_metrado3).children().each(function(index){
									if($(this).prop("selected"))
										tr.text(codigo_metrado3[m3]);
								});
							}
							else{
								tr.text(codigo_metrado2[m2]);
							}
						}
						if("metrado4_id" in rollback){
							var url = "/metrado/json/?metrado3_id="+$(id_metrado3).val();
							$.getJSON(url,function(data){
									$(id_metrado4).children("option").remove();
									addOptions(id_metrado4,data["metrado4"],rollback["metrado4_id"]);
									codigo_metrado4 = getCodigosMetrado(data["metrado4"]);
									m4_0 = data["metrado4"][0]["descripcion"];
									if(m3_0 != "N/A" && m4_0 == "N/A"){
										var text1 = $(id_metrado3).children("option").get(1).text
										var text2 = $(id_metrado4).children("option").get(1).text
										if($(id_metrado4).val() && text2 != "N/A"){
											$(id_metrado4).children().each(function(index){
												if($(this).prop("selected"))
													tr.text(codigo_metrado4[$(id_metrado4).val()]);
											});
										}
										else if(text2 == "N/A"){
											tr.text(codigo_metrado3[m3]);
										}
									}
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
	$("select").change(function(event){
		var id_select = "#"+$(this).attr("id");
		var value_select = $(this).val();
		var id_metrado1 = "#id_metrado1";
		var id_metrado2 = "#id_metrado2";
		var id_metrado3 = "#id_metrado3";
		var id_metrado4 = "#id_metrado4";
		var tr = $("#tm > tbody tr").last().children(".td-partida");
		var tr_id = $("#tm > tbody tr").last().attr("id");
		if(id_select == id_metrado1){
			$(id_metrado2).children("option").remove();
			$(id_metrado3).children("option").remove();
			$(id_metrado4).children("option").remove();
			var url = "/metrado/json/?metrado1_id="+value_select;
			$.getJSON(url,function(data){
				addOptions(id_metrado2,data["metrado2"]);
				codigo_metrado2 = getCodigosMetrado(data["metrado2"]);
			});
		}
		else if(id_select == id_metrado2){
			$(id_metrado3).children("option").remove();
			$(id_metrado4).children("option").remove();
			var url = "/metrado/json/?metrado2_id="+value_select;
			$.getJSON(url,function(data){
				addOptions(id_metrado3,data["metrado3"]);
				codigo_metrado3 = getCodigosMetrado(data["metrado3"]);
				if($(id_metrado3).children().length > 1){
					var text = $(id_metrado3).children("option").get(1).text
					if($(id_metrado3).val() && text != "N/A"){
						$(id_metrado3).children().each(function(index){
							if($(this).prop("selected"))
								tr.text(codigo_metrado3[$(this).val()]);
						});
					}
					else{
						if(value_select)
							tr.text(codigo_metrado2[value_select]);
					}
				}
				else{
					if(value_select)
						tr.text(codigo_metrado2[value_select]);
				}
			});
		}
		else if(id_select == id_metrado3){
			$(id_metrado4).children("option").remove();
			var url = "/metrado/json/?metrado3_id="+value_select;
			$.getJSON(url,function(data){
				addOptions(id_metrado4,data["metrado4"]);
				codigo_metrado4 = getCodigosMetrado(data["metrado4"]);
				if($(id_metrado4).children().length > 1){
					var text1 = $(id_metrado3).children("option").get(1).text
					var text2 = $(id_metrado4).children("option").get(1).text
					if($(id_metrado4).val() && text1 != "N/A"){
						$(id_metrado4).children().each(function(index){
							if($(this).prop("selected"))
								tr.text(codigo_metrado4[$(this).val()]);
						});
					}
					else if(text1 != "N/A"){
						if(value_select)
							tr.text(codigo_metrado3[value_select]);
					}
				}
				else{
					if(value_select)
						tr.text(codigo_metrado3[value_select]);
				}
			});
		}
		else if(id_select == id_metrado4){
			var text = $(id_metrado4).children("option[value="+value_select+"]").text();
			if(value_select && text != "N/A")
				tr.text(codigo_metrado4[value_select]);
		}
		metrados[tr_id] = $("#ficha-tecnica-form");
		$("input").trigger("change");
	});
	$("#add").click(function(event){
		var tr_id = $("#tm > tbody > tr").last().attr("id");
		$(".error").remove();
		if(tr_id in metrados){
			var valid = $("<input type='hidden' name='valid' value='"+true+"'/>");
			metrados[tr_id].append(valid);
			var form = new FormData(metrados[tr_id].get(0));
			$.ajax({
				url: $("#ficha-tecnica-form").attr("action"),
				data: form,
				type: "POST",
				success: function(data){
					if(data["valid"]){
						metrados[tr_id].find("input[name=valid]").remove();
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
						new_tr += '<td class="td-total">0</td>\n';
						new_tr += '<td class="td-unidad"></td>\n';
						new_tr += '<td class="td-precio-unitario">S./ 0</td>\n';
						new_tr += '<td class="td-precio-total">S./ 0</td>\n';
						new_tr += '<td>\n<button type="button" onclick="removeTr(\''+new_tr_id+'\');" class="btn btn-danger">Borrar</button>\n</td>\n';
						new_tr += '</tr>';
						$("#tm > tbody").append($(new_tr));
						$("#ficha-tecnica-form").get(0).reset();
					}
					else{
						$.each(data["errors"],function(key,value){
							console.log(key+": "+value);
							var error = "<p class='help-block'>"+value+"</p>";
							$(".errors_"+key).append("\n<div class='col-lg-12 error'>\n"+error+"\n</div>");
						});
					}
				},
				processData: false,
				contentType: false,
				error: function(data){
					console.log(data);
				}
			});
		}
		else
			alert("Llene el formulario primero");
	});
	$("input").change(function(event){
		var tr = $("#tm > tbody > tr").last();
		var tr_id = tr.attr("id");
		var $numero = $("#id_numero");
		var $val_numero = $numero.val();
		tr.children(".td-numero-veces").text(numberWithCommas($val_numero));
		var $largo = $("#id_largo");
		var $val_largo = $largo.val();
		tr.children(".td-dimensiones-largo").text(numberWithCommas($val_largo));
		var $ancho = $("#id_ancho");
		var $val_ancho = $ancho.val();
		tr.children(".td-dimensiones-ancho").text(numberWithCommas($val_ancho));
		var $alto = $("#id_alto");
		var $val_alto = $alto.val();
		tr.children(".td-dimensiones-altura").text(numberWithCommas($val_alto));
		var $parcial = $("#id_parcial");
		var $val_parcial = $parcial.val();
		tr.children(".td-parcial").text(numberWithCommas($val_parcial));
		var $unidad = $("#id_unidad");
		var $val_unidad = $unidad.val();
		tr.children(".td-unidad").text(numberWithCommas($val_unidad));
		var $punitario = $("#id_punitario");
		var $val_punitario = $punitario.val();
		tr.children(".td-precio-unitario").text("S./ "+numberWithCommas($val_punitario));
		var total = $val_numero*$val_parcial;
		tr.children(".td-total").text(total);
		var precio_total = $val_unidad*$val_punitario;
		tr.children(".td-precio-total").text("S./ "+numberWithCommas(precio_total));
		metrados[tr_id] = $("#ficha-tecnica-form");
	});
	$("#ficha-tecnica-form").submit(function(event){
		event.preventDefault();
		$(".estado").remove();
		if(confirm("¿Estas seguro de que quiere guardar?")){
			var tr_id = $("#tm > tbody > tr").last().attr("id");
			var valid = $("<input>").attr({type: "hidden",name: "valid"}).val(true);
			var div = $("<div>").addClass("estado");
			var span = $("<span>");
			metrados[tr_id].append(valid);
			var form = new FormData(metrados[tr_id].get(0));
			if(tr_id in metrados){
				$.ajax({
					url: $(this).attr("action"),
					data: form,
					type: "POST",
					success: function(data){
						var span_html = span;
						var div_html = div;
						span_html.addClass("success").text("Enviando...");
						div_html.html(span_html);
						$("#submit").after(div_html);
						if(data["valid"]){
							metrados[tr_id].find("input[name=valid]").remove();
							var arr = [];
							$.each(metrados,function(key,value){
								if(value != undefined)
									arr.push(value);
							});
							for(var i in arr){
								$(".estado").remove();
								var formdata = new FormData(arr[i].get(0));
								$.ajax({
									url: $("#ficha-tecnica-form").attr("action"),
									data: formdata,
									type: "POST",
									success: function(data){
										span_html = span;
										div_html = div;
										span_html.addClass("success").text("Enviando...");
										div_html.html(span_html);
										$("#submit").after(div_html);
									},
									complete: function(){
										if(arr.length-1 == i)
											window.location = "/";
									},
									processData: false,
									contentType: false,
									error: function(data){
										$(".estado").remove();
										span_html = span;
										div_html = div;
										span_html.addClass("error").text("Error al enviar");
										div_html.html(span_html);
										$("#submit").after(div_html);
										console.log(data);
									}
								});
							}
						}
						else{
							$(".estado").remove();
							$.each(data["errors"],function(key,value){
								console.log(key+": "+value);
								var error = "<p class='help-block'>"+value+"</p>";
								$(".errors_"+key).append("\n<div class='col-lg-12 error'>\n"+error+"\n</div>");
							});
						}
					},
					processData: false,
					contentType: false,
					error: function(data){
						console.log(1);
						console.log(data);
					}
				});
			}
			else
				alert("Llene el formulario primero");
		}
	});
});