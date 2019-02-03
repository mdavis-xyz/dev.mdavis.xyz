var http = require('http');
var fs = require('fs');
var url = require('url');

fs.readFile('./site.html', function (err, data) {
    if (err) {
        throw err;
    }
    html = data;
});

http.createServer(function (req, res) {
   if ((req.url == '/') || (req.url == '/index.html') || (req.url == '/site.html'){
      res.writeHead(200, {'Content-Type': 'text/html'});
      res.write(html);
   }else if (req.url.indexOf('..') == -1){
      // no sneaky shit
      res.writeHead(200, {'Content-Type': 'text/html'});
   }
      res.writeHead(200, {'Content-Type': 'text/html'});
      var content = fs.readFileSync(req.url).toString();
      res.write(content);
   }
   res.end();
}).listen(8081);
