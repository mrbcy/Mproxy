#-*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

from conf.configloader import ConfigLoader


class EmailUtil:
    conf_loader = ConfigLoader()

    @classmethod
    def send_email(cls,sms_content,exception_info):
        mailto_list = cls.conf_loader.get_mail_to_list()
        mail_host = "smtp.qq.com"
        mail_user = cls.conf_loader.get_mail_username()
        mail_pass = cls.conf_loader.get_mail_password()
        mail_postfix = "qq.com"
        sub = "Mproxy短信接口异常"

        content = "尊敬的管理员您好，您收到这封邮件是因为我们的短信接口出现了问题，无法向运维人员发送短信。" \
                  "\n\n尝试发送的短信内容如下：\n%s \n\n发送过程中出现的异常为：\n%s" % (sms_content,exception_info)

        me = "Mproxy" + "<" + mail_user + "@" + mail_postfix + ">"
        msg = MIMEText(content, _subtype='plain', _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(mailto_list)
        try:
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)
            server.connect(mail_host)
            server.login(mail_user, mail_pass)
            server.sendmail(me, mailto_list, msg.as_string())
            server.quit()

        except Exception, e:
            print str(e)
