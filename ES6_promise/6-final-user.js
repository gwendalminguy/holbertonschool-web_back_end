import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleResults(results) {
  const array = [];
  for (const element of results) {
    if (element.value) {
      array.push({
        status: element.status,
        value: element.value,
      });
    } else {
      array.push({
        status: element.status,
        value:  `${element.reason.name}: ${element.reason.message}`,
      });
    }
  }
  return array;
}

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promiseUser = signUpUser(firstName, lastName);
  const promisePhoto = uploadPhoto(fileName);

  return Promise.allSettled([promiseUser, promisePhoto])
    .then((results) => handleResults(results));
}
