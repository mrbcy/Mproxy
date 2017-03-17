#-*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

mailto_list = ['yang@ricearmy.com']
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = ""  # 用户名
mail_pass = ""  # 口令
mail_postfix = "qq.com"  # 发件箱的后缀

def send_mail(to_list, sub, content):
    me = "Mproxy" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.quit()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    try:
        a = 1 / 0
    except Exception as e:
        content = "尊敬的管理员您好，您收到这封邮件是因为我们的短信接口出现了问题，无法向运维人员发送短信。" \
                  "\n\n尝试发送的短信内容如下：\n %s \n\n发送过程中出现的异常为：%s" % ("快代理爬虫运行过程中出错",e.message)
        if send_mail(mailto_list, "Mproxy短信接口异常", content):
            print "发送成功"
        else:
            print "发送失败"