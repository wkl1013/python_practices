def make_pizza(size, *toppings):
    print(f"制作一个{size}存的披萨，需要以下材料：")
    for topping in toppings:
        print(topping)
