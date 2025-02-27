import pandas as pd
from datetime import datetime

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

class Sale:
    def __init__(self, product, quantity, price):
        try:
            self.product = str(product).lower()
            self.quantity = int(quantity)
            self.price = float(price)
            self.date = datetime.now().strftime('%d%m%Y')
        except Exception as e:
            print(f"Error: {e}")

    def __repr__(self):
        return f"Product: {self.product}, Quantity: {self.quantity}, Price: {self.price}, Date: {self.date}"
    
    def addSale(self, df):
        ser = pd.Series(
                        {"Product": self.product,
                         "Quantity": self.quantity,
                         "Price": self.price,
                         "Date": self.date}
                         )
        df.loc[len(df)] = ser
        print(f"The following Sale has been added successfully:\n{self.__repr__}")

    def removeSale(self, df, pro):
        index = df[df['Product'].str.lower() == pro.lower()].index
        if not index.empty:
            df.drop(index, inplace=True)
            print("Sale removed successfully")
        else:
            print("Sale not found")


def view_database(df):
    if df.empty:
        print("No sales data available.")
    else:
        print(df)


df  = pd.read_csv('sales.csv', names=['Product', 'Quantity', 'Price', 'Date'])

print("Welcome to Sales Data Processor")
while True:
    try:
        choice = int(input(("What would you like to do?\n1. Add a sale\n2. Remove a sale\n3. View Sales\n4. Exit\n5. Process data\n> ")))
    except Exception as e:
        print("Enter an Integer.")
    if not ((choice > 5) or (choice < 1)):
        if choice == 1:
            df = pd.read_csv('sales.csv')
            pro = input("Enter product name:\n> ")
            qua = int(input("Enter Qty:\n> "))
            pri = float(input("Enter Price\n> "))
            new = Sale(product=pro, quantity=qua, price=pri)
            new.addSale(df)
            df.to_csv('sales.csv', index=False)
        elif choice == 2:
            df = pd.read_csv('sales.csv')
            pro = input("What product would you like to remove?\n> ")
            Sale(product=pro, quantity=0, price=0).removeSale(df, pro)
            df = df.reset_index(drop=True)
            df.to_csv('sales.csv', index=False)
        elif choice == 3:
            print(df)
        elif choice == 4:
            print("Exiting")
            break
        elif choice == 5:
            try:
                df = pd.read_csv('sales.csv')
                print("Initiatin data cleansing...")
                print("Removing rows with missing values...")
                df = df.dropna()
                print("Removing duplicates...")
                df = df.drop_duplicates()
                print("Ensuring correct types...")
                df['Product'] = df['Product'].astype(str)
                df['Quantity'] = df['Quantity'].astype(int)
                df['Price'] = df['Price'].astype(float)
                df['Date'] = pd.to_datetime(df['Date'], format='%d%m%Y')
                print("Cleaning done successfully!")
            except Exception as e:
                print(f"Error: {e}")
            df.to_csv('sales.csv', index=False)
    else:
        print("Invalid choice. Must be between 1 and 5")
