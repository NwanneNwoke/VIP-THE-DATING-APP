# 💼💘 VIP Match: Career & Salary-Based Dating App

**VIP Match** is a dual-interface dating application that helps professionals find love based on salary compatibility and career alignment. It includes:

- A 🔧 command-line prototype for rapid matching based on last month's paystubs
- A 🌐 Flask web app with secure Firebase Authentication for user login and a personal dashboard

Whether you're testing offline or deploying online, **VIP Match** offers a modern, privacy-conscious dating solution designed for working professionals.

---

## 📦 Project Structure

```
vip-match/
├── VIP/                        # CLI app
│   ├── main.py
│   ├── salary_utils.py
│   ├── matching_engine.py
│   └── tests/
├── VIP_web/                   # Web app (Flask + Firebase)
│   ├── app.py
│   ├── requirements.txt
│   ├── templates/
│   │   ├── index.html
│   │   └── dashboard.html
│   └── static/
├── README.md
└── LICENSE
```

---

## 🧠 Features

### CLI Version
- 🔢 Generate monthly income from weekly paystubs
- 🤝 Match users by salary range and job compatibility
- 🧪 Includes unit tests for core components

### Web Version (Flask + Firebase)
- 🔐 Email/password authentication via Firebase
- 📲 Session-based dashboard
- 📤 Easy deploy to Replit or Render
- 🔧 Ready for Google OAuth and salary input form (coming soon)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/vip-match.git
cd vip-match
```

### 2. Setup the CLI App

```bash
cd VIP
python main.py
```

### 3. Run the Web App

1. Create a Firebase project
2. Enable **Email/Password** sign-in
3. Copy your Web API Key and paste it into `app.py`:
```python
API_KEY = "AIzaSyADx0ZoMzUqZXshz4cq0fWR5f94nxLdgHg"
```

4. Install dependencies and run:

```bash
cd VIP_web
pip install -r requirements.txt
python app.py
```

Visit `http://127.0.0.1:5000/` to test it live.

---

## 🔐 Security & Privacy

All authentication is handled securely via Firebase. No passwords or emails are stored locally. For enhanced security, consider implementing OAuth login via Google or LinkedIn.

---

## 🧩 Future Enhancements

- Upload paystub PDF for automatic salary parsing
- Match dashboard with swipe UI
- User profiles with avatar and bio
- Email/OTP verification
- Google and LinkedIn OAuth support

---

## 📄 License

This project is licensed under the MIT License – see `LICENSE` for details.

---

## 🧑‍💻 Authors

Built with ❤️ by [YourName] – Powered by Python, Flask, and Firebase
