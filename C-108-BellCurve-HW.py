import plotly.figure_factory  as ff
import plotly.express as px
import pandas as pd
import csv

from google.colab import files
data_to_load = files.upload()

v1=pd.read_csv("data108-HW.csv")
graph=ff.create_distplot([v1["Avg Rating"].tolist()],["Average Rating"],show_hist=True)
graph.show()
