window.onload = function () {
    const add = $('DIV#add_item');
    const remove = $('DIV#remove_item');
    const clear = $('DIV#clear_list');
    const ul = $('UL.my_list');

    add.click(function () {
        ul.append('<li>Item</li>');
    });

    remove.click(function () {
        let lastLi = $('UL.my_list li').last();
        lastLi.remove();
    });

    clear.click(function () {
        let li = $('UL.my_list li');
        li.remove();
    });
}

    
