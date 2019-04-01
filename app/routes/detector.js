var express = require('express');
var router = express.Router();

var extList = require('../extList');

// router.get('/NightShift', function(req, res, next) {
//   res.render('NightShift', { title: 'NightShift' });
// });

extList.forEach(function (element) {
  extName = element;
  router.get('/' + extName, function (req, res, next) {
    res.render(extName, {title: extName})
  })
});


module.exports = router;