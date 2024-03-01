def main():
    str = input("Enter the String:")
    price = calculate_final_price(str)
    print("calculate price", price)


def calculate_final_price(items):
    prices = {
        "A" : 50,
        "B" : 30,
        "C" : 20,
        "D" : 15,
        "AAA" : 130,
        "BB" : 45
    }
    total_price = 0
    item_counts = {}

    for item in items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

    for item, count in item_counts.items():
        if item in prices:
            if item == "A" and count > 2:
                total_price += prices["AAA"] * count / 3
                total_price += prices["A"] * count % 3
            elif item == "B" and count > 1:
                total_price += prices["BB"] * count / 2
                total_price += prices["B"] * count % 2
            else:
                total_price += prices[item] * count
        else:
            return "Invalid item detected: " + item

    return total_price


if __name__ == "__main__":
    main()