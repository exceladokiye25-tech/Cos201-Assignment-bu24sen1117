def compute_tax(status, income):
    tax = 0
    previous = 0

    if status == 0:
        brackets = [
            (8350, 0.10),
            (33950, 0.15),
            (82250, 0.25),
            (171550, 0.28),
            (372950, 0.33),
            (float('inf'), 0.35)
        ]
    elif status == 1:
        brackets = [
            (16700, 0.10),
            (67900, 0.15),
            (137050, 0.25),
            (208850, 0.28),
            (372950, 0.33),
            (float('inf'), 0.35)
        ]
    elif status == 2:
        brackets = [
            (8350, 0.10),
            (33950, 0.15),
            (68525, 0.25),
            (104425, 0.28),
            (186475, 0.33),
            (float('inf'), 0.35)
        ]
    elif status == 3:
        brackets = [
            (11950, 0.10),
            (45500, 0.15),
            (117450, 0.25),
            (190200, 0.28),
            (372950, 0.33),
            (float('inf'), 0.35)
        ]
    else:
        print("Invalid filing status")
        return 0

    for limit, rate in brackets:
        if income > limit:
            tax += (limit - previous) * rate
            previous = limit
        else:
            tax += (income - previous) * rate
            break

    return tax


print("Filing Status")
print("0 - Single")
print("1 - Married Filing Jointly / Qualifying Widow(er)")
print("2 - Married Filing Separately")
print("3 - Head of Household")

status = int(input("Enter filing status: "))
income = float(input("Enter taxable income: "))

tax = compute_tax(status, income)

print("Total tax is: $", round(tax, 2))
