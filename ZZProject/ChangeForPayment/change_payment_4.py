def pay_change(paid, price):
    # set up the change and an empty dictionary for result
    change = paid - price
    bills = [100, 20, 10, 5, 2, 1, 0.5]
    result = {}
    
    # the value of change can be modified by cycling of divmod()
    for billvalue in bills:
        billnum, change = divmod(change, billvalue)
        result[f'${billvalue}'] = billnum

    # present the result, do not show if value is 0
    for k, v in result.items():
        if v != 0:
            print('Need', int(v), 'of', k)

pay_change(200, 17.5)
