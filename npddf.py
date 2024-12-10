def df():
    total_sum = 0

    while True:

        item_name = input("Ievadi preces nosaukumu (vai '0' lai beigtu): ")
        if item_name == "0":
            break
        price = float(input("Ievadi cenu: "))
        if price <= 0:
            print ("Kļūda! Lūdzu ievadiet derīgu cenu.")
            continue
        quantity = int(input("Ievadi daudzumu: "))
        if quantity <= 0:
            print ("Ķļūda! Lūdzu ievadiet derīgu daudzumu.")
            continue
        item_total = price * quantity
        total_sum += item_total
        print(f"Prece: {item_name}, Daudzums: {quantity}, Kopējā summa: {item_total:.2f} €")
    print(f"Kopsumma: {total_sum:.2f} €")

if __name__ == "__main__":
    df()
