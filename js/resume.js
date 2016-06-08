$(document).ready(function() {
    $('.hide td, th.sub-sect2').hide();
    $('td.toggle, td.dum').show();
    $('th.sub-sect, td.toggle, td.togoff').click(function() {
       $(this).parents('table').find('td, th.sub-sect2').toggle();
    }); 
});