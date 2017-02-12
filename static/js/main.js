$(document).ready(function() {
  $(document).on("scroll", function() {
    let windscroll = $(document).scrollTop();
    $('body section').each((i, obj) => {
      if ($(obj).position().top <= windscroll + 150) {
        $('.navbar-links a.active').removeClass('active');
        $('.navbar-links a[data-scroll=' + obj.id + ']').addClass('active');
      }
    });
  });
});
