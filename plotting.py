import pandas as pd
import plotly.express as px
import requests as rq

import json
import os

input_variable = os.environ['INPUT_STORE']

url =('https://nba-stats-db.herokuapp.com/api/playerdata/name/'+input_variable)



response=rq.get(url)

try:
    if response.status_code == 200 :
        df=json.loads(response.text)
        dt=df["results"]
        dat=[]
        for i in range(len(dt)):
            d=dt[i]
            dat.append(
                {
                    'Season':d["season"],
                    'Points':d["PTS"],
                    'PlayerName':d["player_name"]
                }
                )  
        data_frame=pd.DataFrame(dat)
        title='Players Points in Each Season' 
        plot=px.bar(data_frame,x='Season',y='Points',color='PlayerName',title=title)
        plot.show()
    else:
        print(f"Error: {response.status_code}")

except Exception as e:
    print(e)
