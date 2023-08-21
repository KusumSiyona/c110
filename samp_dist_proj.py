import pandas as pd
import csv
import random
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as gf


df = pd.read_csv("images")
data = df["images"].tolist()


#function to get the mean of the given data samples
#pass the number of data points you want as counter
def random_set_of_mean(counter):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data) -1)
        value = data[random_index]
        data_set.append(value)

    mean = st.mean(data_set)
    return mean

#function to plot the mean on the graph
def plot_graph(mean_list):
    df = mean_list
    mean = st.mean(df)
    fig = ff.create_distplot([df], ["images"] , show_hist = False)
    fig.show()

#pass the number of times you want the mean of the data points as a parameter in range of for loop
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)

    plot_graph(mean_list)

setup()

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
      
    std_dv = st.stdev(mean_list)
    print("Standard Deviation of average is " , std_dv)

standard_deviation()