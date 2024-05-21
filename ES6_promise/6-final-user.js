import uploadPhoto from './5-photo-reject';
import signUpUser from './4-user-promise';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const proms = [uploadPhoto(fileName), signUpUser(firstName, lastName)];
  return Promise.allSettled(proms);
}
