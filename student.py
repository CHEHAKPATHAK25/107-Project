#importing modules
import pandas as pd
import plotly.express as px

#read csv data using pd module
dataframe = pd.read_csv("data.csv")

#selecting a particular student
#finding the mean of student of attempts in each level
#creating a graph

mean = dataframe.groupby(["student_id", "level"], as_index=False) ["attempt"].mean()
scatter_graph = px.scatter(mean, x="student_id", y="level", color="attempt", size="attempt")
scatter_graph.show()