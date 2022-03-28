import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv
import math

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()


def random_set_of_mean(counter):

      dataset = []
      for i in range(0, counter):
            random_index= random.randint(0,len(data))
            value = data[random_index]
            dataset.append(value)
      mean = statistics.mean(dataset)
      std_deviation = statistics.stdev(dataset)
      return mean

      print("Mean of 1000 values :- ",mean)
      print("std_deviation of 1000 values :- ",std_deviation)

def setup():
      mean_list = []
      for i in range(0,100):
            set_of_means= random_set_of_mean(30)
      
            mean_list.append(set_of_means)
      show_fig(mean_list)

def show_fig(mean_list):
      df = mean_list 
      fig = ff.create_distplot([df],["temp"],show_hist=False)
      fig.show()                       

setup()