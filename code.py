import plotly.figure_factory as ff
import csv
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
def random_set_of_mean (counter):
  dataset = []
  for i in range(0, counter):
    random_index = random.randint(0,len(data)-1)
    value = data[random_index]
    dataset.append(value)
  mean = statistics.mean(dataset)
  return mean

mean_list = []
for i in range (0, 1000):
  set_of_means = random_set_of_mean(100)
  mean_list.append(set_of_means)
std_deviation = statistics.stdev(mean_list)

mean_of_sample1 = statistics.mean(data)
print(mean_of_sample1)
first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean+std_deviation
fig = ff.create_distplot([mean_list], ["CLAPS"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1] , y =[0, 0.17] ,mode = "lines", name = "No.of claps"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end], y = [0,0.17], mode = "lines", name ="Standard deviation"))
fig.show()
z_score = (mean_of_sample1 - mean)/std_deviation
print(z_score)