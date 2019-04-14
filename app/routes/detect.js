var express = require('express');
var router = express.Router();



router.get('/', function (req, res) {
    var extName = "";
    // console.log(req.query);
    if (req.query.ext)
        extName = req.query.ext;
    res.render('detect', {title: extName});
});
// extList.forEach(function (element) {
//     extName = element;
//     router.get('/' + extName, function (req, res, next) {
//         res.render(extName, {title: extName})
//     })
// });


module.exports = router;