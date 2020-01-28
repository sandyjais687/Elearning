import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("sandyjais687@gmail.com", "Symb@venom") 
  
# message to be sent 
message = "Message_you_need_to_send"
  
# sending the mail 
s.sendmail("sender_email_id", "sandyjais687@outlook.com", message) 
  
# terminating the session 
s.quit() 
