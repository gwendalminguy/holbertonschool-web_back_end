function countStudents(path) {
  const fs = require('fs');

  fs.readFile(path, 'utf8', (err, data) => {
	if (err) {
		throw new Error('Cannot load the database');
	}

    const content = data.split('\n');
	const CSStudents = [];
	const SWEStudents = [];

	for (let i = 1; i < content.length; i++) {
      const [firstname, lastname, age, field] = content[i].split(',');
	  if (field === 'CS') {
		CSStudents.push(firstname);
	  } else if (field === 'SWE') {
		SWEStudents.push(firstname);
	  }
	}

	const stringCS = CSStudents.join(', ');
	const stringSWE = SWEStudents.join(', ');

	console.log(`Number of students: ${CSStudents.length + SWEStudents.length}`);
	console.log(`Number of students in CS: ${CSStudents.length}. List: ${stringCS}`);
	console.log(`Number of students in SWE: ${SWEStudents.length}. List: ${stringSWE}`);
  });
}

module.exports = countStudents;
