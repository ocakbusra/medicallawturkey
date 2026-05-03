import os
import re

new_terms = [
    ("Permanent Disability Rate", "Turkish: Maluliyet Oranı", "The officially determined percentage of permanent loss of bodily or mental functions resulting from a medical error, used to calculate future loss of earnings."),
    ("Temporary Incapacity", "Turkish: Geçici İş Göremezlik", "The period during which a patient is unable to work or perform daily activities while recovering from a medically induced injury before reaching maximum medical improvement."),
    ("Iatrogenic Injury", "Turkish: İyatrojenik Zarar", "Any harm, injury, or complication unintentionally caused to a patient by a physician, medical treatment, or diagnostic procedure."),
    ("Nosocomial Infection", "Turkish: Hastane Enfeksiyonu", "An infection acquired by a patient during a hospital stay that was not present or incubating at the time of admission, often raising questions about facility hygiene standards."),
    ("Wrong-Site Surgery", "Turkish: Yanlış Taraf Ameliyatı", "A severe never event in which a surgical procedure is performed on the wrong patient, wrong body part, or the wrong side of the body."),
    ("Surgical Negligence", "Turkish: Cerrahi İhmal", "A failure by a surgeon to exercise the required standard of care during an operation, encompassing technical errors, leaving foreign objects inside patients, or poor surgical planning."),
    ("Post-Operative Care", "Turkish: Ameliyat Sonrası Bakım Yükümlülüğü", "The legal and ethical obligation of a healthcare provider to monitor, treat, and manage a patient's recovery and any complications immediately following surgery."),
    ("Off-Label Drug Use", "Turkish: Endikasyon Dışı İlaç Kullanımı", "The practice of prescribing a medication for an unapproved indication, age group, dose, or form of administration, which carries specific informed consent requirements."),
    ("Medical Device Liability", "Turkish: Tıbbi Cihaz Sorumluluğu", "The legal responsibility borne by manufacturers, distributors, or medical facilities when a defective medical implant or device causes patient injury."),
    ("Cosmetic Surgery Regulation", "Turkish: Estetik Cerrahi Mevzuatı", "The specific body of laws and ethical guidelines governing elective aesthetic procedures, which heavily emphasizes guaranteed outcomes and stringent informed consent."),
    ("Loss of Earnings", "Turkish: Kazanç Kaybı", "Pecuniary damages awarded to compensate a patient for the income they have lost, and will predictably lose in the future, due to a malpractice-induced disability."),
    ("Future Medical Expenses", "Turkish: Gelecekteki Tedavi Giderleri", "Compensation intended to cover all anticipated costs for necessary ongoing care, revision surgeries, medications, and rehabilitation resulting from a medical error."),
    ("Loss of Consortium", "Turkish: Aile Bütünlüğünün Bozulması Zararı", "Damages claimed by the close family members or spouse of a malpractice victim for the deprivation of companionship, affection, and marital relations due to severe injury or death."),
    ("Wrongful Death", "Turkish: Haksız Ölüm", "A legal claim brought by surviving dependents or close relatives against a healthcare provider whose negligence directly caused the death of the patient."),
    ("Bereavement Damages", "Turkish: Ölüm Nedeniyle Manevi Tazminat", "Non-pecuniary (moral) compensation awarded to the family members of a deceased patient to alleviate their profound grief and emotional suffering."),
    ("Damage Mitigation Obligation", "Turkish: Zararı Azaltma Yükümlülüğü", "The legal duty of an injured patient to take reasonable steps to prevent their health condition and financial losses from worsening following a medical error."),
    ("Interest on Damages", "Turkish: Tazminata İşleyen Faiz", "The statutory or commercial interest applied to a compensation award, calculated from the date the malpractice occurred or the lawsuit was filed, to preserve the value of the money."),
    ("Lump Sum vs. Periodic Payment", "Turkish: Toplu / Dönemsel Ödeme", "The methods by which courts can order compensation to be paid; while lump-sum is standard in Türkiye, periodic payments (annuities) can be requested for long-term care needs."),
    ("Malpractice Insurance", "Turkish: Mesleki Sorumluluk Sigortası", "Mandatory professional liability insurance for physicians in Türkiye that covers the defense costs and compensation claims arising from medical negligence."),
    ("Social Security Recourse", "Turkish: SGK Rücu Hakkı", "The legal right of the Turkish Social Security Institution (SGK) to reclaim the costs of medical treatments it provided to the victim from the negligent doctor or hospital."),
    ("Contractual Liability", "Turkish: Sözleşmeden Doğan Sorumluluk", "The legal responsibility arising when a healthcare provider or private clinic breaches the explicit or implied terms of the treatment contract with the patient."),
    ("Tortious Liability", "Turkish: Haksız Fiilden Doğan Sorumluluk", "Liability that arises from a wrongful act or infringement of a right (other than under contract) leading to civil legal liability, often applicable in emergency interventions."),
    ("Vicarious Liability", "Turkish: Üstün Sorumluluğu / Adam Çalıştıranın Sorumluluğu", "The legal doctrine holding a hospital or clinic owner strictly liable for the negligent actions committed by their employed doctors or nurses during their duties."),
    ("Joint and Several Liability", "Turkish: Müteselsil Sorumluluk", "A legal rule allowing a patient to pursue a claim for the full amount of damages against any one or all of multiple negligent parties (e.g., both the surgeon and the hospital)."),
    ("Strict Liability", "Turkish: Kusursuz Sorumluluk", "Liability that does not depend on actual negligence or intent to harm; in Turkish medical law, this is exceptionally applied to hospitals regarding facility safety and organizational flaws."),
    ("Contributory Negligence", "Turkish: Müterafik Kusur", "A legal defense arguing that the patient's own actions (such as failing to follow post-operative instructions) contributed to their injury, which may reduce the compensation amount."),
    ("Force Majeure", "Turkish: Mücbir Sebep", "An unforeseeable and unavoidable external event (like an earthquake during surgery) that totally prevents a doctor from fulfilling their obligations, exempting them from liability."),
    ("Assumption of Risk", "Turkish: Riski Kabul", "The legal principle that a patient, having been fully and properly informed of the unavoidable natural risks of a procedure, cannot claim malpractice if one of those specific risks occurs."),
    ("Breach of Contract", "Turkish: Sözleşmenin İhlali", "A failure by a medical provider to perform any term of a contract, such as a cosmetic surgeon failing to achieve an explicitly promised aesthetic outcome."),
    ("Medical Service Contract", "Turkish: Vekalet / Eser Sözleşmesi", "The legal classification of the doctor-patient relationship; generally a mandate contract (vekalet) for healing, but a contract of work (eser) for elective cosmetic results."),
    ("Patient Rights Regulation", "Turkish: Hasta Hakları Yönetmeliği", "The comprehensive administrative legislation in Türkiye detailing the fundamental rights of patients, including the right to information, privacy, and respectful care."),
    ("Right to Refuse Treatment", "Turkish: Tedaviyi Reddetme Hakkı", "The fundamental right of a mentally competent patient to decline or halt medical interventions, even if doing so may result in severe health consequences or death."),
    ("Right to Second Opinion", "Turkish: İkinci Görüş Hakkı", "The legal right of a patient to consult with another physician regarding their diagnosis and treatment plan without facing prejudice from their primary healthcare provider."),
    ("Privacy of Medical Data", "Turkish: Tıbbi Veri Gizliliği", "The strict legal protection of patient health records and personal information, protected under both medical ethics and the Turkish Personal Data Protection Law (KVKK)."),
    ("Right to Access Medical Records", "Turkish: Tıbbi Kayıtlara Erişim Hakkı", "A patient's absolute right to obtain copies of all documents, test results, and notes in their medical file, which is crucial for building a malpractice case."),
    ("Patient Advocate", "Turkish: Hasta Hakları Birimi", "A dedicated unit within Turkish hospitals designed to address patient grievances, facilitate communication, and mediate minor disputes before they escalate to legal action."),
    ("Vulnerable Patient", "Turkish: Savunmasız Hasta", "Patients who are minors, elderly, mentally incapacitated, or language-barrier-restricted (like tourists), requiring heightened standards of care and specialized consent procedures."),
    ("Minor Patient Consent", "Turkish: Küçük Hastada Onam", "The legal requirement that valid consent for treating a patient under the age of 18 must be obtained from their parents or legal guardians, except in immediate life-saving emergencies."),
    ("Capacity to Consent", "Turkish: Rıza Ehliyeti", "The mental and legal ability of a patient to understand the nature, risks, and consequences of a medical procedure and make an informed decision regarding it."),
    ("Emergency Exception to Consent", "Turkish: Acil Durumda Onam İstisnası", "The legal provision allowing doctors to perform life-saving medical interventions on an unconscious or incapacitated patient without obtaining prior consent.")
]

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\-]+', '-', text)
    return text.strip('-')

new_html = ""
for term, tr_term, desc in new_terms:
    slug = slugify(term)
    new_html += f'''
        <a href="glossary-{slug}.html" class="cs-card" style="text-decoration: none;">
          <span class="cs-tag">Glossary Term</span>
          <h3>{term}</h3>
          <p style="font-weight: 600; font-size: 0.9rem; color: #0891B2; margin-bottom: 0.5rem;">{tr_term}</p>
          <p>{desc}</p>
          <span class="cs-read">Read detailed guide →</span>
        </a>
'''

with open('glossary.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find where the .cs-grid closes.
# Let's look for:
#       </div>
#     </div>
#   </section>
# 
#   <!-- ── CONTACT / CTA ── -->
insert_marker = "      </div>\n    </div>\n  </section>\n\n  <!-- ── CONTACT / CTA ── -->"

if insert_marker in content:
    content = content.replace(insert_marker, new_html + "\n" + insert_marker)
else:
    # Just a fallback if exact spacing is different
    insert_marker_alt = "</div>\n    </div>\n  </section>\n\n  <!-- ── CONTACT / CTA ── -->"
    content = content.replace(insert_marker_alt, new_html + "\n" + insert_marker_alt)

with open('glossary.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated glossary.html with 40 new terms.")
