import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def Vo(w, R, C, L):
    return (-1j*w*L) / (-1j*w*L - R + R*C*L*w**2)


def get_resonance(w, voltage):
    return w[np.argmax(voltage)]


def update(val):
    ax.cla()
    voltage = abs(Vo(w, slider_R.val, slider_C.val, slider_L.val))
    ax.plot(f, voltage)
    ax.set_title(
        f"Theoretical resonance: {1/(np.sqrt(slider_C.val*slider_L.val) * 2*np.pi)}\nComputed resonance:  {get_resonance(f, voltage)}",
        loc="left")
    ax.set_ylabel("Output Voltage (V)")
    ax.set_xlabel("Frequency (Hz)")
    fig.canvas.draw_idle()


L = 1e-3  # henries
C = 1e-6  # farads
R = 2700  # ohms
w = np.linspace(20000, 45000, 500)  # omega
f = w / (2*np.pi)

fig, ax = plt.subplots()
fig.subplots_adjust(left=0.25, bottom=0.30)
voltage = abs(Vo(w, R, C, L))
ax.plot(f, voltage)
ax.set_title(
    f"Theoretical resonance: {1/(np.sqrt(L*C) * 2*np.pi)}\nComputed resonance:  {get_resonance(f, voltage)}",
    loc="left")
ax.set_ylabel("Output Voltage (V)")
ax.set_xlabel("Frequency (Hz)")


R_slider_ax = fig.add_axes([0.2, .05, 0.65, 0.03])
slider_R = Slider(R_slider_ax, 'R (ohms)',
                  100, 2700, valinit=1000, valfmt='%d')
slider_R.on_changed(update)

C_slider_ax = fig.add_axes([0.2, 0.1, 0.65, 0.03])
slider_C = Slider(C_slider_ax, 'C (farads)', .5e-6,
                  2e-6, valinit=1e-6, valfmt='%f')
slider_C.on_changed(update)

L_slider_ax = fig.add_axes([0.2, 0.15, 0.65, 0.03])
slider_L = Slider(L_slider_ax,
                  'L (henries)', .5e-3, 2e-3, valinit=1e-3, valfmt='%f')
slider_L.on_changed(update)

plt.show()
