var express = require("express");
var router = express.Router();
var fs = require('fs');

router.post('/', function (req, res, next) {
    var data_ = req.body.data;
    data = JSON.parse(data_);
    var extName = data['ext'];
    var file = __dirname + '/../diffs/' +extName + '.json';
    fs.open(file, 'w+', function (err, fd) {
        if(err) return console.log(err);
        else
            fs.write(fd, data_, function (err) {
                if (err) return console.log(err);
                else
                    fs.close(fd, function (err) {
                        if (err) console.log(err);
                    });
            });
    });

    res.send('Received');
});

module.exports = router;