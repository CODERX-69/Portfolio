from flask import Flask , render_template , redirect , url_for , request, flash
from dotenv import load_dotenv
load_dotenv()
import os
from  flask_mail import Mail , Message

app = Flask(__name__ , template_folder='templates')


app = Flask(__name__)



app.config['USER_ENABLE_EMAIL'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME']= 'sejal.officialmail@gmail.com'
app.config['MAIL_PASSWORD'] = 'ajrlvdrwiswjypey'                             


mail = Mail(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send_mail', methods = ['POST'])
def send_mail():
    email = request.form['email']
    name = request.form['name']
    subject = request.form['subject'] 
    msg = Message(subject="hello",
        sender= 'sejal.officialmail@gmail.com',
        recipients=['sejal.officialmail@gmail.com'] )
    msg.html= f'You have received a new message!\n<b>Name :</b>{name}\n<b>Email :</b>{email}\n<b>Message :</b>{subject}'
    mail.send(msg)
    msg = Message(subject="hello",
        sender= 'sejal.officialmail@gmail.com',
        recipients=[email] ) 
    msg.body = f'Hello , {name}! I have received your response,I will get back to you shortly.'
    mail.send(msg)
    return redirect(url_for('index'))


   
       
if __name__=="__main__": 
    app.secret_key = "jnfjgjr"  
    app.run(debug=True , port=5000)