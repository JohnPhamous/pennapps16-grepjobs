(function($) {
  "use strict"; // Start of use strict

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Collapse the navbar when page is scrolled
  $(window).scroll(function() {
    if ($("#mainNav").offset().top > 100) {
      $("#mainNav").addClass("navbar-shrink");
    } else {
      $("#mainNav").removeClass("navbar-shrink");
    }
  });

})(jQuery); // End of use strict

function resizable (el, factor) {
      var int = Number(factor) || 7.7;
      function resize() {el.style.width = ((el.value.length+1) * int) + 'px'}
      var e = 'keyup,keypress,focus,blur,change'.split(',');
      for (var i in e) el.addEventListener(e[i],resize,false);
      resize();
}

var textSize = 20;

resizable(document.getElementById('job-title'),textSize);
resizable(document.getElementById('job-location'),textSize);
