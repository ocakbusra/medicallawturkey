import re

file_path = "arm-lift-malpractice.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# ═══════════════════════════════════════════════════════
# 1. REPLACE THE CONTENT SECTION (lines 352-532)
# ═══════════════════════════════════════════════════════

new_content_section = """
  <!-- ── CONTENT ── -->
  <section id="content" style="background: var(--off-white); padding-top: 4rem; padding-bottom: 2rem;">
    <div class="section-inner" style="max-width: 820px; margin: 0 auto;">

      <!-- ── TABLE OF CONTENTS ── -->
      <div class="alp-toc">
        <div class="alp-toc-label">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="2"><path d="M4 6h16M4 12h10M4 18h14"/></svg>
          <span>In This Guide</span>
        </div>
        <ol class="alp-toc-list">
          <li><a href="#alp-what-is">What Is Arm Lift Malpractice?</a></li>
          <li><a href="#alp-why-turkey">Why Türkiye — And Where It Goes Wrong</a></li>
          <li><a href="#alp-complications">Recognizing Severe Complications</a></li>
          <li><a href="#alp-legal">The Turkish Legal Framework</a></li>
          <li><a href="#alp-consent">Informed Consent Requirements</a></li>
          <li><a href="#alp-process">Step-by-Step Legal Process</a></li>
          <li><a href="#alp-compensation">Types of Compensation</a></li>
          <li><a href="#alp-statute">Statute of Limitations</a></li>
          <li><a href="#alp-help">How We Can Help</a></li>
        </ol>
      </div>

      <!-- ── ARTICLE CARD ── -->
      <article class="alp-article">

        <!-- ── KEY TAKEAWAYS BOX ── -->
        <div class="alp-takeaways">
          <div class="alp-takeaways-header">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--teal)" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
            <h3>Key Takeaways</h3>
          </div>
          <ul class="alp-takeaway-list">
            <li>
              <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
              <span>Arm lift (brachioplasty) is classified as a <strong>"Contract for Work"</strong> under Turkish law — surgeons guarantee a specific aesthetic result.</span>
            </li>
            <li>
              <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
              <span>International patients have <strong>full legal rights</strong> in Türkiye — identical to Turkish citizens.</span>
            </li>
            <li>
              <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
              <span>You do <strong>not</strong> need to travel back to Türkiye — a Power of Attorney (Vekaletname) enables remote representation.</span>
            </li>
            <li>
              <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
              <span>Compensation covers surgery costs, revision surgeries, lost wages, and <strong>moral damages</strong> for pain and suffering.</span>
            </li>
            <li>
              <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
              <span>The statute of limitations is <strong>5 years</strong> (up to 20 years for gross negligence).</span>
            </li>
          </ul>
        </div>

        <!-- ── INTRO ── -->
        <p class="alp-body">
          Arm lift surgery, medically referred to as brachioplasty, is a highly specialized cosmetic procedure aimed at reshaping the under portion of the upper arm, from the armpit region to the elbow. By removing excess skin and fat, the surgery results in a more toned, proportionate, and youthful appearance. Every year, thousands of international patients, particularly from the UK, the US, Europe, and the Middle East, travel to Türkiye for this transformative procedure. Turkish clinics in Istanbul, Antalya, Izmir, and Ankara are globally recognized for their modern facilities, highly skilled surgeons, and cost-effective medical tourism packages.
        </p>
        <p class="alp-body">
          However, as the volume of cosmetic surgeries increases, so does the unfortunate incidence of <strong>medical malpractice and substandard care</strong>. While most procedures are successful, some patients awaken to a nightmare: severe scarring, permanent nerve damage, striking asymmetry, or massive infections. When an arm lift goes wrong due to the negligence of a clinic or a surgeon, it ceases to be a mere cosmetic disappointment—it becomes a profound physical, emotional, and financial trauma. Understanding your legal rights under Turkish law is the first critical step toward obtaining justice and fair compensation. This comprehensive guide serves as an authoritative resource on arm lift malpractice in Türkiye, specifically designed for international patients seeking legal recourse.
        </p>

        <!-- ── DEFINITION BOX ── -->
        <div class="alp-highlight-box" id="alp-what-is">
          <div class="alp-highlight-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--navy)" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
          </div>
          <h3 class="alp-highlight-title">What is Arm Lift (Brachioplasty) Malpractice?</h3>
          <p class="alp-body" style="margin-bottom: 1rem;">
            Medical malpractice in the context of an arm lift occurs when a surgeon, medical staff, or clinic deviates from the universally accepted standard of medical care, directly resulting in harm to the patient. It is absolutely crucial to differentiate between an "expected, inherent risk" of surgery (such as standard scar maturation or temporary swelling) and actual "medical negligence."
          </p>
          <p class="alp-body" style="margin-bottom: 0;">
            Malpractice is not just about being dissatisfied with a minor aesthetic flaw. It involves a breach of the duty of care. This breach could happen during the pre-operative consultation (e.g., failure to obtain informed consent), during the surgery itself (e.g., severing a major nerve, excising too much skin), or in the post-operative period (e.g., discharging a patient with an active, unmanaged infection). Under Turkish jurisprudence, aesthetic surgeons are held to a particularly high standard because the procedures are elective, and the primary goal is the enhancement of the patient's physical appearance.
          </p>
        </div>

        <!-- ── WHY TÜRKIYE ── -->
        <h2 class="alp-section-title" id="alp-why-turkey">Why Do International Patients Choose Türkiye, and Where Does It Go Wrong?</h2>
        <p class="alp-body">
          Türkiye has positioned itself as the undisputed capital of health tourism in Europe and the Middle East. The country boasts dozens of JCI-accredited hospitals, state-of-the-art medical equipment, and internationally trained plastic surgeons. The allure is undeniable: patients can receive VIP treatment, luxury hotel stays, and world-class surgery at a fraction of the cost they would incur in London, New York, or Berlin.
        </p>
        <p class="alp-body">
          So, where does the system break down? The explosive growth of the medical tourism sector has led to the proliferation of aggressive "health tourism agencies" acting as middlemen. Sometimes, these agencies prioritize profit over patient safety. Patients might be consulted entirely over WhatsApp, without ever meeting the surgeon until the morning of the operation. In severe cases of malpractice, patients discover that their procedure was performed not by the "celebrity surgeon" advertised on Instagram, but by an inexperienced junior doctor, or even an unlicensed technician. Furthermore, the "fly-in, fly-out" model of medical tourism leaves little to no room for adequate post-operative care. When complications like wound dehiscence (surgical incisions reopening) or necrosis occur, the patient is often already on a plane back home, miles away from the treating physician.
        </p>

        <!-- ── COMPLICATIONS ── -->
        <h2 class="alp-section-title" id="alp-complications">Recognizing Arm Lift Malpractice: Common Severe Complications</h2>
        <p class="alp-body">
          Every surgical procedure carries risks, but when these complications arise from sheer negligence, lack of skill, or improper surgical technique, it crosses the line into medical malpractice. Below is a detailed analysis of the most frequent complications that constitute grounds for a malpractice lawsuit in Türkiye:
        </p>

        <div class="alp-complication-grid">

          <div class="alp-complication-card">
            <div class="alp-complication-num">01</div>
            <h4 class="alp-complication-title">Severe, Unexpected, or Disfiguring Scarring</h4>
            <p class="alp-body" style="margin-bottom:0">
              By definition, an arm lift requires an incision, which means a scar is inevitable. A standard brachioplasty scar runs on the inside or the back of the arm. However, a competent surgeon uses meticulous suturing techniques to ensure the scar heals as a thin, inconspicuous line. Malpractice occurs when the surgeon places the incision poorly, making it highly visible from the front or back, or uses rough, improper suturing techniques leading to massive, raised keloid or hypertrophic scars. Furthermore, if the surgeon removes excessive tension from the skin (closing the wound too tightly), the scar can stretch excessively or cause the wound to burst open entirely (dehiscence).
            </p>
          </div>

          <div class="alp-complication-card">
            <div class="alp-complication-num">02</div>
            <h4 class="alp-complication-title">Noticeable and Permanent Asymmetry</h4>
            <p class="alp-body" style="margin-bottom:0">
              The human body is not perfectly symmetrical, and minor discrepancies between the left and right arms are normal. However, glaring asymmetry—where one arm is significantly thicker, longer, or shaped differently than the other—is a hallmark of a botched surgery. This typically happens when the surgeon fails to measure and mark the patient accurately before the operation, or when different amounts of fat and skin are arbitrarily excised from each limb. When asymmetry is so severe that it is immediately noticeable to the naked eye, the patient may have a strong legal claim for breach of the aesthetic contract.
            </p>
          </div>

          <div class="alp-complication-card">
            <div class="alp-complication-num">03</div>
            <h4 class="alp-complication-title">Nerve Damage, Numbness, and Loss of Motor Function</h4>
            <p class="alp-body" style="margin-bottom:0">
              The inner arm is a highly complex anatomical zone housing major neurovascular bundles, including the medial antebrachial cutaneous nerve. If a surgeon is careless, inexperienced, or rushes the procedure, they can accidentally sever or heavily compress these vital nerves. While temporary numbness around the incision line is expected, permanent loss of sensation radiating down to the forearm or hand, chronic shooting nerve pain (neuropathy), or a complete loss of motor function (inability to move the fingers or wrist) points directly to surgical negligence. Such catastrophic outcomes drastically alter the patient's quality of life and earning capacity, warranting significant compensation.
            </p>
          </div>

          <div class="alp-complication-card">
            <div class="alp-complication-num">04</div>
            <h4 class="alp-complication-title">Severe Infections and Skin Necrosis</h4>
            <p class="alp-body" style="margin-bottom:0">
              Post-operative infections can occur in any hospital worldwide. However, if an infection arises because the clinic's operating theater lacked basic sterilization, or because the surgeon used contaminated instruments, it is malpractice. More alarmingly, poor surgical technique can destroy the blood supply to the skin flaps created during the arm lift. Without adequate blood flow, the tissue dies—a condition known as necrosis. Necrosis leaves the patient with gaping black wounds, requires painful debridement (surgical removal of dead tissue), and necessitates complex skin grafting procedures, leaving horrific secondary scars.
            </p>
          </div>

          <div class="alp-complication-card">
            <div class="alp-complication-num">05</div>
            <h4 class="alp-complication-title">Contour Irregularities and "Dog Ears"</h4>
            <p class="alp-body" style="margin-bottom:0">
              When an arm lift is performed in conjunction with aggressive liposuction, the surgeon must be highly skilled to ensure a smooth, even contour. A botched procedure often results in a lumpy, bumpy, and uneven skin surface. Additionally, poor incision planning can lead to the formation of "dog ears"—unsightly puckers of excess skin and fat that bunch up at the ends of the incision lines, usually near the armpit or elbow. These deformities almost always require a second, expensive revision surgery to correct.
            </p>
          </div>

        </div>

        <!-- ── MID-CONTENT CTA ── -->
        <div class="alp-inline-cta">
          <div class="alp-inline-cta-text">
            <h4>Have You Experienced Complications After an Arm Lift?</h4>
            <p>Our legal team offers a free, confidential case assessment for international patients.</p>
          </div>
          <a href="index.html#contact" class="alp-inline-cta-btn">Request Free Case Review</a>
        </div>

        <!-- ── LEGAL FRAMEWORK ── -->
        <h2 class="alp-section-title" id="alp-legal">The Turkish Legal Framework for Aesthetic Malpractice</h2>
        <p class="alp-body">
          Navigating the legal landscape in a foreign country can be intimidating. However, the Turkish legal system is well-developed, highly structured, and offers robust protections for patients—regardless of their nationality. In Türkiye, medical malpractice claims, particularly those involving elective cosmetic surgeries like an arm lift, are evaluated under very specific legal doctrines.
        </p>

        <div class="alp-legal-cards">

          <div class="alp-legal-card">
            <div class="alp-legal-card-header">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--teal)" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
              <h4>Contract for Work (Eser Sözleşmesi)</h4>
            </div>
            <p class="alp-body" style="margin-bottom: 1rem;">
              In traditional therapeutic medicine (e.g., treating a heart attack), the doctor-patient relationship is governed by a mandate contract (vekalet sözleşmesi), meaning the doctor promises to use their best efforts, but does not guarantee a cure. However, the Turkish Court of Cassation (Yargıtay) has established a crucial precedent for aesthetic surgeries. Since a brachioplasty is elective and performed primarily to achieve a specific aesthetic result, the relationship is classified as a "Contract for Work" (Eser Sözleşmesi) under the Turkish Code of Obligations.
            </p>
            <p class="alp-body" style="margin-bottom: 0;">
              This classification is incredibly powerful for the patient. It means the surgeon is legally bound to produce the specific aesthetic result that was promised and agreed upon during consultations. If the surgeon promised a smooth contour and a hidden scar, but delivered a disfigured, asymmetrical arm with massive keloids, the surgeon has fundamentally breached the contract. The surgeon cannot simply defend themselves by saying "I tried my best"; they must answer for the failure to deliver the agreed-upon "work."
            </p>
          </div>

          <div class="alp-legal-card">
            <div class="alp-legal-card-header">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--teal)" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              <h4>Tort Liability (Haksız Fiil)</h4>
            </div>
            <p class="alp-body" style="margin-bottom: 0;">
              In addition to breaching a contract, medical negligence constitutes a "tort"—a civil wrong that causes harm. Under Turkish tort law, if a surgeon acts negligently, recklessly, or without the requisite professional skill, they are liable for the physical and psychological damages inflicted on the patient. To succeed in a tort claim, your legal team must prove four elements: an unlawful act (the negligent surgery), fault (the doctor's deviation from medical standards), damage (your physical injuries and financial losses), and a causal link (proving the doctor's actions directly caused your injuries).
            </p>
          </div>

          <div class="alp-legal-card">
            <div class="alp-legal-card-header">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--teal)" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>
              <h4>Consumer Protection Law (Tüketicinin Korunması Hakkında Kanun)</h4>
            </div>
            <p class="alp-body" style="margin-bottom: 0;">
              Because an arm lift is deemed a "Contract for Work," the patient is legally classified as a "consumer," and the doctor or clinic is the "service provider." Consequently, these malpractice cases are heard in specialized Consumer Courts (Tüketici Mahkemeleri) in Türkiye. Consumer law inherently favors the protection of the weaker party—the patient. It places a strict burden of proof on the clinic to demonstrate that they provided flawless service, adequate warnings, and fulfilled their contractual duties.
            </p>
          </div>

        </div>

        <!-- ── INFORMED CONSENT ── -->
        <h2 class="alp-section-title" id="alp-consent">The Crucial Role of Informed Consent in Aesthetic Procedures</h2>
        <p class="alp-body">
          One of the most frequent violations in medical tourism is the lack of proper, legally valid "Informed Consent" (Aydınlatılmış Onam). Turkish law is exceptionally strict regarding the patient's right to information. Before an arm lift, the surgeon is legally obligated to personally inform you, in a language you fully understand, about the entire scope of the procedure.
        </p>
        <p class="alp-body">
          This is not a mere formality where you sign a 30-page document in a rushed hospital lobby five minutes before anesthesia. The law requires the doctor to explain:
        </p>

        <ul class="alp-icon-list">
          <li>
            <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
            <span>The exact technique to be used and the expected aesthetic outcome.</span>
          </li>
          <li>
            <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
            <span>The realistic size, shape, and placement of the permanent scars.</span>
          </li>
          <li>
            <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
            <span>All potential risks, ranging from minor swelling to catastrophic nerve damage or necrosis.</span>
          </li>
          <li>
            <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
            <span>Alternative treatment options (such as non-surgical fat reduction).</span>
          </li>
          <li>
            <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
            <span>The likelihood of needing future revision surgeries.</span>
          </li>
        </ul>

        <!-- ── QUOTE BLOCK ── -->
        <blockquote class="alp-quote">
          <p>If a clinic forced you to sign consent forms written entirely in Turkish, or if the "consent" was gathered by a sales representative over WhatsApp rather than the operating surgeon, the consent is <strong>legally void</strong>.</p>
        </blockquote>

        <p class="alp-body">
          Under Turkish Supreme Court rulings, if a complication occurs—even an expected one—but the patient was never adequately warned about it beforehand, the doctor is deemed 100% liable for the damages, regardless of whether the surgery itself was performed flawlessly.
        </p>

        <!-- ── STEP-BY-STEP LEGAL PROCESS (TIMELINE) ── -->
        <h2 class="alp-section-title" id="alp-process">The Step-by-Step Legal Process for Foreign Patients</h2>
        <p class="alp-body">
          The prospect of fighting a legal battle in a foreign jurisdiction can seem overwhelming. However, our specialized legal team handles the entire process on your behalf, ensuring you do not need to constantly travel back to Türkiye. Here is how the process works from start to finish:
        </p>

        <div class="alp-timeline">

          <div class="alp-timeline-item">
            <div class="alp-timeline-marker">1</div>
            <div class="alp-timeline-content">
              <h4>Gathering Evidence and Initial Assessment</h4>
              <p>Your case is built on evidence. From the moment you suspect malpractice, you should document everything. Do not delete your WhatsApp conversations with the clinic, the health tourism agency, or the doctor. These messages are critical evidence of what was promised versus what was delivered. Save all payment receipts, bank transfer records, and promotional brochures. Take clear, well-lit photographs of your arms from multiple angles every single day to document the progression of the scarring, infection, or asymmetry. We will review this evidence during our initial, confidential consultation to determine the legal viability of your claim.</p>
            </div>
          </div>

          <div class="alp-timeline-item">
            <div class="alp-timeline-marker">2</div>
            <div class="alp-timeline-content">
              <h4>Securing Independent Medical Opinions</h4>
              <p>We cannot simply walk into court and state that the surgery was botched; we must prove it medically. We work with independent, board-certified plastic surgeons and medical experts (both in Türkiye and internationally) to review your pre-operative photos, post-operative results, and surgical notes. These experts will provide a formalized medical report indicating exactly how the operating surgeon deviated from the standard of care.</p>
            </div>
          </div>

          <div class="alp-timeline-item">
            <div class="alp-timeline-marker">3</div>
            <div class="alp-timeline-content">
              <h4>Issuing a Power of Attorney (Vekaletname)</h4>
              <p>To act on your behalf, we require legal authorization. You do not need to fly to Istanbul for this. You simply visit the nearest Turkish Consulate or Embassy in your home country (e.g., in London, New York, or Berlin) and issue a specialized Power of Attorney to our law firm. This document empowers us to file lawsuits, attend court hearings, and negotiate settlements without your physical presence.</p>
            </div>
          </div>

          <div class="alp-timeline-item">
            <div class="alp-timeline-marker">4</div>
            <div class="alp-timeline-content">
              <h4>Mandatory Mediation (Arabuluculuk)</h4>
              <p>Before a medical malpractice case can be formally tried in a Consumer Court in Türkiye, the law requires both parties to participate in mandatory mediation. This is a highly strategic phase. We will present the clinic and their malpractice insurance company with the overwhelming evidence of their negligence. In many cases, clinics wish to avoid public scandals and the lengthy court process, leading to a substantial, confidential financial settlement during mediation.</p>
            </div>
          </div>

          <div class="alp-timeline-item">
            <div class="alp-timeline-marker">5</div>
            <div class="alp-timeline-content">
              <h4>Litigation and Forensic Medicine Evaluation</h4>
              <p>If the clinic refuses to offer a fair settlement, we immediately file a lawsuit in the Consumer Courts. During litigation, the court will inevitably refer the case to the Turkish Forensic Medicine Institute (Adli Tıp Kurumu) or a panel of university professors. This panel conducts an official, binding review of the surgical outcome to determine fault. Our lawyers continuously monitor this process, submitting counter-arguments and independent expert reports to ensure the court's panel receives the full, accurate picture of your suffering.</p>
            </div>
          </div>

        </div>

        <!-- ── COMPENSATION ── -->
        <h2 class="alp-section-title" id="alp-compensation">Types of Compensation You Can Recover</h2>
        <p class="alp-body">
          If you have been the victim of arm lift malpractice, the financial burden can be devastating. You may require multiple revision surgeries, extensive physical therapy, and psychological counseling. Turkish law allows you to claim comprehensive damages against the surgeon, the clinic, and the medical tourism agency.
        </p>

        <div class="alp-compensation-grid">

          <div class="alp-compensation-card alp-compensation-material">
            <h4>Pecuniary (Material) Damages<br><small style="font-weight:400; color: var(--text-muted);">Maddi Tazminat</small></h4>
            <p class="alp-body" style="margin-bottom: 1rem;">Pecuniary damages are designed to reimburse you for every single penny you have lost or will lose as a direct result of the botched surgery. This includes:</p>
            <ul class="alp-icon-list alp-icon-list-compact">
              <li>
                <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
                <span><strong>Refund of the Original Surgery:</strong> The total amount you paid to the clinic and the agency for the botched procedure, including your flights and hotel accommodations in Türkiye.</span>
              </li>
              <li>
                <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
                <span><strong>Revision Surgery Costs:</strong> The estimated costs of future corrective surgeries required to fix the deformities. Crucially, you can claim the cost of having these corrective surgeries performed in your home country (e.g., by a top surgeon in Harley Street, London), which is often vastly more expensive than the original surgery in Türkiye.</span>
              </li>
              <li>
                <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
                <span><strong>Medical Expenses:</strong> Costs for medications, wound care supplies, physical therapy for nerve damage, and psychiatric counseling.</span>
              </li>
              <li>
                <svg class="alp-check" viewBox="0 0 24 24"><path d="M20 6L9 17l-5-5" stroke="var(--teal)" stroke-width="2.5" fill="none"/></svg>
                <span><strong>Loss of Earnings:</strong> If your severe scarring, infections, or nerve damage prevented you from returning to work, or permanently diminished your earning capacity, you can claim full compensation for your lost wages.</span>
              </li>
            </ul>
          </div>

          <div class="alp-compensation-card alp-compensation-moral">
            <h4>Non-Pecuniary (Moral) Damages<br><small style="font-weight:400; color: var(--text-muted);">Manevi Tazminat</small></h4>
            <p class="alp-body" style="margin-bottom: 0;">
              A botched cosmetic surgery inflicts immense psychological trauma. Non-pecuniary damages are awarded to compensate you for your physical pain, emotional suffering, loss of self-esteem, depression, and the overall degradation of your quality of life. The court determines the amount of moral damages based on the severity of the disfigurement, your age, your psychological state, and the degree of gross negligence exhibited by the surgeon. In cases of massive, permanent scarring or irreversible nerve damage, Turkish courts award substantial moral damages to provide a sense of justice and solace to the victim.
            </p>
          </div>

        </div>

        <!-- ── STATUTE OF LIMITATIONS ── -->
        <h2 class="alp-section-title" id="alp-statute">Understanding the Statute of Limitations</h2>

        <div class="alp-warning-box">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#b45309" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
          <div>
            <strong>Time is of the essence.</strong> The standard statute of limitations is <strong>5 years</strong> from the date of the surgery. For gross negligence or fraud, it extends to <strong>20 years</strong>.
          </div>
        </div>

        <p class="alp-body">
          Time is of the essence in medical malpractice claims. In Türkiye, strict legal deadlines—known as the statute of limitations (zaman aşımı)—govern how long you have to file a lawsuit. Because an arm lift is classified under a "Contract for Work," the standard statute of limitations is <strong>five (5) years</strong> from the date of the surgery.
        </p>
        <p class="alp-body">
          However, if the surgeon's actions constituted "gross negligence" (ağır kusur) or intentional fraud (such as an unlicensed assistant performing the surgery while claiming to be the doctor), the statute of limitations can be extended to <strong>twenty (20) years</strong>. Despite these seemingly generous timeframes, it is imperative to act immediately. As time passes, vital evidence disappears: clinics shut down, surgeons relocate, hospital records are conveniently "lost," and physical scars begin to fade, making it far more difficult for forensic experts to evaluate the initial severity of the malpractice.
        </p>

        <!-- ── HOW WE CAN HELP ── -->
        <h2 class="alp-section-title" id="alp-help">How Medical Law Türkiye Can Help You</h2>
        <p class="alp-body">
          At Medical Law Türkiye, we specialize exclusively in representing international patients who have suffered at the hands of negligent medical professionals in Türkiye. We are not a general practice firm; our entire infrastructure is dedicated to the highly complex intersection of Turkish health law, cosmetic surgery litigation, and cross-border consumer protection.
        </p>
        <p class="alp-body">
          We know the clinics, we know the "health tourism agencies," and we intimately understand the tactics their insurance companies use to avoid paying out claims. When you entrust us with your case, we provide a full-service, aggressive legal strategy aimed at maximizing your financial recovery. You sought out an arm lift to improve your confidence, not to be left with life-altering deformities. Let our expert attorneys fight the legal battles in Istanbul, Ankara, or Antalya, while you focus entirely on your physical and emotional recovery at home.
        </p>

        <!-- ── END CTA ── -->
        <div class="alp-end-cta">
          <h3>Ready to Protect Your Rights?</h3>
          <p>Contact our specialized legal team for a free, strictly confidential assessment of your arm lift malpractice case. All communications are protected by attorney-client privilege.</p>
          <div class="alp-end-cta-actions">
            <a href="index.html#contact" class="alp-end-cta-btn">Request Free Case Review</a>
            <a href="https://wa.me/905319336316" class="alp-end-cta-btn-secondary" target="_blank" rel="noopener">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.625.846 5.059 2.284 7.034L.789 23.492l4.625-1.478A11.932 11.932 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.75c-2.16 0-4.16-.69-5.795-1.86l-.415-.276-2.744.878.853-2.668-.3-.434A9.713 9.713 0 012.25 12c0-5.385 4.365-9.75 9.75-9.75s9.75 4.365 9.75 9.75-4.365 9.75-9.75 9.75z"/></svg>
              WhatsApp Us
            </a>
          </div>
        </div>

        <!-- ── DISCLAIMER ── -->
        <div class="alp-disclaimer">
          <h4>Disclaimer</h4>
          <p>
            The comprehensive information provided on this page is intended for general informational and educational purposes only. It does not constitute formal legal advice, nor does reading it establish an attorney-client relationship. Medical malpractice is a highly nuanced area of law, and the outcome of any case depends entirely on its unique facts and the specific evidence available. Always consult directly with a qualified Turkish medical malpractice lawyer regarding your specific situation.
          </p>
        </div>

      </article>
    </div>
  </section>
"""

# ═══════════════════════════════════════════════════════
# 2. PERFORM REPLACEMENTS
# ═══════════════════════════════════════════════════════

# Replace content section
html = re.sub(
    r'  <!-- ── CONTENT ── -->.*?</section>\s*\n\s*\n\s*  <!-- ── FAQ ── -->',
    new_content_section + '\n\n  <!-- ── FAQ ── -->',
    html,
    flags=re.DOTALL
)

# ═══════════════════════════════════════════════════════
# 3. ADD PAGE-SPECIFIC STYLES BEFORE </head>
# ═══════════════════════════════════════════════════════

page_styles = """
  <!-- Page-specific styles for article layout -->
  <style>
    /* ── ALP: Article Layout & Typography ── */
    .alp-article {
      background: var(--white);
      padding: 3rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
      border-radius: var(--radius-md);
    }
    @media (max-width: 640px) {
      .alp-article { padding: 1.5rem; }
    }
    .alp-body {
      color: var(--text-secondary);
      line-height: 1.85;
      font-size: 1.02rem;
      margin-bottom: 1.5rem;
    }
    .alp-section-title {
      font-size: 1.65rem;
      color: var(--navy);
      margin-top: 3rem;
      margin-bottom: 1.25rem;
      line-height: 1.3;
      font-weight: 700;
      letter-spacing: -0.01em;
    }

    /* ── TABLE OF CONTENTS ── */
    .alp-toc {
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.5rem 2rem;
      margin-bottom: 2rem;
      box-shadow: var(--shadow-xs);
    }
    .alp-toc-label {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-weight: 700;
      color: var(--navy);
      font-size: 0.92rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 1rem;
    }
    .alp-toc-list {
      list-style: none;
      counter-reset: toc-counter;
      padding: 0;
      margin: 0;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.5rem 2rem;
    }
    @media (max-width: 640px) {
      .alp-toc-list { grid-template-columns: 1fr; }
    }
    .alp-toc-list li {
      counter-increment: toc-counter;
    }
    .alp-toc-list li a {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--text-secondary);
      font-size: 0.88rem;
      font-weight: 500;
      padding: 0.4rem 0;
      transition: color var(--transition);
      text-decoration: none;
    }
    .alp-toc-list li a::before {
      content: counter(toc-counter, decimal-leading-zero);
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--teal);
      min-width: 1.5rem;
    }
    .alp-toc-list li a:hover {
      color: var(--teal);
    }

    /* ── KEY TAKEAWAYS ── */
    .alp-takeaways {
      background: linear-gradient(135deg, #F0FDFA 0%, #ECFDF5 100%);
      border: 1px solid rgba(14, 116, 144, 0.15);
      border-radius: var(--radius-md);
      padding: 2rem;
      margin-bottom: 2.5rem;
    }
    .alp-takeaways-header {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      margin-bottom: 1.25rem;
    }
    .alp-takeaways-header h3 {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--navy);
      margin: 0;
    }
    .alp-takeaway-list {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
    .alp-takeaway-list li {
      display: flex;
      align-items: flex-start;
      gap: 0.65rem;
    }
    .alp-check {
      width: 20px;
      height: 20px;
      min-width: 20px;
      margin-top: 2px;
    }
    .alp-takeaway-list li span {
      color: var(--text-secondary);
      font-size: 0.93rem;
      line-height: 1.6;
    }

    /* ── HIGHLIGHT / DEFINITION BOX ── */
    .alp-highlight-box {
      background: var(--gray-50);
      border-left: 4px solid var(--navy);
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      padding: 2rem;
      margin: 2.5rem 0;
      position: relative;
    }
    .alp-highlight-icon {
      position: absolute;
      top: -14px;
      left: 20px;
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: 50%;
      width: 36px;
      height: 36px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .alp-highlight-title {
      font-size: 1.3rem;
      color: var(--navy);
      margin: 0.5rem 0 1rem 0;
      font-weight: 700;
    }

    /* ── COMPLICATION CARDS ── */
    .alp-complication-grid {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin: 1.5rem 0 2rem 0;
    }
    .alp-complication-card {
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.75rem;
      position: relative;
      transition: box-shadow var(--transition), border-color var(--transition);
    }
    .alp-complication-card:hover {
      box-shadow: var(--shadow-md);
      border-color: var(--border-teal);
    }
    .alp-complication-num {
      font-size: 2rem;
      font-weight: 800;
      color: rgba(14, 116, 144, 0.12);
      line-height: 1;
      margin-bottom: 0.5rem;
      letter-spacing: -0.02em;
    }
    .alp-complication-title {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--navy);
      margin-bottom: 0.75rem;
    }

    /* ── INLINE CTA ── */
    .alp-inline-cta {
      background: linear-gradient(135deg, var(--navy) 0%, var(--navy-mid) 100%);
      border-radius: var(--radius-lg);
      padding: 2rem 2.5rem;
      margin: 3rem 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 2rem;
      flex-wrap: wrap;
    }
    .alp-inline-cta-text h4 {
      color: #fff;
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 0.35rem;
    }
    .alp-inline-cta-text p {
      color: rgba(255,255,255,0.75);
      font-size: 0.88rem;
      margin: 0;
    }
    .alp-inline-cta-btn {
      background: var(--teal);
      color: #fff;
      padding: 0.75rem 1.75rem;
      border-radius: var(--radius-sm);
      font-weight: 600;
      font-size: 0.88rem;
      text-decoration: none;
      white-space: nowrap;
      transition: background var(--transition), transform var(--transition);
    }
    .alp-inline-cta-btn:hover {
      background: var(--teal-dark);
      transform: translateY(-1px);
    }

    /* ── LEGAL DOCTRINE CARDS ── */
    .alp-legal-cards {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin: 1.5rem 0 2rem 0;
    }
    .alp-legal-card {
      background: var(--white);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 1.75rem;
      transition: box-shadow var(--transition);
    }
    .alp-legal-card:hover {
      box-shadow: var(--shadow-md);
    }
    .alp-legal-card-header {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      margin-bottom: 1rem;
    }
    .alp-legal-card-header h4 {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--navy);
      margin: 0;
    }

    /* ── ICON LIST ── */
    .alp-icon-list {
      list-style: none;
      padding: 0;
      margin: 0 0 1.5rem 0;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }
    .alp-icon-list-compact { gap: 0.6rem; }
    .alp-icon-list li {
      display: flex;
      align-items: flex-start;
      gap: 0.65rem;
    }
    .alp-icon-list li span {
      color: var(--text-secondary);
      font-size: 0.95rem;
      line-height: 1.7;
    }

    /* ── QUOTE BLOCK ── */
    .alp-quote {
      border-left: 4px solid var(--teal);
      background: var(--teal-bg);
      padding: 1.75rem 2rem;
      margin: 2rem 0;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
    }
    .alp-quote p {
      color: var(--navy);
      font-size: 1.05rem;
      font-weight: 500;
      line-height: 1.7;
      margin: 0;
      font-style: italic;
    }

    /* ── TIMELINE ── */
    .alp-timeline {
      position: relative;
      padding-left: 3rem;
      margin: 1.5rem 0 2.5rem 0;
    }
    .alp-timeline::before {
      content: '';
      position: absolute;
      left: 15px;
      top: 0;
      bottom: 0;
      width: 2px;
      background: linear-gradient(180deg, var(--teal), var(--border));
      border-radius: 1px;
    }
    .alp-timeline-item {
      position: relative;
      padding-bottom: 2rem;
    }
    .alp-timeline-item:last-child {
      padding-bottom: 0;
    }
    .alp-timeline-marker {
      position: absolute;
      left: -3rem;
      top: 0;
      width: 32px;
      height: 32px;
      background: var(--teal);
      color: #fff;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 0.82rem;
      z-index: 1;
      box-shadow: 0 0 0 4px var(--off-white);
    }
    .alp-timeline-content h4 {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--navy);
      margin-bottom: 0.5rem;
    }
    .alp-timeline-content p {
      color: var(--text-secondary);
      font-size: 0.93rem;
      line-height: 1.75;
      margin: 0;
    }

    /* ── COMPENSATION GRID ── */
    .alp-compensation-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1rem;
      margin: 1.5rem 0;
    }
    .alp-compensation-card {
      border-radius: var(--radius-md);
      padding: 2rem;
    }
    .alp-compensation-card h4 {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--navy);
      margin-bottom: 1rem;
    }
    .alp-compensation-material {
      background: var(--gray-50);
      border: 1px solid var(--border);
    }
    .alp-compensation-moral {
      background: linear-gradient(135deg, #F0FDFA 0%, #F0F9FF 100%);
      border: 1px solid rgba(14, 116, 144, 0.12);
    }

    /* ── WARNING BOX ── */
    .alp-warning-box {
      display: flex;
      align-items: flex-start;
      gap: 0.85rem;
      background: #FFFBEB;
      border: 1px solid #FDE68A;
      border-radius: var(--radius-md);
      padding: 1.25rem 1.5rem;
      margin-bottom: 1.5rem;
      font-size: 0.93rem;
      color: #92400E;
      line-height: 1.6;
    }
    .alp-warning-box svg { flex-shrink: 0; margin-top: 2px; }

    /* ── END CTA ── */
    .alp-end-cta {
      background: linear-gradient(135deg, var(--navy) 0%, #1E3A5F 100%);
      border-radius: var(--radius-lg);
      padding: 2.5rem;
      margin-top: 3rem;
      text-align: center;
    }
    .alp-end-cta h3 {
      color: #fff;
      font-size: 1.4rem;
      font-weight: 700;
      margin-bottom: 0.75rem;
    }
    .alp-end-cta p {
      color: rgba(255,255,255,0.75);
      font-size: 0.93rem;
      max-width: 540px;
      margin: 0 auto 1.5rem auto;
      line-height: 1.6;
    }
    .alp-end-cta-actions {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1rem;
      flex-wrap: wrap;
    }
    .alp-end-cta-btn {
      background: var(--teal);
      color: #fff;
      padding: 0.85rem 2rem;
      border-radius: var(--radius-sm);
      font-weight: 600;
      font-size: 0.93rem;
      text-decoration: none;
      transition: background var(--transition), transform var(--transition);
    }
    .alp-end-cta-btn:hover {
      background: var(--teal-dark);
      transform: translateY(-1px);
    }
    .alp-end-cta-btn-secondary {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: transparent;
      color: rgba(255,255,255,0.85);
      padding: 0.85rem 1.75rem;
      border: 1px solid rgba(255,255,255,0.25);
      border-radius: var(--radius-sm);
      font-weight: 600;
      font-size: 0.93rem;
      text-decoration: none;
      transition: all var(--transition);
    }
    .alp-end-cta-btn-secondary:hover {
      background: rgba(255,255,255,0.1);
      border-color: rgba(255,255,255,0.45);
    }

    /* ── DISCLAIMER ── */
    .alp-disclaimer {
      background: var(--gray-50);
      border-left: 3px solid var(--border);
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      padding: 1.25rem 1.5rem;
      margin-top: 2.5rem;
    }
    .alp-disclaimer h4 {
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 0.35rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .alp-disclaimer p {
      color: var(--text-muted);
      font-size: 0.82rem;
      line-height: 1.6;
      margin: 0;
    }
  </style>
"""

html = html.replace('</head>', page_styles + '</head>')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: UI refactored. File size:", len(html))
