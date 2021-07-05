import requests
import sys
import os


API_Key = os.getenv("API_Key", None)

URL = "https://api.macaddress.io/v1?apiKey={api_key}&output={output_type}&search={search_address}"

output_type = "json"


def get_data(search_address):
    url = URL.format(api_key=API_Key, output_type=output_type, search_address=search_address)
    res = requests.get(url)
    # print(res, res.content)
    # If status is 200 then the response is success else something response is failed/unsucess due to some reason
    if res.status_code == 200:
        res = res.json()
        return res["vendorDetails"]["companyName"]
    return "Please check the address beacuse the response is " + str(res.status_code)
    

def main():
    try:
        # check if APIKEY is sent from env
        if API_Key:
            # Check if we are getting argument from command line
            search_key = sys.argv[1]
            result =  get_data(search_key)
            print(result)
        else:
            print("please pass API KEY")
    except:
        print("Please pass Mac Address")


main()

# search_key = "44:38:39:ff:ef:57"