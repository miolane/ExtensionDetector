var express = require("express");
var router = express.Router();
var fs = require('fs');

router.post('/', function (req, res, next) {
    var data_ = req.body.data;
    var data = JSON.parse(data_);
    var file = __dirname + '/../diffs.json';
    var diffs = data["diffs"];
    fs.readFile(file, 'utf-8', function (err, content) {
        var dataset = JSON.parse(content);
        var list = [];
        for (var diff of diffs) {
            for (var ext in dataset) {
                var found = false;
                for (var entry of dataset[ext]) {
                    if (JSON.stringify(entry) === JSON.stringify(diff)) {
                        if (list.indexOf(ext) === -1)
                            list.push(ext);
                        found = true;
                        break;
                    }
                }
                if (found === true)
                    break;
            }
        }
        var resp = JSON.stringify(list, null, "\t");
        res.send(resp);
    });

});

module.exports = router;