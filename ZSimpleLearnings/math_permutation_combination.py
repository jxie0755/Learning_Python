# This is just to math calculate the P(X,Y) and C(X, Y) instead of showing all the possible arrangment

# P(X, Y) = X! / X-Y!
# C(X, Y) = X! / Y!


from scipy.special import comb, perm

# Output will be float
print(perm(3,2))  # >>> 6.0
print(comb(3,2))  # >>> 3.0

# Output will be float
import scipy.special as spsp
print(spsp.perm(3,2))  # >>> 6.0
print(spsp.comb(3,2))  # >>> 3.0
