import requests 
import json 
import pandas as pd 
#AREA EXTENT COORDINATE WGS4 
lon_min,lat_min=-125.974,30.038
lon_max,lat_max=-68.748,52.214
user_name=''
password=''
url_data='https://'+user_name+':'+password+'@opensky-network.org/api/states/all?'+'lamin='+str(lat_min)+'&lomin='+str(lon_min)+'&lamax='+str(lat_max)+'&lomax='+str(lon_max)
response=requests.get(url_data).json()
col_name=[]
