import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const promiseA = uploadPhoto();
  const promiseB = createUser();

  return Promise.all(
    [promiseA, promiseB],
  ).then(
    ([valueA, valueB]) => { console.log(valueA.body, valueB.firstName, valueB.lastName); },
  ).catch(
    () => { console.log('Signup system offline'); },
  );
}
