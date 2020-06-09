const link = 'https://fourtonfish.com/hellosalut/?lang=fr';
let data;
$.get(link, data, function (data) {
    $('DIV#hello').text(data.hello);
    console.log(data.hello);
})
