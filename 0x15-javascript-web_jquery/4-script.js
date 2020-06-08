const headerButton = $('DIV#toggle_header');
const header = $('header');
headerButton.click(function () {
    let attr = header.attr('class');
    console.log(attr);
    if (attr == 'red') {
        header.removeClass('red');
        header.addClass('green');
    } else {
        header.removeClass('green');
        header.addClass('red');
    } 
})
