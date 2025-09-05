import math

def sigm(x):
    return math.e**x / (1 + math.e**x)

print(
    sigm(0) * sigm(sigm(0)) * sigm(sigm(sigm(0)))
)