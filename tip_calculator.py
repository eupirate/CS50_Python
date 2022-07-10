def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    format_dollar = d.replace('$', '')
    return float(format_dollar)

def percent_to_float(p):
    # TODO
    format_percent = p.replace('%', '')
    cal_percent = float(format_percent) / 100
    return cal_percent

main()
