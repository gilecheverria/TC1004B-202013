"""
First plots using matplotlib

Install Matplotlib using
    pip install matplotlib

Gilberto Echeverria
13/11/2020
"""

import random
import matplotlib.pyplot as plt

def create_graph(data, filename):
    plt.title("Graph or random data")
    plt.xlabel("Items")
    plt.ylabel("Values")
    plt.plot(data)
    plt.savefig(filename)
    #plt.show()
    print(f"Image {filename} generated")



data = [random.randint(1, 100) for i in range(500)]
create_graph(data, "new_graph.png")

