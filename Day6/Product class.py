'''create a product class and declare the states as productname,
price,discount,gst,quantity'''



class Product:
    def __init__(self,ProductName,Price,Discount,GST,Quantity):
        self.ProductName=ProductName
        self.Price=Price
        self.Discount=Discount
        self.GST=GST
        self.Quantity=Quantity
    def display(self):
        print(f"Product Name is : {self.ProductName}")
        print(f"Product Price is : {self.Price}")
        print(f"Discount is : {self.Discount}")
        print(f"GST is : {self.GST}")
        print(f"Quantity is : {self.Quantity}")
E1=Product("Washing Machine",10000,20,10,4)
E1.display()
        
        