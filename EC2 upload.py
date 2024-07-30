import requests
import json
 
# URL of the API endpoint
api_url = "http://esoft-uat-1681494035.us-east-1.elb.amazonaws.com:8089/store_data"  # Replace with your API URL
 
# Data to be sent in the POST request
data = {
    "model_name": "TDML_avg_picks_per_order",
    "bucket_name": "eslplt-data-models",
      "category": "Continuous",
      "folder_name":"TDML_avg_picks_per_order"
}
 
def post_data(api_url, data):
    try:
        # Make the POST request
        response = requests.post(api_url, json=data)
        response.raise_for_status()  # Check if the request was successful
 
        # Parse the response JSON
        response_data = response.json()
        return response_data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
 
def main():
    response_data = post_data(api_url, data)
    if response_data:
        print("Response from API:")
        print(json.dumps(response_data, indent=4))
 
if __name__ == "__main__":
    main()