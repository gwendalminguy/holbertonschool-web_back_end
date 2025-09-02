import readDatabase from '../utils';

class StudentsController {
  static getAllStudents() {
    return readDatabase(process.argv[2])
      .then((data) => {
        let result = 'This is the list of our students';
        for (const [key] of Object.entries(data)) {
          result += `\nNumber of students in ${key}: ${data[key].length}. List: ${data[key].join(', ')}`;
        }

        return {
          status: 200,
          body: result,
        };
      })
      .catch(() => ({
        status: 500,
        body: 'Cannot load the database',
      }));
  }

  static getAllStudentsByMajor(major) {
    return readDatabase(process.argv[2])
      .then((data) => {
        if (Object.keys(data).includes(major)) {
          const result = `List: ${data[major].join(', ')}`;
          return {
            status: 200,
            body: result,
          };
        }
        return {
          status: 500,
          body: 'Major parameter must be CS or SWE',
        };
      })
      .catch(() => ({
        status: 500,
        body: 'Cannot load the database',
      }));
  }
}

module.exports = StudentsController;
