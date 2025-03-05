

class Product:
    def __init__ (self,
                name: str,
                price: float,
                description=''):
        
        self.name = name
        self.price = price
        self.description = description
        
    def display_data(self):
        print(f'{self.name}')
        
    
    def __str__(self) -> str:
        return f'Naziv: {self.name}'
        
    def __repr__(self) -> str:
        return f'Naziv: {self.name}'    