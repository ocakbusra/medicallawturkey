(function () {
  'use strict';

  const receiptKey = 'mlt:assessment-confirmation';
  const receiptLifetime = 15 * 60 * 1000;
  let receipt = null;
  try {
    const saved = JSON.parse(sessionStorage.getItem(receiptKey));
    const age = saved && Date.now() - saved.receivedAt;
    if (saved && typeof saved.receivedAt === 'number' && Number.isFinite(age) && age >= 0 && age < receiptLifetime) {
      receipt = saved;
    } else sessionStorage.removeItem(receiptKey);
  } catch (_) { /* Show an anonymous confirmation when storage is unavailable. */ }

  const justReceived = window.location.hash === '#received';
  if (justReceived || receipt) {
    document.getElementById('enquiryIntro').hidden = true;
    document.getElementById('confirmationContent').hidden = false;
    document.getElementById('confirmationSteps').hidden = false;
    document.getElementById('confirmationEyebrow').hidden = false;
    document.title = 'Thank you | Medical Law Türkiye';
    const name = typeof receipt?.firstName === 'string' ? receipt.firstName.trim().slice(0, 80) : '';
    document.getElementById('confirmationTitle').textContent = name ? 'Thank you, ' + name + '.' : 'Thank you for getting in touch.';
  }

  if (justReceived) {
    try { history.replaceState(null, '', window.location.pathname); } catch (_) { /* Optional URL cleanup. */ }
  }

  // Keep the greeting only briefly in this tab, including when a page stays open.
  if (receipt) {
    window.setTimeout(function () {
      try { sessionStorage.removeItem(receiptKey); } catch (_) { /* Storage may be blocked. */ }
      document.getElementById('confirmationTitle').textContent = 'Thank you for getting in touch.';
    }, Math.max(0, receipt.receivedAt + receiptLifetime - Date.now()));
  }
})();
