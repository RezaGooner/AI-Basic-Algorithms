# Simple Python program to compute w1 and w0 for simple linear regression with SSE cost function

# y = 3x - 2 + ε -> w1 = 3 , w2 = -2

# Given data
x = [5,  3,   -1,   2,  6]
y = [14, 6, -5.5, 3.5, 18]

X, Y, XiYi, Xi2 = 0, 0, 0, 0

# Number of samples
n = len(x)

# Compute required variable
for i in range(n):
    X += x[i]
    Y += y[i]
    XiYi += x[i] * y[i]
    Xi2  += x[i] ** 2

w1 = (n * XiYi - X * Y) / (n * Xi2 - X ** 2)
w0 = (Y - w1 * X) / n

print(f"w1 (slope)     = {w1}")
print(f"w0 (intercept) = {w0}")
