var express = require("express");
var router = express.Router();

router.post('/', function (req, res, next) {
    var data = req.body.data;
    data = JSON.parse(data);
    console.log(data);
    res.send('Received');
});

module.exports = router;