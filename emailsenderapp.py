import smtplib

def sendMemo(to,subject,body):
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)

    f = open("Passwords.txt")
    L = f.readlines()

    username = L[3].strip('\n')
    password = L[4].strip('\n')
    server.login(username,password)

    message = f'Subject:{subject}\n\n{body}'

    server.sendmail(username,to,message)

    print("Memo Sent!")

    server.quit()
