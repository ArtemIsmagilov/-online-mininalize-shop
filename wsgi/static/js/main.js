function change_mode() {
    const schema = document.querySelector("html");
    if (schema.getAttribute("data-bs-theme") == "dark") {
        schema.removeAttribute("data-bs-theme");
    }
    else {
        schema.setAttribute("data-bs-theme", "dark");
    }

}

function increment_inventory(row_id) {
    const quantity = document.getElementById(row_id);
    var counter = parseInt(quantity.innerHTML);
    if (counter < 999999) {
        quantity.innerHTML = counter + 1;
    }
}

function decrement_inventory(row_id) {
    const quantity = document.getElementById(row_id);
    var counter = parseInt(quantity.innerHTML);
    if (counter > 0) {
        quantity.innerHTML = counter - 1;
    }

}



function load_counts(block_id, count) {
    function update() {
        if (step < count) {
            quantity.innerHTML = step;
            step++;
            if (count - step < 10) {
                delay += 50;
            }
            setTimeout(update, delay);
        }
    }

    const quantity = document.getElementById(block_id);
    if (count > 9999){
        return;
    }

    let step = 0;
    var delay = 10;

    update();
}

function load_preview_digits() {
    load_counts("count_income_id", 150);
    load_counts("count_employ_id", 100);
    load_counts("count_vacancy_id", 54);
    load_counts("count_trust_id", 15);
    load_counts("count_sale_id", 10);
}

function short_long_cart_text() {
    var elements = document.getElementsByClassName('card-text');
    for (var i = 0; i < elements.length; i++) {
        if (elements[i].innerHTML.length > 50) {
            elements[i].innerHTML = elements[i].innerHTML.substring(0, 50) + '...';
        }
    }
}
