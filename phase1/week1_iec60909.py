import numpy as np

# IEC 60909 parameters
c  = 1.10
Un = 13.8e3
Z1 = 0.0576

# Calculate fault current
Ik = (c * Un) / (np.sqrt(3) * Z1)

kappa = 1.8
ip = kappa * np.sqrt(2) * Ik

print("IEC 60909 Fault Current Calculation")
print("=" * 40)
print(f"Nominal Voltage  : {Un/1000:.1f} kV")
print(f"Voltage Factor c : {c:.2f}")
print(f"Impedance Z1     : {Z1:.4f} ohm")
print(f"Fault Current Ik : {Ik/1000:.2f} kA")
print(f"peak current ip : { ip/1000:.2f} KA")