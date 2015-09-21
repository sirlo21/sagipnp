$(document).ready(function(){
	$("#id_tipo_instalacion").change(function(ev){
		var id = this.value;
		var url = "/json/?tipo_instalacion="+id;
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
});