window.onload = function () {
    const button = $('INPUT#btn_translate');
    const hello = $('DIV#hello');
    const langInput = $('INPUT#language_code');
    let data;

    function sayHello () {
        lang = langInput.val();
        const link = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
        $.get(link, data, function (data) {
            hello.text(data.hello);
        })
    }

    button.click(function () {
        sayHello();
    });

    langInput.keypress(function (e) {
        if (e.keyCode === 13) {
            sayHello();
        }
    });
}
