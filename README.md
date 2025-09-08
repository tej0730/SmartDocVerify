## 📄 SmartDocVerify

SmartDocVerify is a Django + DRF project for **document upload and verification** using **OCR (Tesseract)** and **basic field extraction** (e.g., Aadhaar, PAN, Driving License, Marksheet).

### 🚀 Features

* Upload PDF or image documents (Aadhaar, PAN, DL, Marksheet).
* Store raw OCR text and normalized structured fields.
* Verify documents (set status: Pending, Verified, Rejected).
* REST API endpoints for upload & verification.
* Extensible for AI/ML based field parsing later.

---

### ⚙️ Tech Stack

* **Backend:** Django 5 + Django REST Framework
* **Database:** SQLite (default, can switch to PostgreSQL)
* **OCR:** Tesseract OCR + pdfplumber + pdf2image
* **Frontend (planned):** React.js

---

### 📂 Project Structure

```
SmartDocVerify/
│
├── backend/
│   ├── core/               # Core Django project
│   ├── documents/          # App handling document upload & verification
│   ├── manage.py
│   ├── db.sqlite3
│
├── venv/                   # Virtual environment
├── .gitignore
├── README.md
```

---

### 🛠️ Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/tejdoshi/SmartDocVerify.git
cd SmartDocVerify/backend
```

#### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Linux/Mac
```

#### 3. Install Requirements

```bash
pip install -r requirements.txt
```

#### 4. Install Dependencies

* [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
* [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/) (for pdf2image)

#### 5. Run Migrations

```bash
python manage.py migrate
```

#### 6. Start Development Server

```bash
python manage.py runserver
```

Visit API at:
👉 `http://127.0.0.1:8000/api/documents/`
