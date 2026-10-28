
from flask import Flask, request

app = Flask(__name__)
emails = []

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        email = request.form["email"].strip().lower()

        if email in emails:
            message = "Duplicate data!"
        else:
            emails.append(email)
            message = "Data saved successfully!"

    return f"""
    <h1>CodeAlpha - Data Redundancy Removal System</h1>
    <form method="post">
        <input name="email" type="email" required
        placeholder="Enter email">
        <button type="submit">Save Data</button>
    </form>
    <h3>{message}</h3>
    <h3>Stored Emails</h3>
    <p>{', '.join(emails)}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
