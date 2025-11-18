// Fetch the movies data from the Star Wars API
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())  // Convert the response to JSON
  .then(data => {
    // Select the ul element with id 'list_movies'
    const movieList = document.querySelector('#list_movies');
    
    // Loop through each movie in the results array
    data.results.forEach(movie => {
      // Create a new li element for each movie
      const listItem = document.createElement('li');
      
      // Set the text content to the movie title
      listItem.textContent = movie.title;
      
      // Append the li to the ul
      movieList.appendChild(listItem);
    });
  });