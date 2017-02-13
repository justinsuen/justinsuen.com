jQuery(document).ready($ => {
  $(document).on("scroll", () => {
    let windscroll = $(document).scrollTop();
    $('body section').each((i, obj) => {
      if ($(obj).position().top <= windscroll + 150) {
        $('.navbar-links a.active').removeClass('active');
        $('.navbar-links a[data-scroll=' + obj.id + ']').addClass('active');
      }
    });
  });

  $('a.smoothscroll').click(function() {
    let target = $(this.hash);
    target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');

    if (target.length) {
      $('html, body').animate({
        scrollTop: target.offset().top
      }, 500);
      return false;
    }
  });
});
