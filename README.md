# 💼 VIP Match: Full-Stack Salary-Based Dating Platform

**VIP Match** is a professional-grade, full-stack dating app designed to match users based on income and career compatibility. It includes a secure web application with Firebase Authentication, PDF salary extraction, RESTful Flask backend, and CLI-based salary matching. Built to showcase scalable architecture and real-world integrations.

---

## 🧩 Tech Stack Overview

| Layer            | Tools & Libraries                            |
|------------------|----------------------------------------------|
| **Frontend**     | HTML, Jinja2 (Flask Templates)               |
| **Backend**      | Python, Flask, RESTful routes                |
| **Authentication** | Firebase Auth (Email/Password)             |
| **PDF Parsing**  | PyMuPDF for extracting salary from paystubs  |
| **Environment**  | `.env`, `python-dotenv`, `requirements.txt`  |
| **DevOps**       | Git, Replit-ready, Modular Structure         |
| **Testing**      | `unittest` (planned for CLI modules)         |

---

## 🚀 Features

- 🔐 **Secure Login/Signup** using Firebase (email/password)
- 📄 **Upload PDF Paystubs** and extract gross/monthly pay
- 🤖 **Auto-calculated Salary Matching**
- 🔁 **Reusable Matching Logic** (CLI and Web shared core logic)
- 🧪 CLI Mode for script-based testing and automation
- 🌍 Ready for Replit, Render, or GitHub Pages hosting

---

## 🧭 Project Structure

```
VIP_Match_FullStack/
├── VIP/                  # CLI Matching App
│   ├── main.py
│   ├── salary_utils.py
│   ├── matching_engine.py
│   └── tests/
├── VIP_web/              # Flask Web App
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   └── dashboard.html
│   ├── static/
│   ├── uploads/
│   ├── .env.example
│   ├── .gitignore
│   └── requirements.txt
├── LICENSE
└── README.md
```

---

## 🛠️ Installation & Setup

### Prerequisites:
- Python 3.8+
- Firebase project (https://console.firebase.google.com)
- Enable Email/Password sign-in
- Get your Web API Key

### Clone & Run Locally:

```bash
git clone https://github.com/YOUR_USERNAME/vip-match.git
cd VIP_Match_FullStack/VIP_web
cp .env.example .env
# Paste your Firebase API key inside .env
pip install -r requirements.txt
python app.py
```

---

## 🔒 .env File Example

```env
# .env
FIREBASE_API_KEY=your_firebase_web_api_key_here
```

---

## 📄 Description for Employers

> VIP Match demonstrates full-stack development skills using Python and Firebase.
> It integrates secure authentication, RESTful design, real-time PDF processing, session management, and templating.
> Modular design allows for testing, scalability, and frontend/backend decoupling.

---

## 🧪 Coming Soon

- Google OAuth & LinkedIn OAuth integration
- Firestore database for persistent profiles
- Full unit test coverage
- Swipe-based UI for compatibility scores

---

## 📄 License

MIT License – 2025 VIP Match
