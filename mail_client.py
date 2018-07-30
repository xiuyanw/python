from email.mime.text import MIMEText
from email.header import Header
import smtplib
from getpass import getpass
mail_host='smtp.163.com'
mail_user='linux_wxy@163.com'
mail_pwd=getpass()
message=MIMEText('hello 最近好不？\n','plain','utf8')

message['From']=Header('linux_wxy@163.com','utf8')
message['To']=Header('1273405387@qq.com','utf8')
message['Subject']=Header('最近好不？','utf8')

sender='linux_wxy@163.com'
receivers=['1273405387@qq.com']
smtp_obj=smtplib.SMTP()
smtp_obj.connect(mail_host)
smtp_obj.login(mail_user,mail_pwd)
smtp_obj.sendmail(sender,receivers,message.as_string())