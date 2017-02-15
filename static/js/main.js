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

  $('.mobile-navbar-links a.navbar-item').on('click', function() {
    $('.mobile-navbar-links').toggleClass('hide');
  });

  // Google Analytics
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-92073504-1', 'auto');
  ga('send', 'pageview');
});

function navShow() {
  $('.mobile-navbar-links').toggleClass('hide');
}
