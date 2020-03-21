from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    order = {}
    order['strawberry'] = int(request.form['strawberry'])
    order['raspberry'] = int(request.form['raspberry'])
    order['apple'] = int(request.form['apple'])
    order['sum'] = order['strawberry']+order['raspberry']+order['apple']
    user = {}
    user['firstName']=request.form['first_name']
    user['lastName'] = request.form['last_name']
    user['id'] = request.form['student_id']
    print('Charging ' + user['firstName'] + " " + user['lastName'] + " for ", order['sum'], ' fruits')
    return render_template("checkout.html", order=order, user=user)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    