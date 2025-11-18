// Wait for the DOM to be fully loaded before running the code
document.addEventListener('DOMContentLoaded', function() {
  // Fetch the translation from the API
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())  // Convert the response to JSON
    .then(data => {
      // Display the hello translation in the element with id 'hello'
      document.querySelector('#hello').textContent = data.hello;
    });
});
