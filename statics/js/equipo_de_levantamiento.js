$(document).ready(function(){
	for(var i in $("input[name=ejecutando_mejoras_mantenimiento]")){
		var obj = $("input[name=ejecutando_mejoras_mantenimiento]")[i];
		if(obj.value == 2 && obj.checked){
			$(".monto").show();
			break;
		}
		else
			$(".monto").hide();
	}
	$("#id_tipo_instalacion").change(function(event){
		var id = this.value;
		var url = "/equipo-de-levantamiento/json/?tipo_instalacion="+id;
		$.getJSON(url,function(data){
			$("#id_tipo_comisaria").children().remove();
			$("#id_clase_comisaria").children().remove();
			$("#id_especialidad").children().remove();
			$("#id_categoria").children().remove();

			var success = function(key){
				var arr = data[key];
				for(var i=0;i<arr.length;i++){
					var obj = arr[i];
					var option = "<option value='"+obj["id"]+"'>"+obj["name"]+"</option>";
					$("#id_"+key).append(option);
				}
			}
			success("tipo_comisaria");
			success("clase_comisaria");
			success("especialidad");
			success("categoria");
		});
	});
	$("input[name=ejecutando_mejoras_mantenimiento]").change(function(event){
		if($(this).val() == 2)
			$(".monto").show();
		else
			$(".monto").hide();
	});
});