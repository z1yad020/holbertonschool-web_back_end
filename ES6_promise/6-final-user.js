import uploadPhoto from './5-photo-reject';
import signUpUser from './4-user-promise';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const proms = [signUpUser(firstName, lastName), uploadPhoto(fileName)];
  return Promise.allSettled(proms);
}
