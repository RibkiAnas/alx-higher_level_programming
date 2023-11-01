// script that fetches and prints how to say “Hello” depending on the language

$(document).ready(() => {
  function translate () {
    const lang = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang;
    $.getJSON(url, (data) => {
      const hello = data.hello;
      $('#hello').text(hello);
    });
  }

  $('#btn_translate').click(translate);

  $('#language_code').keypress((event) => {
    if (event.which === 13) {
      translate();
    }
  });
});
