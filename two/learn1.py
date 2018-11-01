import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "190065838@qq.com"
receiver = "1064807182@qq.com"
message = MIMEText('Python邮件发送测试', 'plain', 'utf-8')
message['From'] = Header("菜鸟", 'utf-8')
message['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
try:
    smtpObj = smtplib.SMTP("localhost")
    smtpObj.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error：无法发送邮件")

