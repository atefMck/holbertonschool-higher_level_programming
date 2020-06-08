const button = $('DIV#add_item');
const ul = $('UL.my_list');
button.click(function () {
    ul.append('<li>Item</li>');
})
