def pay_change(paid, price):
    # set up the change and an empty dictionary for result
    change = paid - price
    result = {}

    # get the result dictionary values for each bill
    result['$20'] = divmod(change, 20)[0]
    rest = divmod(change, 20)[1]

    result['$10'] = divmod(rest, 10)[0]
    rest = divmod(change, 10)[1]

    result['$5'] = divmod(rest, 5)[0]
    rest = divmod(change, 5)[1]

    result['$2'] = divmod(rest, 2)[0]
    rest = divmod(change, 2)[1]

    result['$1'] = divmod(rest, 1)[0]
    rest = divmod(change, 1)[1]

    # present the result, do not show if value is 0
    for k, v in result.items():
        if v != 0:
            print('Need', v, 'bills of', k)

pay_change(100, 8)
# TODO try to use map to simply this
