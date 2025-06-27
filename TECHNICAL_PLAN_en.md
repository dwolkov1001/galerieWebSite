# Technical Implementation Plan for "Image Gallery" Project

---

## Stage 1. Project Initialization and Basic Structure `[DONE]`

**Step 1.1:** Create project folder and file structure (see TDD_SPEC_en.md, section 6). `[DONE]`
**Step 1.2:** Set up virtual environment and requirements.txt (Flask, SQLite, etc.). `[DONE]`
**Step 1.3:** Create empty database and `images` table. `[DONE]`
**Step 1.4:** Create basic HTML templates (index.html, upload.html). `[DONE]`

---

## Stage 2. Image Upload `[DONE]`

**Step 2.1:** Implement image upload form (upload.html). `[DONE]`
**Step 2.2:** Implement backend upload logic (size and format restrictions). `[DONE]`
**Step 2.3:** Save file to disk and info to database. `[DONE]`
**Step 2.4:** Error handling (size, format, malicious files). `[DONE]`
**Step 2.5:** Redirect to main page after successful upload. `[DONE]`
**Step 2.6:** Write and run tests for image upload (see TDD_SPEC_en.md, 5.1, 5.4). `[DONE]`

---

## Stage 3. Gallery Display `[DONE]`

**Step 3.1:** Display all images from database on main page (index.html). `[DONE]`
**Step 3.2:** Style image grid with CSS. `[DONE]`
**Step 3.3:** Show captions for images. `[DONE]`
**Step 3.4:** Show "No images" message if gallery is empty. `[DONE]`
**Step 3.5:** Write and run tests for gallery display (see TDD_SPEC_en.md, 5.2). `[DONE]`

---

## Stage 4. Theme System `[DONE]`

**Step 4.1:** Create CSS variables for light and dark themes. `[DONE]`
**Step 4.2:** Implement dark theme styles with data-theme="dark". `[DONE]`
**Step 4.3:** Add theme toggle to header of all pages. `[DONE]`
**Step 4.4:** Create JavaScript for theme switching and saving in localStorage. `[DONE]`
**Step 4.5:** Add smooth transitions between themes (CSS transitions). `[DONE]`
**Step 4.6:** Write and run tests for theme system (see TDD_SPEC_en.md, 5.5). Manually tested, theme system works correctly.

---

## Stage 5. Image Deletion `[DONE]`

**Step 5.1:** Add "Delete" button for each image. `[DONE]`
**Step 5.2:** Implement backend logic for deleting file from disk and DB. `[DONE]`
**Step 5.3:** Error handling for deletion (nonexistent file, etc.). `[DONE]`
**Step 5.4:** Redirect to main page after deletion. `[DONE]`
**Step 5.5:** Write and run tests for image deletion (see TDD_SPEC_en.md, 5.3).

---

## Stage 6. UI/UX and Non-functional Requirements `[DONE]`

**Step 6.1:** Implement responsive image grid. `[DONE]`
**Step 6.2:** Add error and success messages. `[DONE]`
**Step 6.3:** Check file size and format restrictions. `[DONE]`
**Step 6.4:** Check path and upload security (see TDD_SPEC_en.md, 5.4). `[DONE]`

---

## Stage 7. Additional Features

**Step 7.1:** Implement user authentication and registration (multi-user, secure).
    - **7.1.1:** Add users table (id, username, email, password_hash) and user_id to images table. `[DONE]`
    - **7.1.2:** Implement registration page (username, email (optional), password, password confirmation). Passwords are hashed. `[DONE]`
    - **7.1.3:** Implement login/logout (sessions, password hash check). `[DONE]`
    - **7.1.4:** Store Flask secret key and DB config in .env (use python-dotenv). `[DONE]`
    - **7.1.5:** Only authenticated users can upload/delete images. Each user sees only their own images. `[DONE]`
    - **7.1.6:** Implement password reset via email (send link, set new password). `[CODED, SMTP not configured]`
    - **7.1.7:** All interface and messages in English. `[DONE]`
    - **7.1.8:** Update templates: user status, logout, registration/login links, error/success messages. `[DONE]`
**Step 7.2:** Implement viewing image on a separate page.
    - **7.2.1:** Add route and template for viewing image by id. `[DONE]`
    - **7.2.2:** Show enlarged image, caption, date, owner on separate page. `[DONE]`
    - **7.2.3:** Delete button (owner only). `[DONE]`
    - **7.2.4:** "Back to gallery" link. `[DONE]`
**Step 7.3:** Implement gallery pagination. `[DONE]`
    - **7.3.1:** Add page parameters to main route. `[DONE]`
    - **7.3.2:** Implement image selection for current page in backend. `[DONE]`
    - **7.3.3:** Add pagination navigation to gallery template. `[DONE]`
    - **7.3.4:** Test pagination. `[DONE]`

---

## Note

After each stage, run corresponding tests from TDD_SPEC_en.md and record the result. 