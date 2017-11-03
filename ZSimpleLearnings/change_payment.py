def pay_change(paid, price):
    # set up the change and an empty dictionary for result
    change = paid - price
    result = {}

    # get the result dictionary values for each bill
    # get the result dictionary values for each bill
    result['$20'] = divmod(change, 20)[0]
    change = divmod(change, 20)[1]

    result['$10'] = divmod(change, 10)[0]
    change = divmod(change, 10)[1]

    result['$5'] = divmod(change, 5)[0]
    change = divmod(change, 5)[1]

    result['$2'] = divmod(change, 2)[0]
    change = divmod(change, 2)[1]

    result['$1'] = divmod(change, 1)[0]
    change = divmod(change, 1)[1]

    # present the result, do not show if value is 0
    for k, v in result.items():
        if v != 0:
            print('Need', v, 'bills of', k)

pay_change(100, 8)
