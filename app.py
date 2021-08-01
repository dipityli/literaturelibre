from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')
    
@app.route('/about')
def about():
    return render_template('about-us.html') 

# @app.route('/predict')
# def predict():
#     return render_template('predict.html')
    
# @app.route('/predict_form_inputs', methods=['POST'])
# def predict_form_inputs():
#     return render_template('predict.html', output=output)

# @app.route('/privacy-policy')
# def privacy_policy():
#     return render_template('privacy-policy.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)