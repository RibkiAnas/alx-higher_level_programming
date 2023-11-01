// script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello

$(document).ready(() => {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    const hello = data.hello;
    $('#hello').text(hello);
  });
});
