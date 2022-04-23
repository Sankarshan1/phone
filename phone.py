import csv
import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv('p.csv')



fig2=ff.create_distplot([df["Avg Rating"].tolist()],["Rating"],show_hist=False)

fig2.show()
