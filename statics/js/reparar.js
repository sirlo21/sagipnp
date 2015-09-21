function numero_unidad_medida(form){
	$("input").change(function(ev){
		var id = $(this).attr("id");
		if(typeof(id) == "string"){
			if(id.endsWith(form+"_numero_unidad_medida")){
				var input = $(this);
				return Number(input.val());
			}
			else
				return false;
		}
		else
			return false;
	});
}
function precio_unitario(form){
	$("input").change(function(ev){
		var id = $(this).attr("id");
		if(typeof(id) == "string"){
			if(id.endsWith(form+"_precio_unitario")){
				var input = $(this);
				return Number(input.val());
			}
			else
				return false;
		}
		else
			return false;
	});
}
function precio_total_referencial(form){
	$("input").change(function(ev){
		var numero_unidad_medida = numero_unidad_medida(form);
		var precio_unitario = precio_unitario(form);
		var id = $(this).attr("id");
		if(typeof(id) == "string"){
			if(numero_unidad_medida && precio_unitario){
				var input = $(this);
				$("input").each(function(index){
					var input_id = $(this).attr("id");
					if($input.attr("id") == input_id){
						var total = numero_unidad_medida * precio_unitario;
						if(id.endsWith(form+"_precio_unitario"))
							var precio_total = input_id.replace(form+"_precio_unitario",form+"_precio_total_referencial");
						else if(id.endsWith(form+"_numero_unidad_medida"))
							var precio_total = input_id.replace(form+"_numero_unidad_medida",form+"_precio_total_referencial");
						$("#"+precio_total).val(total);
					}
				});
			}
		}
	});
}
precio_total_referencial("techo");
precio_total_referencial("inst_sant");
precio_total_referencial("inst_elect");
precio_total_referencial("mp");