jQuery(document).ready(function($) {
  $(document).on("scroll", function() {
    var windscroll = $(document).scrollTop();
    $('body section').each(function(i, obj) {
      if ($(obj).position().top <= windscroll + 150) {
        $('.navbar-links a.active').removeClass('active');
        $('.navbar-links a[data-scroll=' + obj.id + ']').addClass('active');
      }
    });

    // Get background overlay to change color
    if ($("#splash").position().top <= windscroll + 150) {
      $(".overlay").css('background-color', 'transparent');
      $("#navbar").css('padding', '50px 60px 30px 60px');
    }

    if ($("#about").position().top <= windscroll + 400) {
      $("#navbar").css('padding', '10px 60px');
      $(".overlay").css('background-color', '#B8F2FF');
    }

    if ($("#projects").position().top <= windscroll + 150)
      $(".overlay").css('background-color', '#B5FF75');

    if ($("#contact").position().top <= windscroll + 150)
      $(".overlay").css('background-color', '#FEF284');
  });

  $('a.smoothscroll').click(function() {
    var target = $(this.hash);
    target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');

    if (target.length) {
      $('html, body').animate({
        scrollTop: target.offset().top
      }, 500);
      return false;
    }
  });
});
