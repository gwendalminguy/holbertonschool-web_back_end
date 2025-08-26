function successMessage() {
  console.log('Success');
}

function failureMessage() {
  console.log('Failure');
}

export default function getResponseFromAPI() {
  return new Promise(successMessage, failureMessage);
}
