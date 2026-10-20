(function () {
  'use strict';

  var review = document.querySelector('details.glossary-hero-form');
  if (review) {
    var mobile = window.matchMedia('(max-width: 900px)');
    function updateReviewLayout() {
      review.open = !mobile.matches;
    }
    updateReviewLayout();
    mobile.addEventListener('change', updateReviewLayout);
  }

  // Recover once from a transient image/CDN failure, without a reload loop.
  document.querySelectorAll('.glossary-figure img').forEach(function (image) {
    function retryImage() {
      if (image.dataset.imageRetried === 'true') return;
      image.dataset.imageRetried = 'true';
      var retryUrl = new URL(image.src, document.baseURI);
      retryUrl.searchParams.set('image-retry', '1');
      window.setTimeout(function () { image.src = retryUrl.href; }, 300);
    }
    image.addEventListener('error', retryImage, { once: true });
    if (image.complete && !image.naturalWidth) retryImage();
  });
})();
