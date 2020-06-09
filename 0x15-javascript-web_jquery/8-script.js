const ul = $('UL#list_movies');
const link = 'https://swapi-api.hbtn.io/api/films/?format=json';
let data;
$.get(link, data, function (data) {
    const result = data.results;
    for (let i = 0; i < result.length; i++) {
        let liTitle = '<li>' + result[i].title + '</li>'
        ul.append(liTitle);
    }
})
