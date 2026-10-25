from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return "Please fill in every field.", 400

    with open("messages.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M} | {name} | {email}\n{message}\n\n")

    return 'Thanks, your message was sent! <a href="http://127.0.0.1:5500/contact.html">Back</a>'

if __name__ == "__main__":
    app.run(debug=True)
