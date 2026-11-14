# Arowolo Olawale Temidayo — Student Portfolio & Academic Planner

A responsive five-page COS 106 term project built with plain HTML5, CSS3 and JavaScript. No framework, package installation, API keys or build step is needed.

## Run locally

From this folder:

```sh
python3 -m http.server 8000 --directory pages
```

Open http://localhost:8000. On Windows, use `py` instead of `python3` if necessary. Use a local server for consistent browser storage and video captions.

## Pages

- `pages/index.html`: welcome, profile and featured projects.
- `pages/about.html`: biography, skills, interests, education table and local video.
- `pages/projects.html`: three sample projects, with working calculator and timer dialogs.
- `pages/planner.html`: task creation, optional deadlines, priorities, completion, deletion, filters and progress.
- `pages/contact.html`: required-field, email and digits-only phone validation.
- `pages/styles.css`: shared simple styling, responsive layout with Grid and Flexbox, and reduced-motion support.
- `pages/app.js`: navigation, planner, contact validation and project interactions.
- `pages/assets/`: profile photograph, original illustrations, video and captions.

## Before academic submission

1. Check that the biography, goals and interests on the About page describe you accurately. The institution is set to MIVA Open University.
2. Review and personalise the project descriptions and sample grading scale. The calculator's scale is illustrative, not an official university grading policy.
3. Review the code so you can explain the arrays, functions, event handlers, DOM updates and local storage.
4. Publish the website and submit both the public website URL and your GitHub repository URL. A private preview is not the public submission link.

## GitHub upload and hosting

Extract the ZIP first. Upload its contents to a new repository; do not upload only the ZIP. The repository root should contain this README, `pages/`, and `scripts/`.

To publish with a branch-based GitHub Pages workflow, put the contents of `pages/` at the root of your publishing branch and enable Pages for that branch/root. Alternatively configure a Pages deployment workflow that uploads `pages/` as the static artifact. All page and asset links are relative, so repository subpath hosting works. No secrets are required.

## Behaviour and limitations

- Tasks are stored under `prince-academic-tasks-v1` in this browser's local storage. They do not sync between devices or domains. Storage failure is reported, and the planner continues for the current session.
- Contact validation is a classroom demonstration. It sends and stores no messages. A server or form service is needed for real delivery.
- Task titles are inserted using `textContent`, so entered HTML is displayed as text.
- The focus timer uses the clock to account for delayed background ticks. Closing its dialog resets the session.
- The 12-second video is an original silent introduction with captions and a text transcript.
- This project intentionally has no login or backend; neither is required by the brief.

## Checks

```sh
node --check pages/app.js
python3 scripts/check_project.py
```

See `TESTING.md` for the browser checks and remaining personalisation items.
