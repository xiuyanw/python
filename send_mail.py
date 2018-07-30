from email.mime.text import MIMEText
from email.header import Header
import smtplib
message=MIMEText('Python 邮件发送测试。。\n','plain','utf8')

message['From']=Header('root@loaclhost','utf8')
message['To']=Header('bob@localhost','utf8')
message['Subject']=Header('mail test','utf8')

sender='root@redhat.com'
receivers=['bob@localhost','alice@localhost']
smtp_obj=smtplib.SMTP('192.168.1.254')
smtp_obj.sendmail(sender,receivers,message.as_string())

