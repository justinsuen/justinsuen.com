jQuery(document).ready(function($) {
  $(document).on("scroll", function() {
    var windscroll = $(document).scrollTop();
    $('body section').each(function(i, obj) {
      if ($(obj).position().top <= windscroll + 150) {
        $('.navbar-item.active').removeClass('active');
        $('.navbar-item[data-scroll=' + obj.id + ']').addClass('active');
      }
    });

    if ($("#splash").position().top <= windscroll + 150)
      $("#navbar").css('padding', '50px 60px 30px 60px');

    if ($("#about").position().top <= windscroll + 400)
      $("#navbar").css('padding', '10px 60px');
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

  $('.mobile-navbar-links a.navbar-item').on('click touchend', function() {
    $('.mobile-navbar-links').toggleClass('hide');
  });
});

function navShow() {
  $('.mobile-navbar-links').toggleClass('hide');
}
