def pay_change(paid, price):
    # set up the change and an empty dictionary for result
    global change
    change = paid - price
    bills = ['$100', '$20', '$10', '$5', '$2', '$1', '$0.5']

    # get a function to calculate the change, for the number of each bill
    def f(x):
        global change
        result = divmod(change, x)[0]
        change = divmod(change, x)[1]
        return result
    temp = list(map(f, list(map(lambda x: float(x[1:]), bills))))
    result = dict(zip(bills, temp))
    print(result)

    # present the result, do not show if value is 0
    for k, v in result.items():
        if v != 0:
            print('Need', int(v), 'bills of', k)

pay_change(200, 17.5)
