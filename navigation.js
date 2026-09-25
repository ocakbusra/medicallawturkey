(function () {
  'use strict';

  var MOBILE_NAV_MAX_WIDTH = 1023;

  function initialiseContactTracking() {
    if (document.documentElement.dataset.contactTrackingReady === 'true') return;
    document.documentElement.dataset.contactTrackingReady = 'true';

    document.addEventListener('click', function (event) {
      var link = event.target.closest('a[href]');
      if (!link) return;

      var destination;
      try { destination = new URL(link.href, window.location.href); }
      catch (_) { return; }
      if (destination.hostname !== 'wa.me' && destination.hostname !== 'api.whatsapp.com') return;

      // A click shows contact intent. It is not a confirmed conversation or a qualified lead.
      var location = link.id === 'floatingWhatsapp' ? 'floating_button'
        : link.closest('footer') ? 'footer'
        : link.id === 'contactWhatsapp' ? 'contact_section'
        : 'page_content';
      try {
        if (typeof window.gtag === 'function') {
          window.gtag('event', 'whatsapp_click', {
            contact_channel: 'whatsapp',
            link_location: location
          });
        }
      } catch (_) { /* Never prevent the contact link from opening. */ }
    });
  }

  function initialiseNavigation() {
    var nav = document.getElementById('mainNav');
    var hamburger = document.getElementById('hamburgerBtn');
    var links = document.getElementById('navLinks');

    if (!nav || !hamburger || !links || nav.dataset.navigationReady === 'true') {
      return;
    }

    nav.dataset.navigationReady = 'true';
    hamburger.type = 'button';
    hamburger.setAttribute('aria-controls', 'navLinks');
    hamburger.setAttribute('aria-expanded', 'false');

    function setMenuOpen(isOpen, returnFocus) {
      links.classList.toggle('active', isOpen);
      hamburger.classList.toggle('active', isOpen);
      nav.classList.toggle('menu-open', isOpen);
      hamburger.setAttribute('aria-expanded', String(isOpen));

      if (returnFocus) {
        hamburger.focus();
      }
    }

    function menuIsOpen() {
      return links.classList.contains('active');
    }

    /*
     * Capture the click so this controller safely supersedes older inline
     * hamburger handlers that still exist on some legacy static pages.
     */
    hamburger.addEventListener('click', function (event) {
      event.preventDefault();
      event.stopImmediatePropagation();
      setMenuOpen(!menuIsOpen(), false);
    }, true);

    links.addEventListener('click', function (event) {
      if (event.target.closest('a')) {
        setMenuOpen(false, false);
      }
    });

    document.addEventListener('click', function (event) {
      if (menuIsOpen() && !nav.contains(event.target)) {
        setMenuOpen(false, false);
      }
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && menuIsOpen()) {
        setMenuOpen(false, true);
      }
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > MOBILE_NAV_MAX_WIDTH && menuIsOpen()) {
        setMenuOpen(false, false);
      }
    });

    function updateScrolledState() {
      nav.classList.toggle('scrolled', window.scrollY > 50);
    }

    window.addEventListener('scroll', updateScrolledState, { passive: true });
    updateScrolledState();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initialiseNavigation();
      initialiseContactTracking();
    }, { once: true });
  } else {
    initialiseNavigation();
    initialiseContactTracking();
  }
})();
