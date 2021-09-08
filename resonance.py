import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def Vo(w, R, C, L):
    return (-1j*w*L) / (-1j*w*L - R + R*C*L*w**2)


def get_resonance(w, voltage):
    return w[np.argmax(voltage)]


L = 1e-3  # henries
C = 1e-6  # farads
R = 2700  # ohms
w = np.linspace(20000, 45000, 500)  # omega
f = w / (2*np.pi)

theoretical = []
computed = []

for i in range(100):
    C += .01e-6
    voltage = abs(Vo(w, R, C, L))
    computed.append(get_resonance(f, voltage))
    theoretical.append(1 / (np.sqrt(L*C) * 2*np.pi))

slope, intercept, r, p_value, std_err = stats.linregress(
    theoretical, computed)

plt.scatter(theoretical, computed,
            label=f'R^2 = {round(r**2, 2)}\nstandard error = {round(std_err, 5)}\n best fit line equation: y = {round(slope, 2)}x + {round(intercept, 2)}')
plt.title("Theoretical vs Computed Resonance Frequency")
plt.xlabel("Theoretical (Hz)")
plt.ylabel("Computed (Hz)")
plt.grid()
plt.legend()
plt.show()
