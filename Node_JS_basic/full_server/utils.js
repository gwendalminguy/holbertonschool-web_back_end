import fs from 'fs';

async function readDatabase(path) {
  const myPromise = new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      }
      resolve(data);
    });
  });

  return myPromise.then((data) => {
    const content = data.split('\n');
    const result = {};

    for (let i = 1; i < content.length; i += 1) {
      const [firstname, , , field] = content[i].split(',');

      if (!(field in result) && field) {
        result[field] = [];
      }

      if (field) {
        result[field].push(firstname);
      }
    }

    return result;
  });
}
export default readDatabase;
