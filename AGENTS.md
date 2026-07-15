# Medical Law Türkiye — Agent Rules

## Floating WhatsApp button (mandatory on every page)

Every HTML page on this site **must** include the fixed floating WhatsApp icon in the bottom-right corner, matching `index.html`.

### When creating or generating any new HTML page

1. Link `styles.css` (it already defines `.floating-whatsapp`).
2. Place the following block once, just before `</body>` (after the footer and page scripts is fine; do not put it inside the footer):

```html
  <!-- ── FLOATING WHATSAPP ── -->
  <a href="https://wa.me/905319336316" class="floating-whatsapp" id="floatingWhatsapp" target="_blank" rel="noopener"
    aria-label="Contact us on WhatsApp">
    <svg viewBox="0 0 24 24" fill="currentColor" width="28" height="28">
      <path
        d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z" />
      <path
        d="M12 0C5.373 0 0 5.373 0 12c0 2.625.846 5.059 2.284 7.034L.789 23.492l4.625-1.478A11.932 11.932 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.75c-2.16 0-4.16-.69-5.795-1.86l-.415-.276-2.744.878.853-2.668-.3-.434A9.713 9.713 0 012.25 12c0-5.385 4.365-9.75 9.75-9.75s9.75 4.365 9.75 9.75-4.365 9.75-9.75 9.75z" />
    </svg>
  </a>
```

### Requirements

- **URL:** `https://wa.me/905319336316` (do not change the number unless explicitly requested).
- **Classes / id:** `class="floating-whatsapp"` and `id="floatingWhatsapp"`.
- **One per page only** — never duplicate the floating button.
- **Page generators** (`generate_glossary_pages.py`, `generate_more_glossary_pages.py`, or any new HTML builder) must include this block in their footer/template.
- Do **not** remove or hide the button for print-only exceptions unless the user asks; CSS already hides it in `@media print`.

### Quick check

Before finishing any page create/edit task, confirm the file contains `class="floating-whatsapp"`.
