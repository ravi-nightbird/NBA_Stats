import pandas as pd
import plotly.express as px
import requests as rq

import json

name=input('Enter the name of the player for which you want the stats: ')
url =('https://nba-stats-db.herokuapp.com/api/playerdata/name/'+name)



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
