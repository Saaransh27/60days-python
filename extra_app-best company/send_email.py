import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "saaranshjain2709@gmail.com"
    password = "emkrccieckinumxd"

    reciever = "saaranshjain2709@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)