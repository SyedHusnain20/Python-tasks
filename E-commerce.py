from datetime import datetime

class Order:
    discount_rate = 0

    def __init__(self):
        self.Total = 0
        self.items = []

    def log_action(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            with open('Tasks/log.txt', 'a') as log_file:
                log_file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Executed {func.__name__}\n")
            return result
        return wrapper

    @log_action
    def add_item_by_ID(self, product_ID, Quantity):
        product_found = False
        with open('Tasks/products.csv') as file:
            lines = file.readlines()
            for i in range(1, len(lines)):
                products = lines[i].strip().split(',')
                if products[0] == product_ID:
                    price = float(products[2])
                    item_total = price * Quantity
                    self.Total += item_total
                    self.items.append({
                        'id': product_ID,
                        'name': products[1],
                        'quantity': Quantity,
                        'price': price,
                        'item_total': item_total
                    })
                    order_log = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Added item: {products[1]} (x{Quantity}) - Total: {item_total}"
                    with open('Tasks/log.txt', 'a') as log_file:
                        log_file.write(order_log + '\n')
                    print(f"Product {products[1]} added successfully.")
                    product_found = True
                    break
        
        if not product_found:
            error_log = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Invalid product ID attempt: {product_ID}"
            with open('Tasks/log.txt', 'a') as log_file:
                log_file.write(error_log + '\n')
            print("Product not found. Please enter a valid product ID")

    @log_action
    def calculate_total(self):
        discount_amount = (self.discount_rate / 100) * self.Total
        final_total = self.Total - discount_amount
        total_log = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Calculated total with discount: {final_total}"
        with open('Tasks/log.txt', 'a') as log_file:
            log_file.write(total_log + '\n')
        print(f"Calculated total after {self.discount_rate}% discount: {final_total}")
        return final_total

    @classmethod
    @log_action
    def set_discount(cls, discount_rate):
        cls.discount_rate = discount_rate
        discount_log = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Discount set to {discount_rate}%"
        with open('Tasks/log.txt', 'a') as log_file:
            log_file.write(discount_log + '\n')
        print(f"Global discount set to {discount_rate}%")

    @staticmethod
    def is_valid_product_id(product_id):
        with open('Tasks/products.csv') as file:
            lines = file.readlines()
            for i in range(1, len(lines)):
                products = lines[i].strip().split(',')
                if products[0] == product_id:
                    return True
        error_log = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Invalid product ID attempt: {product_id}"
        with open('Tasks/log.txt', 'a') as log_file:
            log_file.write(error_log + '\n')
        return False

order = Order()
order.add_item_by_ID("1", 2)
order.add_item_by_ID("2", 1)
order.add_item_by_ID("99", 1)
Order.set_discount(10)
order.calculate_total()