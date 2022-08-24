import React, { useState } from "react";

function WebPage() {

  //FILE CONST
  const [selectedFile, setSelectedFile] = useState(null);

  const script1 = () => {
    const url = "http://" + window.location.hostname + ":8181";
    const postHeader = {
      method: 'POST',
      body: "python3 script.py"
    }
    fetch(url, postHeader).then(response => response.text()).then((response) => {
      console.log(response);
    }).catch(err => console.log(err));
  }

  const script2 = () => {
    const url = "http://" + window.location.hostname + ":8181";
    const postHeader = {
      method: 'POST',
      //body: "python3 cinepolis.py"
      //body: "echo \"holaaa\""
      body: "ls -la"
    }
    fetch(url, postHeader).then(response => response.text()).then((response) => {
      console.log(response);
    }).catch(err => console.log(err));
  }

  const uploadFile = (e) => {
    const f = e.target.files[0];
    console.log(f);
  }

  return (
    <div class="container-fluid p-5 bg-primary text-white">
      <div class="my-3 text-white text-center">
        <h1>Trabajo Final - Cines</h1>
        <p>Curso de Business Intelligence y Big Data Marzo 2022</p>
      </div>
      <div class="row">
        <div class="col-md-5">
          <div class="row">
            <div class="col-12">
              <h3>Generar Archivos</h3>
              <button type="button" class="btn btn-warning" onClick={script1}>Ejecutar</button>
            </div>
            <div class="col-12">
              <h3>Cargar Archivos</h3>
              <div class="mb-1">
                <input
                  class="form-control"
                  type="file"
                  value={selectedFile}
                  onChange={uploadFile}
                  multiple
                />
              </div>
              <button type="button" class="btn btn-warning" onClick={script2}>Cargar</button>
            </div>
          </div>
        </div>
        <div class="col-md-7">
          <table class="table table-hover bg-light">
            <thead>
              <tr>
                <th scope="col">#</th>
                <th scope="col">Archivo</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">1</th>
                <td>Mark</td>
              </tr>
              <tr>
                <th scope="row">1</th>
                <td>Mark</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default WebPage;
