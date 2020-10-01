import os, smtplib, ssl
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

enviorment_var_keys = ["reCAPTCHA_secret", "server_mail_password"]

for key in enviorment_var_keys:
    if not os.environ.get(key):
        raise RuntimeError("Missing environment key ", key)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/")
def home():
    return render_template("home.html", page="home")


@app.route("/about")
def about():
    return render_template("about.html", page="about")

@app.route("/projects/<string:project>")
def projects(project):
    try:
        return render_template("projects/" + project + ".html", page=project.lower())
    except:
        return render_template("404.html"), 404


@app.route("/out/<string:outRequest>")
def social(outRequest):
    from externalIndex import externalIndex
    if outRequest not in externalIndex:
        return render_template("404.html"), 404

    externalLink = externalIndex[outRequest]
    return render_template("out.html", externalLink=externalLink)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", page="contact", success=None)

    reCAPTCHAresponse = requests.post("https://www.google.com/recaptcha/api/siteverify", data={
        "secret": os.environ.get("reCAPTCHA_secret"),
        "response": request.form.get("g-recaptcha-response"),
        "remoteip": request.remote_addr
    }).json()
    if not reCAPTCHAresponse["success"]:
        return render_template("contact.html", page="contact", success=False)
    if reCAPTCHAresponse["score"] > 0.5:
        port = 587
        smtp_server = "box.skyler.cc"
        sender_email = "server@skyler.cc"
        receiver_email = "skyler@skyler.cc"
        password = os.environ.get("server_mail_password")

        message = f"""From: {request.form.get("name")} <server@skyler.cc>\nTo: Skyler Wiernik <{receiver_email}>\nReply-To:{request.form.get("email")}\nSubject: Email via contact form at skyler.cc/contact! (reCAPTCHA score: {str(reCAPTCHAresponse["score"])})\n\n{request.form.get("message")}\nSend response to: {request.form.get("email")}\nUID = {request.form.get("uid")}"""
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        connection = smtplib.SMTP(smtp_server, port)
        connection.starttls(context=context)
        connection.login(sender_email, password)
        connection.sendmail(sender_email, receiver_email, message)
        return render_template("contact.html", page="contact", success=True)
    else:
        return render_template("contact.html", page="contact", success=False)


if __name__ == '__main__':
    app.run()
