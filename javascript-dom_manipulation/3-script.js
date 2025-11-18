// Select the element with id 'toggle_header' and add a click event listener
document.querySelector('#toggle_header').addEventListener('click', function() {
  // Select the header element
  const header = document.querySelector('header');
  
  // Check if the header currently has the 'red' class
  if (header.classList.contains('red')) {
    // If red, remove it and add green
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    // If green (or any other class), remove green and add red
    header.classList.remove('green');
    header.classList.add('red');
  }
});
