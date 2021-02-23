import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML

def simple_plot(t, Y):
  plt.figure(figsize=(15, 10))

  plt.plot(t, Y[0], label='x')
  plt.plot(t, Y[1], label='v')
  plt.plot(t, Y[2], label='θ')
  plt.plot(t, Y[3], label='ω')
  plt.xlabel('t')
  plt.legend()
  plt.grid()

  plt.show()


def phase_plots(Y):
  plt.figure(figsize=(15, 7))

  plt.subplot(221)
  plt.plot(Y[0], Y[1])
  plt.xlabel('x')
  plt.ylabel('v')
  plt.grid()
  plt.title('Cart position and velocity')

  plt.subplot(222)
  plt.plot(Y[2], Y[3])
  plt.xlabel('θ')
  plt.ylabel('ω')
  plt.grid()
  plt.title('Pendulum angle and angular velocity')

  plt.show()

'''
def sim_animation(Y, params):
  L = params[2]

  plt.figure(figsize=(15, 7))

  plt.grid()
  plt.xlabel('x')

  fig, ax = plt.subplots()

  ax.set_xlim(( -8, 8))
  ax.set_ylim(( -0.5, L + 1))

  plots = [plt.plot([],[]), plt.plot([],[]), plt.scatter([],[]), plt.scatter([],[])]

  def init():
      plots[0].set_data([-0.5, L+1], [0, 0])
      return plots

  def animate(frame):
    cart_x = Y[0, frame]
    cart_y = 0.5
    head_x = Y[2, frame]
    head_y = 0.5 + L

    plots[1].set_data([cart_x, head_x], [cart_y, head_y])
    plots[2].set_data([cart_x], [cart_y])
    plots[3].set_data([head_x], [head_y])

    return plots

  anim = animation.FuncAnimation(fig, animate, init_func=init, frames=Y.shape[1], interval=20, blit=True)
  HTML(anim.to_html5_video())
  rc('animation', html='html5')

  return anim
'''
