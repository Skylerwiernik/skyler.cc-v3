import os, smtplib, ssl
import requests
from flask import Flask, render_template, request
from exports import exports
import mailer
app = Flask(__name__)





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
        "secret": exports["reCAPTCHA_secret"],
        "response": request.form.get("g-recaptcha-response"),
        "remoteip": request.remote_addr
    }).json()
    print(reCAPTCHAresponse)
    if not reCAPTCHAresponse["success"]:
        return render_template("contact.html", page="contact", success=False)
    if reCAPTCHAresponse["score"] > 0.5:
        port = 587
        smtp_server = "smtppro.zoho.com"
        sender_email = "server@skyler.cc"
        receiver_email = "skyler@skyler.cc"
        password = exports["server_mail_password"]

        name = request.form.get("name")
        email = request.form.get("email")
        body = request.form.get("message")
        uid = request.form.get("uid")
        # message = ("From: {request.form.get("name")} <server@skyler.cc>\nTo: Skyler Wiernik <{receiver_email}>\nReply-To:{request.form.get("email")}\nSubject: Email via contact form at skyler.cc/contact!\n\n{request.form.get("message")}\nSend response to: {request.form.get("email")}\nUID = {request.form.get("uid")}")
        message = ("From: {name} <{sender_email}>\n"
                   "To: Skyler Wiernik <{receiver_email}>\n"
                   "Reply-To:{email}\n"
                   "Subject: Email via contact form at skyler.cc/contact!\n\n"
                   "{body}\n\n"
                   "--\n"
                   "Send response to {email}\n"
                   "UID: {uid}"
                   ).format(name=name, sender_email=sender_email, receiver_email=receiver_email, email=email, body=body, uid=uid)
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        connection = smtplib.SMTP(smtp_server, port)
        # connection.starttls(context=context)
        connection.starttls()
        connection.login(sender_email, password)
        connection.sendmail(sender_email, receiver_email, message)
        return render_template("contact.html", page="contact", success=True)
    else:
        return render_template("contact.html", page="contact", success=False)


@app.rputer("/mail")
def mail():
    return render_template("mail.html")


@app.route("/lstoday/privacy")
def lstodayPrivacy():
   return render_template("out.html", externalLink="https://docs.google.com/document/d/1ER7pOZfww2bzjiLFC_zFnS3EK_b69Uip4dOJ0-HIadA/edit?usp=sharing")

@app.route("/lstoday/terms")
def lstodayTerms():
    return render_template("out.html", externalLink="https://docs.google.com/document/d/1sxxzSVaGb1wtm1_MfVDgiWnXOTxmSzLD701fSiI6P0Y/edit?usp=sharing")

@app.route("/lstoday")
def lstoday():
    return flask.redirect("https://skyler.cc/out/lstoday")

@app.route("/debug/version")
def version():
    return open("version.txt", "r").read()

if __name__ == '__main__':
    app.run()
