//import logo from './logo.svg';

function WebPage() {

  function sayHello() {
    //alert('EJECUTANDO!');
    const postHeader = { method: 'POST', body: "ls -l", headers: { 'Content-Type': 'text/plain' } }

    const url = "http://" + window.location.hostname + ":8181";
    fetch(url, postHeader).then(function (response) {
      if (response.ok) {
        console.log(response.text());
      } else {
        console.log('Respuesta de red OK pero respuesta HTTP no OK');
      }
    }).then(data => console.log(data));
  }

  return (
    <div class="container-fluid p-5 bg-primary text-white text-center">
      <h1>Trabajo Final - Cines</h1>
      <p>Curso de Business Intelligence y Big Data Marzo 2022</p>
      <button type="button" class="btn btn-warning" onClick={sayHello}>Ejecutar</button>
    </div>
  );
}

export default WebPage;
