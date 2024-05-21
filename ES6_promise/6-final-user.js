import uploadPhoto from './5-photo-reject';
import signUpUser from './4-user-promise';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const proms = [uploadPhoto(firstName, lastName), signUpUser(fileName)];
  return Promise.allSettled(proms);
}
