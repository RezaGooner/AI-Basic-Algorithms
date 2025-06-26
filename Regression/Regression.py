import numpy as np

# n sample and d feature
# X_raw: list of n d-dimensional vectors
# y_raw: list of n terget valur

# test sample
X_raw = [
    [5,  2, -1],
    [3, -1,  0],
    [-1, 4,  1],
    [2,  0,  3],
    [6,  1, -2]
]
y_raw = [14, 6, -5.5, 3.5, 18]

# convert to numpy array
X = np.array(X_raw, dtype=float)    # dim: (n, d)
y = np.array(y_raw, dtype=float).reshape(-1, 1)  # dim: (n, 1)

n, d = X.shape
print(f"Number of samples: n = {n}, number of features: d = {d}")

# add bias
# X dim(n,d) -> X_b dim(n,d+1)
X_b = np.hstack([np.ones((n,1)), X])

# w_hat dim : (d+1,1)
XtX = X_b.T.dot(X_b)          # (d+1, d+1)
XtX_inv = np.linalg.inv(XtX)  # inverse
Xty = X_b.T.dot(y)            # (d+1, 1)

w_hat = XtX_inv.dot(Xty)      # (d+1, 1)

# slice w0 , w1..wd
w0 = w_hat[0, 0]
w = w_hat[1:, 0]   # vector of length d

print("Estimated parameters:")
print(f"  w0 (intercept) = {w0:.4f}")
for j in range(d):
    print(f"  w{j+1} (weight of feature {j+1}) = {w[j]:.4f}")

# get sample entry
x_new = []
for j in range(d):
    val = float(input(f"Enter feature x[{j+1}] for prediction: "))
    x_new.append(val)

x_new = np.array([1] + x_new).reshape(1, -1)  # add bias -> sim (1, d+1)
y_pred = x_new.dot(w_hat)                     # dim (1,1)

print(f"Predicted y = {y_pred[0,0]:.4f}")
