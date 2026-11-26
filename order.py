
def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")

    discount = price * discount_percent / 100
    return round(discount, 2)


def calculate_gst(amount, gst_percent=18):
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if not 0 <= gst_percent <= 100:
        raise ValueError("GST must be between 0 and 100")

    gst = amount * gst_percent / 100
    return round(gst, 2)


def calculate_order_total(price, discount_percent, gst_percent=18):
    if price < 0:
        raise ValueError("Price cannot be negative")

    discount = calculate_discount(price, discount_percent)
    discounted_price = price - discount
    gst = calculate_gst(discounted_price, gst_percent)

    return round(discounted_price + gst, 2)


if __name__ == "__main__":
    price = 1000
    discount_percent = 10

    discount = calculate_discount(price, discount_percent)
    gst = calculate_gst(price - discount)
    total = calculate_order_total(price, discount_percent)

    print("Original Price:", price)
    print("Discount:", discount)
    print("GST:", gst)
    print("Final Order Total:", total)
