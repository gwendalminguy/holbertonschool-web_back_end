import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promiseUser = signUpUser(firstName, lastName);
  const promisePhoto = uploadPhoto(fileName);

  return Promise.allSettled([promiseUser, promisePhoto])
    .then((result) => { return result.map((element) => {element.status, element.value}) });
}
