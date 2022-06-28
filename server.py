from flask import Flask, render_template, request
import database
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/forms')
def form():
    return render_template('submit.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    birthday=request.form.get('birthday')
    phonenumber=request.form.get('phonenumber')
    messages=request.form.get('messages')
    if request.method == 'GET':
        birthday=request.form.get('birthday')
        phonenumber=request.form.get('phonenumber')
        messages=request.form.get('messages')

    if (birthday and phonenumber and messages):
        print(birthday)
        print(phonenumber)
        print(messages)
        #database
        database.clean(birthday,phonenumber,messages)
        return render_template('main.html')
    else:
        return "Finish your form"
        

if __name__=="__main__":
    app.run()