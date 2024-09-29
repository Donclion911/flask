from flask import Flask,render_template,request,redirect,session
from uvas.embassy import Embassies
from uvas.visa import *

app = Flask(__name__)
app.secret_key = 'donclion911'

@app.route('/',methods=['GET','POST'])
def index():
    feedback=request.args.get('feedback')
    return render_template('index.html',embassies=Embassies,feedback=feedback)

@app.route('/submit', methods=['POST'])
async def submit():
    feedback=''
    if request.method == 'POST':
        form_data=request.form
        try:
            send_notification("testing","rrrr")
            initProperties(form_data)
            feedback='well done'
        except:
            feedback='break down,try agian..'
        return redirect(f'/?feedback={feedback}',code=302)

if __name__ == '__main__':
    app.run(port=5001,debug=True)  # Change the port number to 5001 or any other available port