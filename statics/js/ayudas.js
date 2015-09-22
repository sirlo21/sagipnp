var summernote = function(){
	$('.summernote').summernote({
		height: 200,
		tabsize: 2,
		codemirror: {theme: 'monokai'}
	});
}
$(document).ready(function(){
	var submit = true;
	$("#form_ayuda").submit(function(event){
		$(".guardado").remove();
		$(".error").remove();
		if(submit){
			$.ajax({
				url: $(this).attr("action"),
				data: $(this).serialize(),
				type: $(this).attr("method"),
				success: function(data){
					$(".submit").after("<span class='guardado'>&nbsp;Guardado!</span>");
				},	
				error: function(data){
					$(".submit").after("<span class='error'>&nbsp;Error al guardado!</span>")
				}
			});
		}
		return event.preventDefault();
	});
	$("#create").click(function(event){
		$.ajax({
			url: $(this).attr("href"),
			type: "GET",
			success: function(data){
				var ayuda = data["ayuda"];
				var fields = "<label for='title'><li>Titulo: </li></label>";
				fields += "<input class='form-control' id='title' name='title["+ayuda["id"]+"]' maxlength='40' type='text' value='"+ayuda["title"]+"' /><br/>";
				fields += "<label for='posicion'>Posicion: </label>";
				fields += "<input class='form-control' id='posicion' name='posicion["+ayuda["id"]+"]' type='number' value='"+ayuda["posicion"]+"' /><br/>";
				fields += "<label for='text'>Texto:</label><br/>";
				fields += "<textarea id='text["+ayuda["id"]+"]' type='text' class='summernote' name='text["+ayuda["id"]+"]' placeholder='Texto de ayuda'></textarea>";
				if($("#vacio").length > 0){
					$("#vacio").before("<input class='btn btn-success submit' id='submit1' type='submit' value='Guardar' /><br/>");
					$("#vacio").remove();
					$("#submit1").after("<input class='btn btn-success submit' id='submit2' type='submit' value='Guardar' /><br/>");
				}
				$("#submit2").before("<div class='form-group'>"+fields+"</div><br/>");
				summernote();
			}
		});
		return event.preventDefault();
	});
});