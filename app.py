from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=586
app.config['MAIL_USERNAME']='kawinec.k.ece.2021@snsct.org'
app.config['MAIL_PASSWORD']= os.environ.get('PASSWORD')
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
@app.route('/home', methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        msg=Message("Hey",sender='noreply@demo.com', recipients='kawinhari8@gmail.com')
        msg.body="This is the body of the message"
        mail.send(msg)
        return 'Sent Email'
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
    