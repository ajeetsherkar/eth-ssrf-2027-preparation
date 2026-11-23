import time
import numpy as np

a = np.random.rand(1024, 1024).astype(np.float32)

lat = []

for _ in range(1000):
    t0 = time.perf_counter()
    a @ a
    lat.append((time.perf_counter() - t0) * 1000)

lat = np.array(lat)

print("first 10:", lat[:10].round(3))

print(
    "mean", lat.mean(),
    "p50", np.percentile(lat, 50),
    "p95", np.percentile(lat, 95),
    "p99", np.percentile(lat, 99)
)
print("last 100 mean:", lat[-100:].mean())
print("last 100 p50:", np.percentile(lat[-100:], 50))
print("last 100 p95:", np.percentile(lat[-100:], 95))
print("last 100 p99:", np.percentile(lat[-100:], 99))