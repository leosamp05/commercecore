import json


class OrderRepository:
    
    def save_order(self, order):
        data = self.load_orders()
        data.append(order)   
        with open("data/orders.json", "w") as file:
            json.dump(data, file, indent=4)
    
    def load_orders(self):
        with open("data/orders.json", "r") as file:
            data = json.load(file)
            
        return data
    
    def cancel_order(self, index):
        data = self.load_orders()
        
        if data[index]['status'] == 'CANCELLED':
            print("L'ordine era stato già annullato.")
        else:
            data[index]['status'] = 'CANCELLED'
            with open("data/orders.json", "w") as file:
                json.dump(data, file, indent=4)
            print("Ordine annullato con successo.")
        
        