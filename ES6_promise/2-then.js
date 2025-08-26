function handleSuccess() {
  return {
    status: 200,
    body: 'success',
  };
}

function handleFailure() {
  return new Error();
}

export default function handleResponseFromAPI(promise) {
  return promise.then(
    handleSuccess, handleFailure,
  ).then(
    console.log('Got a response from the API'),
  );
}
