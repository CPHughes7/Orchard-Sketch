import matplotlib.pyplot as plt

def generate_orchard_map(x, y):
    fig, ax = plt.subplots()
    ax.scatter(x, y, marker='o', color='green')
    ax.set_title("Orchard Map")
    ax.set_xlabel("X coordinate")
    ax.set_ylabel("Y coordinate")
    fig.save_fig('my_file.png') 
    #plt.show()