import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

class mclass:
    def __init__(self):
        print("iam inside")
    def sendname(self,sname,to="yadavraj2705@gmail.com"):
        fromaddr = "ugendarraj2002@gmail.com"
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
    
        # start TLS for security 
        s.starttls() 
    
        # Authentication 
        s.login(fromaddr, "cxoepxjecfddhbxy")
    
        # message to be sent 
        message = sname
    
        # sending the mail 
        s.sendmail("ugendarraj2002@gmail.com", "yadavraj2705@gmail.com", message) 

        # terminating the session 
        s.quit()
    def multimediamail(self,subj):
        
        body="Message from Headquaters"
        fromaddr = "ugendarraj2002@gmail.com"
        toaddr = "yadavraj2705@gmail.com"
           
        # instance of MIMEMultipart 
        msg = MIMEMultipart() 
          
        # storing the senders email address   
        msg['From'] = fromaddr 
          
        # storing the receivers email address  
        msg['To'] = toaddr 
          
        # storing the subject  
        msg['Subject'] = subj
          
        # attach the body with the msg instance 
        msg.attach(MIMEText(body, 'plain')) 
          
        # open the file to be sent  
        filename = "still.jpeg"
        attachment = open("./still.jpeg", "rb") 
          
        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream') 
          
        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 
          
        # encode into base64 
        encoders.encode_base64(p) 
           
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
          
        # attach the instance 'p' to instance 'msg' 
        msg.attach(p) 
          
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587) 
          
        # start TLS for security 
        s.starttls() 
          
        # Authentication 
        s.login(fromaddr, "cxoepxjecfddhbxy")
          
        # Converts the Multipart msg into a string 
        text = msg.as_string() 
          
        # sending the mail 
        s.sendmail(fromaddr, toaddr, text) 
          
        # terminating the session
        print("mail sent")
        s.quit()
    
    
#ob=mclass()
#ob.newsbbc()
# ob.weather()
#ob.multimediamail("Tresspasser allert from Lucy !!")
#ob.sendname(sname="Hello UGENDAR RAJ")
