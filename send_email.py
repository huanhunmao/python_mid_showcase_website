import smtplib, ssl, os


def send_email():
    host = 'smtp.gmail.com'
    port = 465

    username = 'markfu1996@gmail.com'
    # 和 js 不一样 不是单独 .env 文件 写在系统 环境变量中  open ~/.zshrc
    password = os.getenv('PASSWORD_EMAIL')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
send_email()