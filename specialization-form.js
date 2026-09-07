(function () {
  "use strict";

  function initializeForms() {
    const endpoint = "https://api.web3forms.com/submit";
    const pageName = document.querySelector("h1")?.textContent.replace(/\s+/g, " ").trim() || "Legal assessment";

    document.querySelectorAll(".custom-contact-form").forEach(function (form) {
      if (form.dataset.web3formsReady) return;
      form.dataset.web3formsReady = "true";

      const button = form.querySelector('.btn-submit');
      const status = form.querySelector('.form-msg');
      const controls = Array.from(form.querySelectorAll('input:not([type="hidden"]), textarea, select'));
      let submitting = false;

      function phoneNumber() {
        const number = (form.elements.namedItem("phone")?.value || "").trim();
        const code = (form.elements.namedItem("phonecode")?.value || "").trim();
        if (!number) return "";
        if (/^(\+|00)/.test(number)) return number.replace(/^00/, "+");
        return [code, number].filter(Boolean).join(" ");
      }

      function validate(control, trim) {
        if (!['text', 'tel', 'email', 'textarea'].includes(control.type)) return;
        if (trim) control.value = control.value.trim();
        const value = control.value.trim();
        control.setCustomValidity("");
        if (control.required && !value) {
          control.setCustomValidity("Please complete this field.");
        } else if (control.name === "phone" && value) {
          const digits = phoneNumber().replace(/\D/g, "");
          if (!/^\+?[\d\s().-]+$/.test(value) || digits.length < 7 || digits.length > 15) {
            control.setCustomValidity("Please enter a phone number with 7–15 digits, including the country code when needed.");
          }
        } else if (control.name === "phonecode" && value && !/^\+?[1-9]\d{0,2}$/.test(value)) {
          control.setCustomValidity("Please enter a country code such as +44.");
        }
      }

      controls.forEach(function (control) {
        control.addEventListener("input", function () {
          validate(control, false);
          if (control.name === "phonecode") {
            const phone = form.elements.namedItem("phone");
            if (phone) validate(phone, false);
          }
        });
        control.addEventListener("blur", function () { validate(control, true); });
      });

      function showStatus(message, error) {
        status.style.display = "block";
        status.style.color = error ? "#DC2626" : "#0E7490";
        status.textContent = message;
      }

      form.addEventListener("submit", async function (event) {
        event.preventDefault();
        if (submitting) return;
        controls.forEach(function (control) { validate(control, true); });
        if (!form.reportValidity()) return;

        submitting = true;
        const originalText = button.textContent;
        button.disabled = true;
        button.textContent = "Sending…";
        form.setAttribute("aria-busy", "true");
        showStatus("Sending your request…", false);

        const data = new FormData(form);
        const formType = form.dataset.type || "contact";
        data.set("subject", formType === "checklist" ? "Self-assessment request" : "Assessment Request - " + pageName);
        data.set("from_name", "Medical Law Türkiye Website");
        data.set("page_url", window.location.origin + window.location.pathname);
        data.set("form_type", formType);
        data.set("phone", phoneNumber());
        data.delete("phonecode");

        if (formType === "checklist") {
          const selected = Array.from(document.querySelectorAll('.check-box.checked')).map(function (box) {
            return box.closest('.check-item').querySelector('.check-text').textContent.trim();
          });
          if (selected.length) {
            data.set("message", (data.get("message") || "") + "\n\n--- Selected Assessment Indicators ---\n- " + selected.join("\n- "));
          }
        }

        const controller = new AbortController();
        const timeout = window.setTimeout(function () { controller.abort(); }, 20000);
        try {
          const response = await fetch(endpoint, { method: "POST", body: data, signal: controller.signal });
          const result = await response.json();
          if (!response.ok || result.success !== true) {
            showStatus("We couldn't send your request. Please try again or contact us via WhatsApp.", true);
            return;
          }

          form.reset();
          controls.forEach(function (control) { control.setCustomValidity(""); });
          showStatus("Thank you. Your assessment request has been sent successfully.", false);
          form.dispatchEvent(new CustomEvent("mlt:form-success", { bubbles: true }));
          // Send only the form category to analytics, never enquiry details or contact information.
          try {
            if (typeof window.gtag === "function") window.gtag("event", "generate_lead", { form_type: formType });
          } catch (_) { /* Analytics must not change the submission result. */ }
        } catch (error) {
          showStatus(error.name === "AbortError"
            ? "Your request could not be confirmed in time. Please contact us via WhatsApp before resending."
            : "Your request could not be confirmed. Please check your connection or contact us via WhatsApp.", true);
        } finally {
          window.clearTimeout(timeout);
          submitting = false;
          button.disabled = false;
          button.textContent = originalText;
          form.removeAttribute("aria-busy");
        }
      });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initializeForms);
  else initializeForms();
})();
