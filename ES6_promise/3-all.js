import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([valueA, valueB]) => { console.log(`${valueA.body} ${valueB.firstName} ${valueB.lastName}`); })
    .catch(() => { console.log('Signup system offline'); });
}
