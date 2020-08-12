import yagmail

def send_email(sender, contents):

    """yagmail is a library to manage google smtp in a more simpler manner,
    for more information, visit https://github.com/kootenpv/yagmail"""

    USERNAME = 'cortexsilicon'
    APP_PASSWORD = 'jnzbhrbqcsavnlhu'

    yag = yagmail.SMTP(USERNAME, APP_PASSWORD) #input the email username and app password

    SEND_TO = ['lesliecaminade@gmail.com'] #this will be a list of receivers
    SUBJECT = f"""From: {sender} via caminadeshop.pythonanywhere.com"""
    CONTENTS = contents

    yag.send(to = SEND_TO, subject = SUBJECT, contents = CONTENTS) #send the email

if __name__ == '__main__':
    send_email()
