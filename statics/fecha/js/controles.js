
function popup(url,ancho,alto) {
		var	posicion_x; 
		var posicion_y; 
		posicion_x=(screen.width/2)-(ancho/2); 
		posicion_y=(screen.height/2)-(alto/2); 
		window.open(url, "GFK - Busqueda", "width="+ancho+",height="+alto+",menubar=0,toolbar=0,location=0,directories=no,scrollbars=yes,resizable=no,left="+posicion_x+",top="+posicion_y+"");
}

