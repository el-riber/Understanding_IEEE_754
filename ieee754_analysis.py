import struct
import math
from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_DOWN
import matplotlib.pyplot as plt
import numpy as np
import os

# Part 1: Convert Decimal to IEEE 754
def float_to_ieee754(num):
    packed = struct.pack('>f', num)  # Big-endian float (32-bit)
    bits = ''.join(f'{byte:08b}' for byte in packed)
    return bits

# Part 2: Arithmetic Operations
a = 0.1 + 0.2
b = 1.0 / 3.0
a_ieee = float_to_ieee754(a)
b_ieee = float_to_ieee754(b)

# Part 3: Special Values
pos_inf = float('inf')
neg_inf = float('-inf')
nan_val = float('nan')
is_nan_unequal = nan_val != nan_val

# Part 4: Rounding Modes
getcontext().prec = 5
num_decimal = Decimal('1.235')
rounded_half_up = num_decimal.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP)
rounded_down = num_decimal.quantize(Decimal('1.00'), rounding=ROUND_DOWN)

# Part 5: Underflow and Overflow
underflow = 1e-50 * 1e-50
overflow = 1e308 * 1e10

# Part 6: Precision Loss Visualization

# Create a local directory to save the plot

output_dir = os.path.join(os.getcwd(), "ieee754_output")
os.makedirs(output_dir, exist_ok=True)

# Define output file path
precision_loss_plot_path = os.path.join(output_dir, "precision_loss_plot.png")

x_vals = np.logspace(-45, 38, 1000)
y_vals = x_vals + 1 - 1
error_vals = y_vals - x_vals

plt.figure()
plt.plot(x_vals, error_vals)
plt.xscale('log')
plt.yscale('log')
plt.title("Precision Loss in IEEE 754")
plt.xlabel("Value")
plt.ylabel("Error (x + 1 - 1 - x)")
plt.grid(True)

# Save the plot
plt.savefig(precision_loss_plot_path)
plt.close()

print(f"Plot saved at: {precision_loss_plot_path}")

# Print Summary
print("Part 1: IEEE 754 Binary Representation")
print("0.15625 =", float_to_ieee754(0.15625))

print("\nPart 2: Arithmetic Results")
print("0.1 + 0.2 =", a, "→ IEEE 754:", a_ieee)
print("1.0 / 3.0 =", b, "→ IEEE 754:", b_ieee)

print("\nPart 3: Special Values")
print("Positive Infinity:", pos_inf)
print("Negative Infinity:", neg_inf)
print("NaN:", nan_val)
print("NaN != NaN?", is_nan_unequal)

print("\nPart 4: Rounding Modes")
print("ROUND_HALF_UP:", rounded_half_up)
print("ROUND_DOWN   :", rounded_down)

print("\nPart 5: Underflow and Overflow")
print("Underflow:", underflow)
print("Overflow :", overflow)

print("\nPart 6: Precision Loss plot saved as: precision_loss_plot.png")
