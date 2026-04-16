import numpy as np
size   = np.array([50, 80, 100, 120, 150, 180, 200, 230, 250, 300])
price  = np.array([45, 72,  95, 110, 140, 165, 190, 210, 240, 290])
size_mean  = np.mean(size)
price_mean = np.mean(price)

numerator   = np.sum((size - size_mean) * (price - price_mean))
denominator = np.sum((size - size_mean) ** 2)

m = numerator / denominator
b = price_mean - m * size_mean

print(f"Slope  m = {m:.4f}  (price increases by {m:.2f}M UGX per m²)")
print(f"Bias   b = {b:.4f}  (starting price with 0 m²)")

price_predicted = m * size + b

print("\nHouse Size | Actual Price | Predicted Price")
print("-" * 45)
for s, pa, pp in zip(size, price, price_predicted):
    print(f"  {s} m²    |  {pa} M UGX    |  {pp:.1f} M UGX")


new_house = 170
predicted = m * new_house + b
print(f"\nA {new_house}m² house should cost about {predicted:.1f} M UGX")

ss_residual = np.sum((price - price_predicted) ** 2)
ss_total    = np.sum((price - price_mean) ** 2)
r_squared   = 1 - (ss_residual / ss_total)
print(f"R² Score  = {r_squared:.4f}")