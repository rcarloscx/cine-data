//API
var cors = require('cors')
var express = require('express');

var port = 8181;
var app = express();
app.use(cors());
app.use(express.text());

app.post('/', function(req, res) {
    //INITIALIZE
    const txtComand = req.body;
    console.log('Comand=' + txtComand);

    //EXECUTE
    const { exec } = require('child_process');
    exec(txtComand, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            res.status(400).send("");
            return;
        }
        
        if (stderr!= "") {
            console.error(`stderr: ${stderr}`);
            res.status(401).send("");
        }

        //RESPONSE
        //console.log(`stdout: No. of directories = ${stdout}`);
        res.status(200).send(stdout);
    });
})

app.get('/', function(req, res) {
    //EXECUTE
    const { exec } = require('child_process');
    exec("ls -la", (error, stdout, stderr) => {
        res.status(200).send(stdout);
    });
})

app.listen(port);
console.log('API escuchando en el puerto ' + port);