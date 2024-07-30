import pickle
from flask import Flask, app, jsonify, request
import pandas as pd 
from sklearn.preprocessing import StandardScaler
 
app = Flask(__name__)
						
def Replenishment(df, encoder):
    data1 = df.copy()
    
    cat_features = ['transaction_name', 'sku_number']

    # Encode the categorical features
    for col in cat_features:
        data1[col] = encoder[col].fit_transform(data1[col])
        
    # Scale the features
    scaler = StandardScaler()
    data1 = scaler.fit_transform(data1)

    #data = data1[['transaction_code', 'transaction_name', 'transaction_month', 'warehouse_id', 'sku_number', 'before_quantity']]
    return data1

# Load the model from the pickle file
with open(r'C:\Users\USER\Desktop\Replenishment\Replenishment_pickle.pkl', 'rb') as f:
   model_TDML_Replenishment_Model = pickle.load(f)
 
# Define a route to accept POST requests for predictions - predict1
@app.route('/TDML_Replenishment_Model', methods=['POST'])
def TDML_Replenishment_Model():
    # Get the text inputs from the request
    print(type(model_TDML_Replenishment_Model))
    data = request.get_json()
    df=pd.DataFrame(data)
    encoder = model_TDML_Replenishment_Model['encoders']

    # Make predictions using the loaded model for each text input
    df = Replenishment(df,encoder)
    model = model_TDML_Replenishment_Model['model']
    #model = get_model(model_TDML_Replenishment_Model)
    predictions =  model.predict(df)
    predictions_list = [round(pred) for pred in predictions]
    # Return the predictions as a JSON response
    return jsonify({"results": predictions_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)