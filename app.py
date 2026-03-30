from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/reels")
def reels():
    return render_template("reels.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
