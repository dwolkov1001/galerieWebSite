# Image Gallery — Technical Specification and TDD

## 1. Project Description

**Image Gallery** — a web application for uploading, viewing, and deleting images. Technologies: Python (Flask), HTML/CSS, SQLite.

---

## 2. Functional Requirements

### 2.1. Main page (`/`)
- Displays all uploaded images in a grid.
- Each image has a "Delete" button.
- There is a button/link to "Upload new image".

### 2.2. Upload page (`/upload`)
- Form for uploading an image (input type="file").
- Field for image caption (optional).
- "Upload" button.
- After successful upload — redirect to main page.

### 2.3. Delete image (`/delete/<id>`)
- Clicking "Delete" removes the image from the database and disk.
- After deletion — redirect to main page.

### 2.4. Theme system
- Toggle between light and dark themes in the header.
- Selected theme is saved in browser localStorage.
- Smooth transitions between themes (CSS transitions).
- Toggle icon changes depending on current theme (🌙/☀️).

---

## 3. Non-functional Requirements

- Max file size — 5 MB.
- Allowed formats: jpg, jpeg, png, gif.
- All images are stored in a separate folder on the server.
- File info (name, path, caption, upload date) is stored in the database (SQLite).
- Theme system works without page reload (JavaScript).
- Dark theme is comfortable for low-light viewing.

---

## 4. Database Structure

**Table `images`:**
- `id` (INTEGER, PRIMARY KEY)
- `filename` (TEXT)
- `caption` (TEXT, nullable)
- `upload_date` (DATETIME)
- `user_id` (INTEGER, FOREIGN KEY to users)

**Table `users`:**
- `id` (INTEGER, PRIMARY KEY)
- `username` (TEXT, UNIQUE)
- `email` (TEXT, UNIQUE, nullable)
- `password_hash` (TEXT)

---

## 5. Tests (TDD)

### 5.1. Image upload tests
- [x] Upload a valid file — appears in the gallery.
- [x] Upload a file > 5 MB — error.
- [x] Upload a file of disallowed format — error.
- [x] Upload a file with caption — caption is displayed.

### 5.2. Gallery display tests
- [x] After uploading, image appears on main page.
- [x] If no images — "No images" message is shown.

### 5.3. Image deletion tests
- [x] After deletion, image disappears from gallery and is removed from disk.
- [x] Attempt to delete non-existent image — error handled gracefully.

### 5.4. Security tests
- [x] Attempt to upload malicious file — file is not saved.
- [x] File path does not allow escaping uploads folder.

### 5.5. Theme system tests
- [x] On page load, saved theme from localStorage is applied. (Manually checked)
- [x] Clicking toggle changes theme instantly. (Manually checked)
- [x] Selected theme is saved in localStorage. (Manually checked)
- [x] Toggle icon matches current theme. (Manually checked)
- [x] CSS variables apply correctly for both themes. (Manually checked)
- [x] Transitions between themes are smooth. (Manually checked)
- [x] Dark theme is readable and high-contrast. (Manually checked)

### 5.6. Authentication and multi-user tests
- [ ] Registration: new user can register (username, email, password; password is hashed in DB).
- [ ] Registration: duplicate username/email is rejected.
- [ ] Login: user can log in with correct credentials, session is set.
- [ ] Login: wrong username or password — login denied.
- [ ] Logout: user session is cleared.
- [ ] Only authenticated user can upload/delete images.
- [ ] User sees only their own images in gallery.
- [ ] Password reset: user can request reset, receives email, sets new password.
- [ ] All interface and messages are in English.
- [ ] Security: passwords never stored in plain text, secrets in .env.

---

## 6. Project Structure Example

```
galerieWebSite/
├── app.py
├── database.py
├── requirements.txt
├── .env.example
├── README.md
├── TDD_SPEC_en.md
├── TECHNICAL_PLAN_en.md
├── templates/
│   ├── index.html
│   ├── image.html
│   ├── login.html
│   ├── register.html
│   ├── forgot.html
│   ├── reset.html
│   └── upload.html
├── static/
│   ├── style.css
│   ├── theme.js
│   └── uploads/
└── database.db
```

---

## 7. UI/UX

- Image grid, responsive layout.
- Buttons with clear labels.
- Error and success messages.
- Theme toggle in header.
- Smooth theme transitions.
- Dark theme with muted colors for comfortable viewing.

---

## 8. Optional

- User authentication (only owner can delete their images).
- View image on separate page.
- Pagination (if many images). 
