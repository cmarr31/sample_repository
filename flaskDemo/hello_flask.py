from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)    
app.secret_key = 'ThisIsSecret'
                         
@app.route('/hello_world')                                   
def hello_world():
  #return 'Hello World!, how are you today'  
  return render_template('index.html')

@app.route('/sports/<whichSport>')
def sports(whichSport):
    print whichSport
    #some database call
    
    return render_template('sports.html', sport=whichSport)

@app.route('/')
def index():
      session['form_data'] = 0
      #session.clear()
      return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def fnProcessForm():
      print request.form['first_name']
      print request.form['last_name']
      print request.form['city']
      print request.form['state']

      #session['form_data'] = request.form
      session['firstName'] = request.form['first_name']
      session['lastName'] = request.form['last_name']

      return redirect('/display_form')

@app.route('/display_form')
def display_form():
      return render_template('displayOutput.html', formData=session['form_data'])
    
app.run(debug=True)      