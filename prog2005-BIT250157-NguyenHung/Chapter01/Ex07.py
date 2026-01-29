a = float(input("So thu 1: "))
b = float(input("So thu 2: "))
c = float(input("So thu 3: "))

lon_nhat = a
if b > lon_nhat:
    lon_nhat = b
if c > lon_nhat:
    lon_nhat = c

print(lon_nhat)