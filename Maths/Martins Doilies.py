import matplotlib.pyplot as plt
from numpy import sign, empty

def make_plot(x, y, a, b, c, filename, N=20000):
    xs = empty(N)
    ys = empty(N)
    for n in range(N):
        x, y = y - sign(x)*abs(b*x - c)**0.5, a - x
        xs[n] = x
        ys[n] = y
    plt.scatter(xs, ys, c='k', marker='.', s = 1, alpha=0.5)
    #plt.axes().set_aspect(1)
    plt.axis('off')
    plt.savefig(filename)
    plt.show()
    plt.close()

make_plot(5, 5, 30.5, 2.5, 2.5, "doiley1.png")
make_plot(5, 6, 30, 3, 3, "doiley2.png")
make_plot(3, 4, 5, 6, 7, "doiley3.png")