import flask
from flask import request
from flask import render_template
app = flask.Flask(__name__)
app.config["DEBUG"] = True
import pickle
from flask_cors import CORS
CORS(app)

# main index page route
@app.route('/')
def home():
     return render_template('index.html')

@app.route('/predict',methods=['GET'])
def predict():

    with open(r'picklee\model.pkl','rb') as f:
        model = pickle.load(f)
    print([int(request.args['gender']),
                            int(request.args['religion']),
                            int(request.args['caste']),
                            int(request.args['mother_tongue']),
                            int(request.args['country']),
                            int(request.args['height_cms']),
                           ])
    age = model.predict([[int(request.args['gender']),
                            int(request.args['religion']),
                            int(request.args['caste']),
                            int(request.args['mother_tongue']),
                            int(request.args['country']),
                            int(request.args['height_cms']),
                           ]])
    return str(age[0])
 


if __name__ == "__main__":
    app.run(debug=True)