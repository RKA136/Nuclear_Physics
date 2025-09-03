import numpy as np
import matplotlib.pyplot as plt

# Define the constants
G = 6.6743e-11  # gravitational constant, m^3 kg^-1 s^-2
k_e = 8.9875e9  # Coulomb's constant, N m^2 C^-2
e_charge = 1.6021e-19  # elementary charge, C
m_p = 1.6726e-27  # proton mass, kg
hbar = 1.0546e-34  # J s
c = 3e8  # m/s

# I am using the positive value of each force for better visualization
def force_G(m1, m2, r):
    return G * m1 * m2 / r**2

def force_E(q1, q2, r):
    return k_e * q1 * q2 / r**2

def force_S(V0, λ, r):
    return (V0 / λ) * np.exp(-r * λ) * (λ/r + 1/r**2)

m1 = m_p
m2 = m_p

q1 = e_charge
q2 = e_charge

V0 = 40e6 * e_charge
λ = 0.7e15

#range of r
r = np.linspace(1e-20, 1e-14, 1000)

plt.figure(figsize=(10, 6))
plt.plot(r, force_G(m1, m2, r), label='Gravitational Force')
plt.plot(r, force_E(q1, q2, r), label='Electrostatic Force')
plt.plot(r, force_S(V0, λ, r), label='Strong Force')
plt.xlabel('Distance (m)')
plt.ylabel('Force (N)')
plt.yscale('log')
plt.title('Forces between Particles')
plt.legend()
plt.grid()
plt.savefig('Question_1.png')
plt.close()

print(r"F_G = ", force_G(m1, m2, 1e-15))
print(r"F_E = ", force_E(q1, q2, 1e-15))
print(r"F_S = ", force_S(V0, λ, 1e-15))