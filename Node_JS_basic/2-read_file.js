const fs = require('fs');

function countStudents(path) {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      throw new Error('Cannot load the database');
    }

    const content = data.split('\n');
    const fields = {};
    let total = 0;

    for (let i = 1; i < content.length; i += 1) {
      const [firstname, , , field] = content[i].split(',');
      if (!(field in fields)) {
        fields[field] = [];
      }
      fields[field].push(firstname);
      total += 1;
    }

    console.log(`Number of students: ${total}`);
    for (element in fields) {
      console.log(`Number of students in ${element}: ${fields[element].length}. List: ${fields[element].join(', ')}`)
    }
  });
}

module.exports = countStudents;
