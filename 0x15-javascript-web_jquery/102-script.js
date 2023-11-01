// script that fetches and prints how to say “Hello” depending on the language

$(document).ready(() => {
  $('#btn_translate').click(() => {
    const languageCode = $('#language_code').val();
    const url = `https://fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
    $.getJSON(url, (data) => {
      $('#hello').text(data.hello);
    });
  });
});
