def pay_change(paid, cost):
    # set up the change and an empty dictionary for result
    change = paid - cost
    result = {}

    # get the result dictionary values for each bill
    n_twenty = change // 20
    result['$20'] = n_twenty
    rest = change % 20

    n_ten = rest // 10
    result['$10'] = n_ten
    rest = rest % 10

    n_five = rest // 5
    result['$5'] = n_five
    rest = rest % 5

    n_two = rest // 2
    result['$2'] = n_two
    rest = rest % 2

    n_one = rest // 1
    result['$1'] = n_one

    # present the result, do not show if value is 0
    for k, v in result.items():
        if v != 0:
            print('Need', v, 'bills of', k)


pay_change(65, 33)
