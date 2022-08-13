import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df   = pd.read_csv("medium_data.csv\medium_data.csv")
data = df["claps"].tolist()
popuation_mean = statistics.mean()
std_dev        = statistics.stdev(data)

print("Population Mean = "    , popuation_mean)
print("Standard deviation = " , std_dev)

def random_set_of_mean(counter):
   

    mean_list = []
    for i in range(0 , counter):
        random_index = random.randint(0 , len(data)-1)
        value        = data[random_index]
        mean_list.append(value)

    mean = statistics.mean(mean_list)
    return mean

def show_fig(mean_list):
    df   = mean_list
    mean = statistics.mean(df)
    fig  = ff.create_distplot([df] , ["Claps"] , show_hist=False)
    fig.add_trace(
        go.Scatter(
            x    =  [mean , mean] ,
            y    = [0,1] , 
            mode = "lines" , 
            name = "Mean"
        )
    )
    fig.show()

def setup() :
    mean_list = []

    for i in range(0 , 1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)

    show_fig(mean_list)
    mean = statistics.mean(mean_list)

    print("Mean of the sampling distribution = " , mean)

setup()

def std_dev():
    mean_list = []

    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)

    std_dev = statistics.stdev(mean_list)

    print("Standard Deviation of the sampling Distribution : " , std_dev)

std_dev()

# Standard deveation

first_std_dev_start , first_std_dev_end = popuation_mean-std_dev , popuation_mean+std_dev
second_std_dev_start , second_std_dev_end = popuation_mean-(2*std_dev) , popuation_mean+(2*std_dev)
third_std_dev_start , third_std_dev_end = popuation_mean-(3*std_dev) , popuation_mean+(3*std_dev)


df = pd.read_csv("data1.csv")
data=df["Math_score"].tolist()

mean_of_sample_1 = statistics.mean(data)

print("Mean of sample 1 = " , mean_of_sample_1)

fig  = ff.create_distplot([popuation_mean] , ["Student Marks"] , show_hist=False)
fig.add_trace(go.Scatter(x = [popuation_mean , popuation_mean],y = [0,0.17],mode = "lines",name = "Mean"))
fig.add_trace(go.Scatter(x = [mean_of_sample_1 , mean_of_sample_1],y = [0,0.17],mode = "lines",name = "Mean of the Sample 1"))
fig.add_trace(go.Scatter(x = [first_std_dev_end , first_std_dev_end],y = [0,0.17],mode = "lines",name = " First Standard Deviation End"))
fig.add_trace(go.Scatter(x = [second_std_dev_end , second_std_dev_end],y = [0,0.17],mode = "lines",name = " Second Standard Deviation End"))
fig.add_trace(go.Scatter(x = [third_std_dev_end , third_std_dev_end],y = [0,0.17],mode = "lines",name = " thirdStandard Deviation End"))

fig.show()

z_score = (popuation_mean-mean_of_sample_1)/std_dev
print("The Z score of sample 1 is " , z_score)

