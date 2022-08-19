//API
var express = require('express')
var app = express()

var port = process.env.PORT || 8181
app.use(express.text())

app.post('/', function(req, res) {
    //INITIALIZE
    const txtComand = req.body;
    console.log('Comand=' + txtComand)

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

app.listen(port)
console.log('API escuchando en el puerto ' + port)