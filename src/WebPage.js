//import logo from './logo.svg';

function WebPage() {

  function script1() {
    const url = "http://" + window.location.hostname + ":8181";
    const postHeader = {
      method: 'POST',
      body: "python3 cinepolis.py"
    }
    fetch(url, postHeader).then(response => response.text()).then((response) => {
      console.log(response);
    }).catch(err => console.log(err));
  }

  function script2() {
    const url = "http://" + window.location.hostname + ":8181";
    const postHeader = {
      method: 'POST',
      body: "python3 cinepolis.py"
    }
    fetch(url, postHeader).then(response => response.text()).then((response) => {
      console.log(response);
    }).catch(err => console.log(err));
  }

  return (
    <div class="container-fluid p-5 bg-primary text-white">
      <div class="my-3 text-white text-center">
        <h1>Trabajo Final - Cines</h1>
        <p>Curso de Business Intelligence y Big Data Marzo 2022</p>
      </div>
      <div class="row">
        <div class="col-md-4">
          <div class="row">
            <div class="col-12">
              <h3>Generar Archivos</h3>
              <button type="button" class="btn btn-warning" onClick={script1}>Ejecutar</button>
            </div>
            <div class="col-12">
              <h3>Cargar Archivos</h3>
              <div class="mb-1">
                <label for="svFile" class="form-label">Excel - El Salvador</label>
                <input class="form-control" type="file" id="svFile"></input>
              </div>
              <div class="mb-1">
                <label for="crFile" class="form-label">Excel - Costa Rica</label>
                <input class="form-control" type="file" id="crFile"></input>
              </div>
              <div class="mb-1">
                <label for="gtFile" class="form-label">Excel - Guatemala</label>
                <input class="form-control" type="file" id="gtFile"></input>
              </div>
              <div class="mb-3">
                <label for="crFile" class="form-label">Excel - Honduras</label>
                <input class="form-control" type="file" id="hnFile"></input>
              </div>
              <div class="mb-3">
                <label for="crFile" class="form-label">Excel - Panama</label>
                <input class="form-control" type="file" id="pnFile"></input>
              </div>
              <div class="mb-3">
                <label for="ngFile" class="form-label">Excel - Nicaragua</label>
                <input class="form-control" type="file" id="ngFile"></input>
              </div>
              <button type="button" class="btn btn-warning" onClick={script2}>Cargar</button>
            </div>
          </div>
        </div>
        <div class="col-md-8 bg-light">

        </div>
      </div>
    </div>
  );
}

export default WebPage;
