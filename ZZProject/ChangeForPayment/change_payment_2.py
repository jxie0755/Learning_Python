def pay_change(paid, price):
    # set up the change and an empty dictionary for result
    global change
    change = paid - price
    result = {}
    # get the result dictionary values for each bill, by a function
    def f(x):
        global change
        result = divmod(change, x)[0]
        change = divmod(change, x)[1]
        return result
    result["$20"] = f(20)
    result["$10"] = f(10)
    result["$5"] = f(5)
    result["$2"] = f(2)
    result["s1"] = f(1)

    # present the result, do not show if value is 0
    for k, v in result.items():
        if v != 0:
            print("Need", v, "bills of", k)

pay_change(100, 8)
