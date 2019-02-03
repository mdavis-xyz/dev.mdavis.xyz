var http = require('http');
var fs = require('fs');
var url = require('url');

/**
 * HTTP Cloud Function.
 *
 * @param {Object} req Cloud Function request context.
 * @param {Object} res Cloud Function response context.
 */
exports.web = (req, res) => {
   res.writeHead(200, {'Content-Type': 'text/html'});
   var content = fs.readFileSync('./equation.html').toString();
   res.write(content);
   res.end();
};
