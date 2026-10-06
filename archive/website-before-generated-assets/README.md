# Monroe Seasonal Co. — Website

A 4-page static website built on the brand kit (`../brand-kit`). Plain HTML/CSS/JS, no build step.

| Page | File | What's on it |
|---|---|---|
| Home | `index.html` | Hero, trust bar, current-season offer, services by season, reliability promises, how it works, before/afters, reviews, service area, FAQ |
| Services | `services.html` | Each season in detail + year-round rental cleanup + "what we don't do" |
| Meet the Owners | `about.html` | Story, 4 owner profiles, values, "why hire students" |
| Free Estimate | `contact.html` | Quote request form + contact info + what happens next |

## Preview it
```
python3 -m http.server 8417 --directory website
```
Then open http://localhost:8417

## Before you launch: checklist

**1. Images.** See **`ASSET-PROMPTS.md`** for all 24 image slots with AI prompts. Save each file with the exact name into `images/photos/` and it shows up automatically. Each placeholder on the site also has a "Copy prompt" button.

**2. Fill in the yellow highlighted text.** Anything with a dashed yellow highlight (`class="todo"`) is a placeholder:
- Phone number (also update every `tel:+18120000000` link) and email (`mailto:hello@example.com`)
- Hours, social links
- Owner names, majors, hometowns, bios, fun facts, and roles (`about.html`)
- Your founding story (`about.html`)
- Break-coverage plan, insurance status, payment methods (FAQ on `index.html`)
- Redo guarantee window ("48 hours"), reply time ("one business day"), snow trigger depth ("2 inches")
- Real customer reviews (with permission)

Find them all with: `grep -n 'class="todo"' *.html`

When done, you can delete the `.todo` rule in `css/styles.css` so any leftovers show as plain text.

**3. Only promise what you'll deliver.** The reliability section promises confirmed arrival windows, on-the-way texts, written quotes, photo updates, break coverage and free redos. Remove any you won't do every time.

**4. Connect the estimate form.** It doesn't send anywhere yet. Easiest options:
- [Formspree](https://formspree.io): create a form and set `action="https://formspree.io/f/XXXX"` on `<form id="estimate-form">` in `contact.html`.
- Netlify hosting: add `data-netlify="true"` and `name="estimate"` to the form.

**5. Seasonal swap.** The homepage features **Fall** right now. Each season, update the "This season" block, the hero badge, and the `is-now` card in `index.html`.

**6. Host it.** Netlify, Cloudflare Pages or GitHub Pages can all host this folder for free. Then point your domain at it.
