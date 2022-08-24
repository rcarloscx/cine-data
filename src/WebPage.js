import React, { useState, useEffect } from "react";

import { FileUpload } from 'primereact/fileupload';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';

function WebPage() {

  //FILE CONST
  const [products, setProducts] = useState([]);

  const runComandServer = (txtComand) => {
    const url = "http://" + window.location.hostname + ":8181";
    const postHeader = {
      method: 'POST',
      body: txtComand
      //body: "python3 script.py"
    }
    fetch(url, postHeader).then(response => response.text()).then((response) => {
      console.log(response);
    }).catch(err => console.log(err));
  }

  useEffect(() => {
    //productService.getProductsSmall().then(data => setProducts(data));
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const onUpload = () => {
    console.log({ severity: 'info', summary: 'Success', detail: 'File Uploaded' });
  }

  return (
    <div class="grid">
      {/* TOP */}
      <div class="col-12">
        <h1>Trabajo Final - Cines</h1>
        <p>Curso de Business Intelligence y Big Data Marzo 2022</p>
      </div>
      {/* Izquierda */}
      <div class="col-12 md:col-4 min-w-427">
        <h3>Generar Archivos</h3>
        <button type="button" class="btn btn-warning" onClick={() => runComandServer("ls -l")}>Ejecutar</button>
        <h3>Cargar Archivos</h3>
        <h5>Advanced</h5>
        <FileUpload
          name="demo[]"
          url="https://primefaces.org/primereact/showcase/upload.php"
          onUpload={onUpload}
          multiple accept="image/*"
          maxFileSize={1000000}
          emptyTemplate={<p className="m-0">Drag and drop files to here to upload.</p>}
        />
        <button type="button" class="btn btn-warning" onClick={() => runComandServer("ls -l")}>Cargar</button>
      </div>
      {/* Derecha */}
      <div class="col-12 md:col-8">
        <DataTable value={products} responsiveLayout="scroll">
          <Column field="numero" header="Numero"></Column>
          <Column field="nombre" header="Nombre"></Column>
        </DataTable>
      </div>
    </div>
  );
}

export default WebPage;
