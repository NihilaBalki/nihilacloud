def details(dept):
    if dept == "CSE":
        print("\nTuition fees: Rs.63,000")
    elif dept == "ECE":
        print("\nTuition fees: Rs.52,000")
    elif dept == "MECH":
        print("\nTuition fees: Rs.41,000")
    elif dept == "CIVIL":
        print("\nTuition fees: Rs.74,000")

def transport(km):
    return int(km * 250)

def pay(yn, dept, percent, count):
    if yn.lower() == "yes" or yn.lower() == "y":
        cse = 63000
        ece = 52000
        mech = 41000
        civil = 74000
        if percent >= 90:
            reduction = 50
            print("\nYou have 50% off the fees")
            print("Amount to pay after calculating the fees concessions: ")
            if dept == "CSE":
                return cse - (63000 / 2)
            elif dept == "ECE":
                return ece - (52000 / 2)
            elif dept == "MECH":
                return mech - (41000 / 2)
            elif dept == "CIVIL":
                return civil - (74000 / 2)
        else:
            print("Amount to pay: ")
            if dept == "CSE":
                return cse
            elif dept == "ECE":
                return ece
            elif dept == "MECH":
                return mech
            elif dept == "CIVIL":
                return civil
    else:
        print("Kindly pay the following amount to confirm your seat:")
        return int(20000)

def yemi(topay):
    return int(topay / 2)
