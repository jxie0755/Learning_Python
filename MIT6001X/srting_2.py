temp = 120
if temp > 85:
    print("Hot")
elif temp > 100:  # elif优先级低于if,被跳过
    print("REALLY HOT!")
elif temp > 60:
    print("Comfortable")
else:
    print("Cold")
