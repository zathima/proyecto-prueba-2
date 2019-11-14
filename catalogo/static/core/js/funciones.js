var x;
x=$(document);
x.ready(inicializarEventos);



function inicializarEventos()
{
  var x;
  x=$("h1");			//recuperamos selector				
  x.click(presionh1)		//a través del método click invocamos la función.	
  x=$("H3");
  x.click(presionh3)
}

function presionh1()		//definición de la función, modificamos estilo
{
  var x;
  x=$("h1");
  x.css("color","yellow");
  x.css("font-family","times new roman");
}

function presionh3()
{
  var x;
  x=$("H3");
  x.css("color","yellow");
  x.css("font-family","times new roman");
}
