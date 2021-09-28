import flask
from flask import request,render_template
import pandas as pd
from flask_cors import CORS, cross_origin

cols=["book","pg","word","definition","sentence","category","sample","synonyms"]
data = pd.read_csv('ISLT_data.csv', sep=',', engine='python', usecols=cols,na_values = [''])
json_data = data.to_json(orient = "records")
json_list = json_data.replace("\\","")
print(json_list)


app = flask.Flask(__name__,template_folder='template')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

print('***Backend Running***')

@app.route('/')
def home():
   return render_template('create.html')
@app.route('/getData',methods=['GET'])
def getData():
    return json_list
@app.route('/sendData', methods=['POST']) 
@cross_origin()
def sendData():
    postData= pd.json_normalize(request.form)
    newData = pd.concat([data,postData],ignore_index=True)
    # adding new data into csv
    newData.to_csv('ISLT_data.csv',index=False)
    return request.form
    
if __name__ == '__main__':
    app.run()
