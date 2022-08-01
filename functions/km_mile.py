def main():
    dist = float(input("Enter distance in km "))
    to_mile(dist)

def to_mile(d):
    CONVERTER = 0.6214
    return d * CONVERTER