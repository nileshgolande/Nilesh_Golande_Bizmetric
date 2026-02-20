import pyodbc

class DataConnect:
    """ HAndle Data base connection"""
    def connect(self):

        return  pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=PRADIP\\SQLEXPRESS;"
    "DATABASE=Restaurant;"
    "Trusted_Connection=yes;"
)

print("Connected successfully") 

class menu(DataConnect):
    def show_menu(self):

        """This function fetch the itemName and price from sql menu table to show the available item to customer"""
        con = self.connect() 
        cur = con.cursor()
        cur.execute("select item_name,price from menu")
        rows = cur.fetchall()
        print('------Menu------')
        for i in rows:
            print(i.item_name ,"-" ,i.price,"rs")

# menu1 = menu()
# menu1.show_menu()


class Bill(DataConnect):
        """ handle all bill generation and print the bill """
        
        def printBill(self,cust_id):
            self.cust_id = cust_id

            # cust_id = int(input("Enter customer id for bill: "))
            con = self.connect()
            cur =con.cursor()

            cur.execute("""
                SELECT m.item_name,
                    o.quantity,
                    m.price,
                    (o.quantity * m.price) AS total
                FROM orders o
                JOIN menu m ON o.item_id = m.item_id
                WHERE o.cust_id = ?
            """, (cust_id,))

            rows = cur.fetchall()

            if not rows:
                print("No orders found for this customer.")
                return

            print("-" * 60)
            print("{:^58}".format("Welcome Hotel Nilesh"))
            print("-" * 60)
            print("{:4} {:15} {:10} {:10}".format("sr", "Menu", "qunt", "price"))
            print("-" * 60)

            grand_total = 0
            
            sr = 1

            for r in rows:
                print("{:4} {:15} {:10} {:10}".format(
                    sr,
                    r.item_name,
                    r.quantity,
                    r.total
                ))
                grand_total += r.total
                sr += 1

            print("Grand Total = ",  grand_total,"rs")

            cur.execute("""
                SELECT grandTotal, time
                FROM Customer
                WHERE cust_id = ?
            """, (cust_id,))

        def Save_Bill(self, cust_id):
            """save the generated bill in txt file according to customer id"""

            con = self.connect()
            cur = con.cursor()

            cur.execute("""
                SELECT m.item_name,
                    o.quantity,
                    m.price,
                    (o.quantity * m.price) AS total
                FROM orders o
                JOIN menu m ON o.item_id = m.item_id
                WHERE o.cust_id = ?
            """, (cust_id,))

            rows = cur.fetchall()

            if not rows:
                print("No orders found for this customer.")
                return

            file_name = rf"C:\Users\pradi\Downloads\NILESH\project\bill_{cust_id}.txt"


            with open(file_name, "w") as f:

                f.write("-" * 60 + "\n")
                f.write("Welcome Hotel Nilesh".center(60) + "\n")
                f.write("-" * 60 + "\n")
                f.write("{:4} {:15} {:10} {:10}\n".format("sr", "Menu", "qty", "total"))
                f.write("-" * 60 + "\n")

                sr = 1
                grand_total = 0

                for r in rows:
                    f.write("{:4} {:15} {:10} {:10}\n".format(
                        sr,
                        r.item_name,
                        r.quantity,
                        r.total
                    ))
                    grand_total += r.total
                    sr += 1

                f.write("-" * 60 + "\n")
                f.write(f"Grand Total : {grand_total} rs\n")

                cur.execute("""
                    SELECT grandTotal, time
                    FROM Customer
                    WHERE cust_id = ?
                """, (cust_id,))

                info = cur.fetchone()
                if info:

                    # f.write(f"Grand Total : {info.grandTotal}\n")
                    f.write(f"Time        : {info.time}\n")

            print("Bill downloaded successfully as :", file_name)




class TakeOrder(Bill):

    def cust_Order(self):
        """for getting input of customer order"""

        con = self.connect()
        cur = con.cursor()

        cur.execute("""
            INSERT INTO Customer DEFAULT VALUES;
            SELECT SCOPE_IDENTITY();
        """)
        cur.nextset()
        cust_id = int(cur.fetchone()[0])
        con.commit()

        print("Customer id:", cust_id)

        grand_total = 0

        while True:

            item_name = input(
                "Which item would you like to get (or done): "
            ).capitalize()

            if item_name.lower() == "done":

                cur.execute("""
                    SELECT m.item_name,
                        o.quantity,
                        (o.quantity * m.price) AS total
                    FROM orders o
                    JOIN menu m ON o.item_id = m.item_id
                    WHERE o.cust_id = ?
                """, (cust_id,))
                a = cur.fetchall()
                for i in a:
                    print(f"{i.item_name}    Quantity - {i.quantity}   total = {i.total}")

                a = input("would you like to get bill y/n: ").lower()
                if a == "y":
                    self.printBill(cust_id)
                    self.Save_Bill(cust_id)   
                break

            try:
                qnt = int(input("Quantity: "))
            except ValueError:
                print("Enter valid quantity")
                continue

            cur.execute("""
                SELECT item_id, price
                FROM menu
                WHERE item_name = ? AND is_available = 1
            """, (item_name,))

            row = cur.fetchone()

            if row is None:
                print("Item not found or not available.")
                continue

            item_id = row.item_id
            price = row.price

            total = qnt * price
            grand_total += total

            cur.execute("""
                INSERT INTO orders (item_id, quantity, status, cust_id)
                VALUES (?, ?, ?, ?)
            """, (item_id, qnt, "ordered", cust_id))

            cur.execute("""
                UPDATE Customer
                SET grandTotal = ?, time = GETDATE()
                WHERE cust_id = ?
            """, (grand_total, cust_id))

            con.commit()

            print("Grand total =", grand_total)

        return cust_id

menu1 = menu()
menu1.show_menu()
tk = TakeOrder()
tk.cust_Order()

# tk.printBill(44)




