
import matplotlib.pyplot as plt

dots = [(x, y) for y in range(3) for x in range(3)]
path = [(-1, -1), (2, 2), (-1, 2), (2, -1), (2, 1)]
xs, ys = zip(*dots)
plt.scatter(xs, ys, s=80)
px, py = zip(*path)
plt.plot(px, py, linewidth=3, marker='o')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
