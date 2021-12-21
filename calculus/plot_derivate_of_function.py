import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from scipy.interpolate import make_interp_spline


# Data to plot the curve y=x^3
points_list = []
for x in range(1, 5):
    y = x ** 3
    points_list.append((x, y))

x = np.array([i[0] for i in points_list])
y = np.array([i[1] for i in points_list])

# Plotting the figure
fig = plt.figure()
ax = fig.add_subplot(111)

tangent, = ax.plot([], [], '-')
curve, = ax.plot([], [], '-')
pointA = ax.scatter([], [], c='r')

label_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))

ax.set_xlabel(xlabel='Value of x')
ax.set_ylabel(ylabel='y= f(x), f =x^3')
plt.title('Derivative of function f(x) at a point on the curve y=x^3')


def animate(i,):
    X_Y_Spline = make_interp_spline(x, y)
    X_ = np.linspace(x.min(), x.max(),50)
    Y_ = X_Y_Spline(X_)

    x0 = x[i]
    y0 = y[i]
    m = np.linspace(1, 5, 100)
    slope = 3*x0*x0

    n = (slope*(m-x0)) + y0

    tangent.set_xdata(m)
    tangent.set_ydata(n)
    label_text.set_text(f'Tangent at Point({x0}, {y0})')
    curve.set_xdata(X_)
    curve.set_ydata(Y_)

    pointA.set_offsets([x0, y0])

    return tangent, curve, pointA, label_text


anim = animation.FuncAnimation(fig,
                               animate,
                               frames=len(x),
                               interval=1000,
                               blit=True
                               )
plt.show()

anim.save("curve_plot.gif", dpi=300, writer=PillowWriter(fps=1))
