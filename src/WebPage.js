//import logo from './logo.svg';

function WebPage() {

  function sayHello() {
    alert('EJECUTANDO!');
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
