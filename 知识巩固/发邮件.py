#发邮件的库
import smtplib
#邮件文本
from email.mime.text import MIMEText

# SMTP服务器
SMTPServer="smtp.163.com"

#发邮件的地址
Sender="c1102788982@163.com"

#授权密码
passwd=""

#设置发送的内容
message="sdfsdg"

#转换成邮件文本
msg=MIMEText(message)

#标题
msg["Subject"]="sdfgsf"
#发送者
msg["From"]=Sender


#创建SMTP服务器
mailServer=smtplib.SMTP(SMTPServer,25)

#登录邮箱
mailServer.login(Sender,passwd)

#发送邮件
mailServer.sendmail(Sender,[],msg.as_string())

#退出邮箱
mailServer.quit()