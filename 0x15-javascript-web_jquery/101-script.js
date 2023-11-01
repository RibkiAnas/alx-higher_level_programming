// script that adds, removes and clears LI elements from a list when the user clicks

$(document).ready(() => {
  $('#add_item').click(() => {
    const li = $('<li>Item</li>');
    $('ul.my_list').append(li);
  });

  $('#remove_item').click(() => {
    const li = $('ul.my_list li:last-child');
    li.remove();
  });

  $('#clear_list').click(() => {
    $('ul.my_list').empty();
  });
});
