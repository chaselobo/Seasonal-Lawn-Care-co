# Monroe Seasonal Co. — project notes

## Git workflow (required in every chat)
This project syncs with GitHub: https://github.com/chaselobo/Seasonal-Lawn-Care-co (remote `origin`, branch `main`).

- **Before making any changes:** run `git pull --rebase origin main` so you're working on the latest version.
- **After making changes:** commit with a clear message and `git push origin main`.
- Work directly on `main` (the owner asked for this; no feature branches needed).
- If a pull hits a conflict, stop and ask before resolving anything you didn't write.

## Live site
- The public site is the `website/` folder, published to GitHub Pages by `.github/workflows/pages.yml` on every push to `main` that touches `website/`.
- Live URL: https://chaselobo.github.io/Seasonal-Lawn-Care-co/
- Pages are plain HTML/CSS/JS with relative links, so they work under the `/Seasonal-Lawn-Care-co/` subpath. Keep links relative (no leading `/`).

## Brand
- Brand kit: `brand-kit/` (colors and fonts in `brand-kit/tokens.css`), logo in `logo/`.
- Navy `#17364D` plus four season colors; Fredoka headlines, DM Sans body.
- Placeholder text on the site is marked with `class="todo"` (dashed yellow highlight).
