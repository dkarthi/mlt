import pandas as pd
import sys
import matplotlib.pyplot as plt

def plot(stock):
    df=pd.read_csv("data/{0}.csv".format(stock))
    df[['Volume','Close']].plot()
    plt.show()


def get_mean_volume(stock):
    df=pd.read_csv("data/{0}.csv".format(stock))
    return df['Volume'].mean()

def get_max_close(stock):
    df=pd.read_csv("data/{0}.csv".format(stock))
    return df['Close'].max()

def get_min_close(stock):
    df=pd.read_csv("data/{0}.csv".format(stock))
    return df['Close'].min()
    
def test_run():
    stock = sys.argv[1]
    stock_data = "data/{0}.csv".format(stock)
    df=pd.read_csv(stock_data)
    print "max close is {0},min close is {1} and mean is {2}".format(get_max_close(stock),get_min_close(stock),get_mean_volume(stock))
    #plot(stock)
    print df.tail()

if __name__ == "__main__":
    test_run()

    
