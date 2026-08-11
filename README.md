# Srijana GS — Artist Portfolio Site

A single-page portfolio site for Srijana GS, built from her Instagram (@srijana.art.gallery) content: bio, gallery of paintings, artist statement, and contact/commission info.

## Files
- `index.html` — the entire site (HTML, CSS, and JS all in one file)
- `images/` — artwork images used on the site

## How to publish this on GitHub Pages (username: Sgu61)

1. **Create a new repository**
   - Go to https://github.com/new
   - Repository name: `Sgu61.github.io` (must match your username exactly, including case)
   - Set it to **Public**
   - Do NOT initialize with a README (you're uploading existing files)
   - Click **Create repository**

2. **Upload the files**
   - On the new repo's page, click **uploading an existing file**
   - Drag in `index.html` and the entire `images` folder (keep the folder structure — images must stay inside a folder named `images`)
   - Commit the changes (the default commit message is fine, or write your own)

   Alternatively, if you're comfortable with git on your computer:
   ```
   git clone https://github.com/Sgu61/Sgu61.github.io.git
   cd Sgu61.github.io
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
   **https://sgu61.github.io/**

   GitHub Pages usually takes 1–2 minutes to go live after the first push. If it 404s at first, wait a bit and refresh.

## Making changes later

- To update text: open `index.html` in any text editor, find the relevant section (they're commented and easy to spot — About, Gallery, Process, Contact), edit, save, and re-upload/push.
- To add more artwork: drop a new image into the `images` folder, then duplicate one of the `<div class="art-card">` blocks in the Gallery section of `index.html`, updating the `src`, `data-title`, and `data-desc` values.
- Changes go live automatically within a minute or two of pushing to GitHub — no rebuild step needed.

## Notes on content

The bio and artwork descriptions were written from real captions and details posted publicly on her Instagram (studio process, painting stories, artist statement quotes). Nothing was invented — but it's worth having her review the wording before or after publishing, since it speaks in her voice. The images used are her own posted artwork; if she'd rather swap in higher-resolution originals (these are screenshots), just replace the files in `images/` with better versions using the same filenames.
