import products as pr




def main():

    products = []
    
    laptop = pr.Product('Laptop', 
                        800.00,
                        '15-inch display, 8GB RAM, 256GB SSD')
    
    smartphone = pr.Product('Smartphone',
                            500.00,
                            '6-inch display, 128GB storage')

    #laptop.display_data()
    #print('__dict__', laptop.__dict__)
    #print('__dict__', laptop.__module__)
    #print('__dict__', laptop.__repr__)
    #print('__dict__', laptop.__str__)
    products.append(laptop)
    print(laptop)


    products.append(smartphone)
    print(smartphone)
    
    print(products)


#Na glavnom porgramu iz kojeg se pokrece applikacije mora biti ova dolje konstrukcija:
if __name__ == '__main__':
    main()