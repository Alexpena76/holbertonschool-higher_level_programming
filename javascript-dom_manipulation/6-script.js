// Fetch the character data from the Star Wars API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())  // Convert the response to JSON
  .then(data => {
    // Display the character name in the element with id 'character'
    document.querySelector('#character').textContent = data.name;
  });