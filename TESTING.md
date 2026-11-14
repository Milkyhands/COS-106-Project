# Testing

## Automated checks

From the project root:

```sh
node --check pages/app.js
python3 scripts/check_project.py
```

`check_project.py` confirms that each page has a header, navigation, main area and footer, contains no duplicate IDs, and links only to local files and anchors that exist.

## Browser checks

Serve the site with `python3 -m http.server 8000 --directory pages` and open http://localhost:8000.

### All pages

- Every navigation link opens the correct page, and the current page is highlighted.
- At a narrow width (about 375px), the Menu button opens and closes the navigation.
- Pressing Tab first reveals the "Skip to content" link, which moves focus to the main content.

### About me

- The video plays and the English captions appear at the bottom.
- The transcript expands and collapses.

### Projects

- Grade calculator: a score of 70 shows Grade A, 45 shows Grade D and 39 shows Grade F. Scores outside 0–100 are rejected.
- Focus timer: Start counts down from 25:00, Pause and Resume keep the remaining time, and Reset returns to 25:00. Closing the dialog stops the timer.

### Academic planner

- Submitting an empty title shows "Enter a task description." and adds nothing.
- Adding a task updates the total, pending and progress counts.
- Ticking a task marks it complete and updates the progress percentage. Unticking reverses this.
- With no tasks, the list shows "No tasks yet."
- The All, To do and Completed filters show the matching tasks. A filter with no matches shows "No tasks match this filter."
- Deleting a task removes it and updates the counts.
- Tasks remain after reloading the page.
- A title such as `<b>test</b>` is shown as plain text, not bold.

### Contact

- Submitting an empty form shows an error under every field and moves focus to the first invalid field.
- An invalid email (for example `name@site`) and a phone number containing letters or spaces are rejected.
- Valid details show "Your message passed validation. Demo only — no message has been sent."

## Personalisation still required

These items from the README's "Before academic submission" list are not yet done:

- Check that the biography, goals and interests on the About page describe you accurately.
- Review the project descriptions and the sample grading scale.
- Publish the site and record the public website URL and GitHub repository URL.
