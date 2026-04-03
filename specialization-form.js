document.addEventListener("DOMContentLoaded", function () {
  const pageTitle = document.querySelector("section.hero h1, .spec-page-hero h1, h1");
  const pageName = pageTitle ? pageTitle.textContent.replace(/\s+/g, " ").trim() : "your procedure";

  const ctaTitle = document.querySelector(".specialization-cta-title");
  const ctaCopy = document.querySelector(".specialization-cta-copy");
  const formHeading = document.querySelector(".specialization-form-heading");
  const formCopy = document.querySelector(".specialization-form-copy");
  const submitBtn = document.querySelector(".specialization-submit-btn");
  const procedureInput = document.querySelector('input[name="procedure"]');

  if (ctaTitle) ctaTitle.textContent = "Request a Legal Assessment for " + pageName;
  if (ctaCopy) {
    ctaCopy.textContent =
      "Share the details of your " +
      pageName +
      " experience in Türkiye. Our team reviews these claims confidentially and responds within business hours.";
  }
  if (formHeading) formHeading.textContent = "Start Your " + pageName + " Case Review";
  if (formCopy) {
    formCopy.textContent =
      "Use the form below to request a confidential review related to " + pageName + ".";
  }
  if (submitBtn) submitBtn.textContent = "Request " + pageName + " Review";
  if (procedureInput) procedureInput.value = pageName;

  document.querySelectorAll(".custom-contact-form").forEach(function (form) {
    form.addEventListener("submit", async function (e) {
      e.preventDefault();

      const btn = form.querySelector(".btn-submit");
      const msgBox = form.querySelector(".form-msg");
      const originalBtnText = btn.textContent;

      btn.textContent = "Sending...";
      btn.disabled = true;
      msgBox.style.display = "none";

      const formData = new FormData(form);
      formData.append("access_key", "0926a3cb-6d91-4e4d-85c6-1302d58548bf");
      formData.append("subject", "Assessment Request - " + pageName);
      formData.append("from_name", "Medical Law Türkiye Website");

      const phoneVal = (formData.get("phonecode") || "") + " " + (formData.get("phone") || "");
      formData.set("phone", phoneVal.trim());
      formData.delete("phonecode");

      try {
        const response = await fetch("https://api.web3forms.com/submit", {
          method: "POST",
          body: formData
        });

        const result = await response.json();

        if (result.success) {
          form.reset();
          if (procedureInput) procedureInput.value = pageName;
          msgBox.style.display = "block";
          msgBox.style.color = "#0E7490";
          msgBox.textContent = "Thank you. Your request has been sent successfully.";
        } else {
          msgBox.style.display = "block";
          msgBox.style.color = "#DC2626";
          msgBox.textContent = "An error occurred while submitting: " + result.message;
        }
      } catch (error) {
        msgBox.style.display = "block";
        msgBox.style.color = "#DC2626";
        msgBox.textContent = "Network error. Please try again or contact us via WhatsApp.";
      } finally {
        btn.textContent = originalBtnText;
        btn.disabled = false;
      }
    });
  });
});
