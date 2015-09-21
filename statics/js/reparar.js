function numero_unidad_medida(input,form){
	var unidad = input.attr("id").replace(form+"_precio_unitario",form+"_numero_unidad_medida");
	unidad = unidad.replace(form+"_precio_total_referencial",form+"_numero_unidad_medida");
	var id = $("#"+unidad).attr("id");
	if(typeof(id) == "string"){
		if(id.endsWith(form+"_numero_unidad_medida"))
			return Number($("#"+id).val());
		else
			return false;
	}
	else
		return false;
}
function precio_unitario(input,form){
	var precio = input.attr("id").replace(form+"_numero_unidad_medida",form+"_precio_unitario");
	precio = precio.replace(form+"_precio_total_referencial",form+"_precio_unitario");
	var id = $("#"+precio).attr("id");
	if(typeof(id) == "string"){
		if(id.endsWith(form+"_precio_unitario"))
			return Number($("#"+id).val());
		else
			return false;
	}
	else
		return false;
}
function precio_total_referencial(form){
	$("input[type='number']").change(function(ev){
		var $numero_unidad_medida = numero_unidad_medida($(this),form);
		var $precio_unitario = precio_unitario($(this),form);
		var id = $(this).attr("id");
		if(typeof(id) == "string"){
			if(($numero_unidad_medida || $numero_unidad_medida == 0) && ($precio_unitario || $precio_unitario == 0)){
				var input = $(this);
				$("input[type='number']").each(function(index){
					var input_id = $(this).attr("id");
					if(input.attr("id") == input_id){
						var total = $numero_unidad_medida*$precio_unitario;
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