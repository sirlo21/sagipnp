function delete_row(){
	if($("#ayudas_form").children(".ayuda").length <= 0){
		$(".add-row").prepend($("<h2 id='vacio'>").text("No hay ninguna ayuda"));
	}
}
var summernote = function(){
	$('.summernote').summernote({
		height: 200,
		tabsize: 2,
		codemirror: {theme: 'monokai'}
	});
}
$(document).ready(function(){
	summernote();
	$(".delete-row").ready(function(){
		$.each($(".delete-row"),function(key,value){
			$(this).attr({onclick: "delete_row();"});
		});
	});
	$(".add-row").ready(function(){
		$(".add-row").click(function(event){
			$("#vacio").remove();
			$.each($(".delete-row"),function(key,value){
				$(this).attr({onclick: "delete_row();"});
			});
		});
	});
});