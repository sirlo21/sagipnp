var getProvincias = getProvinciasFactory("#id_ubigeo_1", "#id_ubigeo_2");
var getDistritos = getDistritosFactory("#id_ubigeo_2");
$('#id_ubigeo_0').on('change', function (){
	getProvincias(this.value);
});
$('#id_ubigeo_1').on('change', function (){
	getDistritos(this.value);
});