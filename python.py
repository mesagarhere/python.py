from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password:
            return f"<h3>Welcome, {username}!</h3>"
        else:
            return "<h3 style='color:red;'>Error: Please fill in all fields.</h3>"
    
    return '''
    <form method="post">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
