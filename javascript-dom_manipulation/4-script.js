// Select the element with id 'add_item' and add a click event listener
document.querySelector('#add_item').addEventListener('click', function() {
  // Create a new li element
  const newItem = document.createElement('li');
  
  // Set the text content to 'Item'
  newItem.textContent = 'Item';
  
  // Select the ul element with class 'my_list' and append the new li
  document.querySelector('.my_list').appendChild(newItem);
});