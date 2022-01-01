calc_BMI = lambda W,H : 10000*W/H**2
calc_body_fat = lambda r : 1.20*r.BMI + (0.23*r.Age) - (16.2 if r.Sex=='M' else 5.4)
