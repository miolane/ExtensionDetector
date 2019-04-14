var express = require("express");
var router = express.Router();
var fs = require('fs');

router.post('/', function (req, res, next) {
    var data_ = req.body.data;
    var data = JSON.parse(data_);
    console.log(data['ext']);
    var extName = data['ext'];
    var file = __dirname + '/../diffs.json';
    fs.readFile(file, 'utf-8', function (err, content) {
        var file_t = file;
        if(err)
            console.error(err);
        var json = JSON.parse(content);
        json[extName] = data.diffs;
        fs.writeFile(file_t, JSON.stringify(json, null, '\t'), function (err) {
            if(err)
                console.error(err);
        })

    });


    res.send('Received');
});

module.exports = router;