//import logo from './logo.svg';

function WebPage() {

  function script1() {
    const url = "http://" + window.location.hostname + ":8181";
    const postHeader = {
      method: 'POST',
      body: "ls -l"
    }
    fetch(url, postHeader).then(response => response.text()).then((response) => {
        console.log(response);
    }).catch(err => console.log(err));
  }

  return (
    <div class="container-fluid p-5 bg-primary text-white text-center">
      <h1>Trabajo Final - Cines</h1>
      <p>Curso de Business Intelligence y Big Data Marzo 2022</p>
      <button type="button" class="btn btn-warning" onClick={script1}>Ejecutar</button>
    </div>
  );
}

export default WebPage;
