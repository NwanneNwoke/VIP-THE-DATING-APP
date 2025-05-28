from flask import Flask, render_template, request, redirect, url_for, session
import requests
import json
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Firebase Web API key 
API_KEY = "AIzaSyADx0ZoMzUqZXshz4cq0fWR5f94nxLdgHg"

# Firebase REST endpoints
FIREBASE_SIGNIN_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
FIREBASE_SIGNUP_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"
FIREBASE_VERIFY_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:lookup?key={API_KEY}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        action = request.form["action"]

        data = json.dumps({
            "email": email,
            "password": password,
            "returnSecureToken": True
        })

        if action == "signup":
            response = requests.post(FIREBASE_SIGNUP_URL, data=data)
        else:
            response = requests.post(FIREBASE_SIGNIN_URL, data=data)

        res_data = response.json()

        if "idToken" in res_data:
            session["user"] = res_data["email"]
            return redirect(url_for("dashboard"))
        else:
            error = res_data.get("error", {}).get("message", "Authentication Failed")
            return render_template("index.html", error=error)

    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("index"))
    return render_template("dashboard.html", user=session["user"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
