import json


OFFERS_FILE = "offers.json"
PRODUCTS_FILE = "products.json"
CUSTOMERS_FILE = "customers.json"


def load_data(filename):
    """Load data from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Error decoding {filename}. Check file format.")
        return []


def save_data(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


offer_number = 1

# TODO: Implementirajte funkciju za kreiranje nove ponude.
def create_new_offer(offers, products, customers):
    """
    Prompt user to create a new offer by selecting a customer, entering date,
    choosing products, and calculating totals.
    """
    selected_products = []
    #offers = load_data(OFFERS_FILE)
    #products = load_data(PRODUCTS_FILE)
    #customers = load_data(CUSTOMERS_FILE)
    
    #print("Postojeće ponude:", offers)
    #print("Postojeći proizvodi:", products)
    #print("Postojeći kupci:", customers)

    # Omogućite unos kupca
    customer_index = int(input("Odaberite broj kupca ili unesite 0 za novog: "))
    if customer_index == 0:
        new_customer = input("Unesite ime novog kupca: ")
        customers.append(new_customer)
        selected_customer = new_customer
    else:
        selected_customer = customers[customer_index - 1]
    
    # Izračunajte sub_total, tax i total

    
    # Dodajte novu ponudu u listu offers
    offer_date = input("Unesite datum ponude (YYYY-MM-DD): ")

    new_offer = {
        "customer": selected_customer,
        "date": offer_date
    }
    
    offers.append(new_offer)


# TODO: Implementirajte funkciju za upravljanje proizvodima.
def manage_products(products):
    """
    Allows the user to add a new product or modify an existing product.
    """
    # Omogućite korisniku izbor između dodavanja ili izmjene proizvoda
    
    print('1. Dodaj novi proizvod')
    print('2. Izmijeni postojeći proizvod')
    choice = input('Odaberite (1/2): ')

    # Za dodavanje: unesite podatke o proizvodu i dodajte ga u listu products
    if choice == '1':
        name = input('Naziv proizvoda: ')
        price = float(input('Cijena: '))
        products.append({"name": name, "price": price})
    # Za izmjenu: selektirajte proizvod i ažurirajte podatke
    if choice == '2':
        pass


# TODO: Implementirajte funkciju za upravljanje kupcima.
def manage_customers(customers):
    """
    Allows the user to add a new customer or view all customers.
    """
    # Za dodavanje: omogući unos imena kupca, emaila i unos VAT ID-a
    customers = load_data(CUSTOMERS_FILE)
    #print("Postojeći kupci:", customers)

    while True:
        print()
        customer_name = input('Upisite ime kupca kojeg zelite dodati u sustav: ')
        customer_mail = input('Upisite mail kupca kojeg zelite dodati u sustav: ')
        customer_vat = int(input('Upisite VAT ID kupca kojeg zelite dodati u sustav: ')) 
        
        next_customer = input('Zelite li unijeti jos kupaca da/ne: ')
        
        if next_customer.lower() != 'da':
            break
            
    # Za pregled: prikaži listu svih kupaca
        new_customers = {
            "name" : customer_name,
            "email" : customer_mail,
            "vat_id" : customer_vat
        }
    
        customers.append(new_customers)
        
    save_data(CUSTOMERS_FILE, customers)
    
    print("Ispis kupaca nakon dodavanja:")
    for customer in customers:
        print(customer)
    
    return customers

# TODO: Implementirajte funkciju za prikaz ponuda.
def display_offers(offers):
    """
    Display all offers, offers for a selected month, or a single offer by ID.
    """
    # Omogućite izbor pregleda: sve ponude, po mjesecu ili pojedinačna ponuda
    # Prikaz relevantnih ponuda na temelju izbora
    pass


# Pomoćna funkcija za prikaz jedne ponude
def print_offer(offer):
    """Display details of a single offer."""
    print(f"Ponuda br: {offer['offer_number']}, Kupac: {offer['customer']['name']}, Datum ponude: {offer['date']}")
    print("Stavke:")
    for item in offer["items"]:
        print(f"  - {item['product_name']} (ID: {item['product_id']}): {item['description']}")
        print(f"    Kolicina: {item['quantity']}, Cijena: ${item['price']}, Ukupno: ${item['item_total']}")
    print(f"Ukupno: ${offer['sub_total']}, Porez: ${offer['tax']}, Ukupno za platiti: ${offer['total']}")


def main():
    # Učitavanje podataka iz JSON datoteka
    offers = load_data(OFFERS_FILE)
    products = load_data(PRODUCTS_FILE)
    customers = load_data(CUSTOMERS_FILE)

    while True:
        print("\nOffers Calculator izbornik:")
        print("1. Kreiraj novu ponudu")
        print("2. Upravljanje proizvodima")
        print("3. Upravljanje korisnicima")
        print("4. Prikaz ponuda")
        print("5. Izlaz")
        choice = input("Odabrana opcija: ")

        if choice == "1":
            create_new_offer(offers, products, customers)
        elif choice == "2":
            manage_products(products)
        elif choice == "3":
            manage_customers(customers)
        elif choice == "4":
            display_offers(offers)
        elif choice == "5":
            # Pohrana podataka prilikom izlaza
            save_data(OFFERS_FILE, offers)
            save_data(PRODUCTS_FILE, products)
            save_data(CUSTOMERS_FILE, customers)
            break
        else:
            print("Krivi izbor. Pokusajte ponovno.")


if __name__ == "__main__":
    main()
