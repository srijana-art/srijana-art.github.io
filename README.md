# Srijana GS — Artist Portfolio Site

A single-page portfolio site for Srijana GS, built from her Instagram (@srijana.art.gallery) content: bio, gallery of paintings, artist statement, and contact/commission info.

## Files
- `index.html` — the entire site (HTML, CSS, and JS all in one file)
- `images/thumbs/` — small JPEGs (max 700px) shown in the gallery grid
- `images/web/` — larger JPEGs (max 1600px) shown in the lightbox and the About portrait
- `images/png/` — full-resolution scans. **Not published** (see `.gitignore`) — kept locally as the masters
- `images/old/` — the four earlier low-res images, superseded. Also not published

Only `index.html` and `images/thumbs` + `images/web` need to go to GitHub — about 14 MB. The PNG masters are ~95 MB and are deliberately excluded.

## How to publish this on GitHub Pages (username: srijana-art)

1. **Create a new repository**
   - Go to https://github.com/new
   - Repository name: `srijana-art.github.io` (must match your username exactly, including case)
   - Set it to **Public**
   - Do NOT initialize with a README (you're uploading existing files)
   - Click **Create repository**

2. **Upload the files**
   - On the new repo's page, click **uploading an existing file**
   - Drag in `index.html` and the `images` folder — but only the `thumbs` and `web` subfolders inside it (keep the folder structure: `images/thumbs/...` and `images/web/...`)
   - Commit the changes (the default commit message is fine, or write your own)

   Alternatively, if you're comfortable with git on your computer:
   ```
   git clone https://github.com/srijana-art/srijana-art.github.io.git
   cd srijana-art.github.io
   # copy index.html and the images folder into this directory
   git add .
   git commit -m "Add artist portfolio site"
   git push
   ```

3. **Enable GitHub Pages**
   - In the repo, go to **Settings → Pages**
   - Under "Build and deployment", Source should already be set to "Deploy from a branch"
   - Branch: select `main` (or `master`), folder `/ (root)` — click **Save**

4. **Wait a minute or two**, then visit:
   **https://srijana-art.github.io/**

   GitHub Pages usually takes 1–2 minutes to go live after the first push. If it 404s at first, wait a bit and refresh.

## Making changes later

- To update text: open `index.html` in any text editor, find the relevant section (they're commented and easy to spot — About, Gallery, Process, Contact), edit, save, and re-upload/push.
- To fix a title, medium, or description: search `index.html` for the current title. Each painting is one `<figure class="art-card">` block; the `data-title`, `data-medium` and `data-desc` attributes feed the lightbox, and the `<figcaption>` at the bottom of the block feeds the hover caption. Change both so they match.
- To add more artwork:
  1. Put the full-resolution file in `images/png/` as `SrijanaNN.png`.
  2. Make the two web versions (macOS, needs ImageMagick — `brew install imagemagick`):
     ```
     cd images
     magick png/SrijanaNN.png -resize 700x700  -strip -quality 82 thumbs/artNN.jpg
     magick png/SrijanaNN.png -resize 1600x1600 -strip -quality 85 web/artNN.jpg
     ```
  3. Duplicate any `<figure class="art-card">` block in the Gallery section and update `data-full`, `data-title`, `data-medium`, `data-desc`, the `<img src>`, its `width`/`height` (the pixel size of the thumb — this stops the page jumping while images load), the `alt` text, and the `<figcaption>`.
  4. Set `data-cat` to `portrait`, `landscape`, or `still-life`, and bump the matching number in the filter buttons just above the grid.
- Changes go live automatically within a minute or two of pushing to GitHub — no rebuild step needed.

## Notes on content

The bio and artwork descriptions were written from real captions and details posted publicly on her Instagram (studio process, painting stories, artist statement quotes). Nothing was invented — but it's worth having her review the wording before or after publishing, since it speaks in her voice. The images are her own artwork, scanned at full resolution. The published JPEGs are generated from those scans; a few had white scanner margins trimmed off automatically. Titles and mediums for the 21 newer works were written from looking at the paintings, not from her captions — worth having her correct them before this goes public.
