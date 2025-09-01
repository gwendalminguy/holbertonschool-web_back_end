const app = require('http');

const server = app.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello Holberton School!');
})

server.listen(1245, 'localhost', () => {
  console.log('Server running at http://localhost:1245/');
})
