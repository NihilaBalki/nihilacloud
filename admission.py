import random

def admn():
    print("Welcome to the College!")
    print("We are an autonomous engineering college in the state of Tamil Nadu in India. It is affiliated with Anna University and accredited 'A++' Grade by the National Assessment and Accreditation Council.")
    print("There are {} seats left".format(random.randrange(10, 20)))

def paid(topay, busfare, amt, yemi):
    total_fees = topay + busfare
    remaining_fees = total_fees - amt
    
    if yemi == 0:
        if remaining_fees == 0:
            print("Welcome to GCT")
            return 0
        else:
            return remaining_fees
    else:
        remaining_installment = yemi + (busfare / 2) - amt
        if remaining_installment == 0:
            print("Welcome to GCT")
            return 0
        else:
            return remaining_installment


def bye():
    print("We are an autonomous engineering college in the state of Tamil Nadu in India. It is affiliated with Anna University and accredited 'A++' Grade by the National Assessment and Accreditation Council.")
    print("Too bad that you don't want to continue, but yeah, have a good life.\nThank you.")
