// Select the element with id 'red_header' and add a click event listener
document.querySelector('#red_header').addEventListener('click', function() {
  // When clicked, select the header element and update its text color to red
  document.querySelector('header').style.color = '#FF0000';
});
