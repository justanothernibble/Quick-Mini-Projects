"""
Distance converter would be done by assigning each magnitude a number and multiplying
So m is given a magnitude of 1
cm is magnitude -1
km is magnitude 3
"""



dist = {"mm": -4,
        "cm": -2,
        "m": 0,
        "km": 3}


mass = {"ug": -6,
        "mg": -4,
        "g": 0,
        "kg": 3}

curr = {"gbp": 0.82,
        "jpy": 157.69,
        "eur": 0.98,
        "cny": 7.33,
        "krw": 1474.12,
        "dir": 3.67} # divide the dollar by original, then multiply by new

def convert_dist(ori, new, val):
    if ori == new:
        return "Error"
    else:
        return f"{val} {ori} is now {float(val * (float(10**(dist[ori]-dist[new]))))} {new}"
    

def convert_mass(ori, new, val):
    if ori == new:
        return "Error"
    else:
        return f"{val} {ori} is now {float(val * (float(10**(mass[ori]-mass[new]))))} {new}"
    
def convert_curr(ori, new, val):
    return f"{val} {ori} is now {((val/curr[ori])*curr[new]):.2f} {new}"

print(convert_dist("m", "km", 50000))
print(convert_mass("g", "kg", 250))
print(convert_curr("dir", "krw", 1))