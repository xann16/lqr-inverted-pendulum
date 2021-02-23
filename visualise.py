import numpy as np
import matplotlib.pyplot as plt

def simple_plot(t, Y):
  plt.plot(t, Y[0], label='x')
  plt.plot(t, Y[1], label='v')
  plt.plot(t, Y[2], label='θ')
  plt.plot(t, Y[3], label='ω')
  plt.xlabel('t')
  plt.legend()
  plt.grid()

  plt.show()


def phase_plots(Y):
  plt.figure(figsize=(10, 5))

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
