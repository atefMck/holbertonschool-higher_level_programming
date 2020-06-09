const char = $('DIV#character');
const link = 'https://swapi-api.hbtn.io/api/films/?format=json';
let data;
$.get(link, data, function (data) {
    const name = data.name;
    char.text(name);
})
