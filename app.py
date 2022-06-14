from flask import Flask, request,redirect,url_for, jsonify, render_template,session
from game_module import *
app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def home():
    msg=''
    if request.method == 'POST':
        if "choice" in request.form:
            choice = request.form['choice']
            row ,col = mapper(int(choice))
            print(row,col)
            msg = play(row,col)

        if "reset" in request.form:
            reset()
            msg=''


    return render_template('index.html',maze=maze,msg=msg,player=player,computer=compute)
@app.route('/hard',methods=["GET", "POST"])
def hard():
    msg=''
    if request.method == 'POST':
        if "choice" in request.form:
            choice = request.form['choice']
            row ,col = mapper(int(choice))
            print(row,col)
            msg = play_hard(row,col)

        if "reset" in request.form:
            reset()
            msg=''


    return render_template('index_hard.html',maze=maze,msg=msg,player=player,computer=compute)

@app.route('/medium',methods=["GET", "POST"])
def medium():
    msg=''
    if request.method == 'POST':
        if "choice" in request.form:
            choice = request.form['choice']
            row ,col = mapper(int(choice))
            print(row,col)
            msg = play_medium(row,col)

        if "reset" in request.form:
            reset()
            msg=''


    return render_template('index_medium.html',maze=maze,msg=msg,player=player,computer=compute)

@app.route('/decide',methods=["GET", "POST"])
def decide():
    if request.method == 'POST':
        select = request.form['myselect']
        if select == 'easy':
            reset()
            player[0] = 0
            compute[0] = 0
            return redirect(url_for('home'))
        elif select == 'medium':
            reset()
            player[0] = 0
            compute[0] = 0
            return redirect(url_for('medium'))
        else:
            reset()
            player[0] = 0
            compute[0] = 0
            return redirect(url_for('hard'))


if __name__ == "__main__":
    app.run(debug=True)