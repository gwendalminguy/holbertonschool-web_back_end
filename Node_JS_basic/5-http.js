const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  const file = process.argv[2];
  const { url } = req;

  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (url === '/') {
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    await countStudents(file)
      .then((data) => res.end(`This is the list of our students\n${data}`))
      .catch((err) => res.end(err.toString()));
  }
});

app.listen(1245, 'localhost', () => {
  console.log('Server running at http://localhost:1245/');
});

module.exports = app;
