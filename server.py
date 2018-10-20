from flask import Flask,render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def index():
    if 'Wins' not in session:
        session['Wins'] = 0
        session['Losses'] = 0
        session['Ties'] = 0
    return render_template('index.html')

@app.route('/process_play', methods=['POST'])
def process_play():
    choices = ['Rock','Paper','Scissors']
    computer_choice = random.choice(choices)
    result = {
        'Rock':{
            'Rock':'Ties',
            'Paper':'Losses',
            'Scissors':'Wins'
        },
        'Paper':{
            'Rock':'Wins',
            'Scissors':'Losses',
            'Paper':'Ties'
        },
        'Scissors':{
            'Rock':'Losses',
            'Paper':'Wins',
            'Scissors':'Ties'
        }
    }
    session[result[request.form['player_choice']][computer_choice]]+=1
    return redirect ('/')

@app.route('/reset')
def reset():
    if 'Wins' in session:
        session['Wins'] = 0
        session['Losses'] = 0
        session['Ties'] = 0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)