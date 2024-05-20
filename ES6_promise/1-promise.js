export default function getFullResponseFromAPI(success) {
  if (success) {
    return new Promise((fulfill) => {
      fulfill({ status: 200, body: 'Success' });
    });
  }
  return new Promise((fulfill, reject) => {
    reject(new Error('The fake API is not working currently'));
  });
}
