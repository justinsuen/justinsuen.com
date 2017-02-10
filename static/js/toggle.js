function toggle(id) {
    var element = document.getElementById(id);

    if ( element.style.display != 'none' ) {
        element.style.display = 'none';
    }
    else {

        element.style.display = '';
    }
}
