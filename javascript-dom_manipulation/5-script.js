// Select the element with id 'update_header' and add a click event listener
document.querySelector('#update_header').addEventListener('click', function() {
  // Select the header element and update its text content
  document.querySelector('header').textContent = 'New Header!!!';
});
