window.onload = function () {
    const button = $('INPUT#btn_translate');
    const hello = $('DIV#hello');
    let data;

    button.click(function () {
        const lang = $('INPUT#language_code').val();
        const link = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
        $.get(link, data, function (data) {
            hello.text(data.hello);
        })
    });
}
