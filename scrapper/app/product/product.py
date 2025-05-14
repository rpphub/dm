class Product:
    def __init__(self, name: str, restaurantName: str, price: float):
        self.name = name
        self.price = price
        self.restaurantName = restaurantName
    def __str__(self):
        return f"Étel:{self.name} - Ár:{self.price} Ft"