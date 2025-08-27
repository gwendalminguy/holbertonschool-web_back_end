import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

function handleResults(results) {
  const array = [];
  for (const element of results) {
    array.push({
      status: element.status,
      value: element.value,
    });
  }
  return array;
}

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promiseUser = signUpUser(firstName, lastName);
  const promisePhoto = uploadPhoto(fileName);

  return Promise.allSettled([promiseUser, promisePhoto])
    .then((results) => { return handleResults(results); });
}
