
import requests
 
url = "http://127.0.0.1:8080/TDML_Replenishment_Model"
headers = {'Content-Type': 'application/json'}
data = [{
    "transaction_code":306,
    "transaction_name":"Replenishment (Put)",
    "transaction_month":10,
    "warehouse_id":850,
    "sku_number":"50014535",
    "before_quantity":60
    }
    ]
 
response = requests.post(url, json=data, headers=headers)
print(response.json())
 