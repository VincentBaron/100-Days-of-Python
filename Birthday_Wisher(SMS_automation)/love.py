import smtplib

my_email = "VinnyThePinny@gmail.com"
password = "ThePinny/300496"

with smtplib.SMTP("smtp.gmail.com") as mail:
    mail.starttls()
    mail.login(my_email, password)
    mail.sendmail(to_addrs="lafarge.nathan.3b3@gmail.com", from_addr=my_email,
                  msg="Subject: MESSAGE IMPORTANT\n\n \n\n\n\n\n\n\n\n\nPasse une bonne journee.")
    mail.sendmail(to_addrs="granger.ndr@gmail.com", from_addr=my_email,
                  msg="Subject: MESSAGE IMPORTANT\n\n \n\n\n\n\n\n\n\n\nPasse une bonne journee.")