import requests
vagons =requests.get("https://rwl.artport.pro/commercialAgent/hs/CarrWorkApp/VagonInfo").json()["Vagons"]