import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('../data/csv/data.csv')
    x = df["SalesID"].as_matrix()
    y = df["ProductPrice"].as_matrix()
    plt.xlabel("SalesID")
    plt.ylabel("ProductPrice")
    plt.title("Sales Analysis")
    plt.plot(x, y)
    plt.show()
