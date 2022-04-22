import sqlite3

con = sqlite3.connect("projectDB.db")
print("Database created successfully")

# con.execute("drop table users")
# con.execute("create table users(name text not null, gender text not null, email text primary key not null, phone text not null, password text not null);")
# con.execute("insert into users('raman','male','r@gmail.com','123456789','1234')")
# con.execute("DELETE FROM users WHERE email = 'abc@gmail.com';")

# con.execute('drop table products')
# con.execute("create table products(id integer primary key autoincrement, name text not null, image text not null, price float not null, onSale integer, onSalePrice float not null, kind text not null);")


# con.execute("create table cart(image text,name text,qty integer, price text, subTotal text, id integer );")

# con.execute('drop table purchases')
# con.execute("create table purchases(uid integer primary key autoincrement,
# name text, image text, quantity integer, mail varchar(50), date text);") con.commit()

print("users")
res = con.execute("SELECT * FROM users")
for i in res:
    print(i[0], i[1], i[2], i[3], i[4])

print()
# con.execute('''create table complaint(order_id integer primary key,name text, prod_name text,date integer,descr text)''')
print("help and complaint table created")
# con.execute("create table queries(name text,phone text,mail integer, message text);")
print("complaint")
res = con.execute("SELECT * FROM complaint")
for i in res:
    print(i[0], i[1], i[2], i[3], i[4])

print()

res = con.execute("SELECT * FROM queries")
for i in res:
    print(i[0], i[1], i[2], i[3])

# con.execute('delete from users where user_id<11')
# con.execute("create table deliveryDetails(name text, mobile text, ddate text, mail text, method text, address text);")
# con.execute("drop table deliverydetails")
con.commit()
# con.execute("drop table purchases")
res = con.execute("SELECT * FROM deliveryDetails")
for i in res:
    print(i[0], i[1], i[2], i[3], i[4], i[5])

# con.execute('drop table products')
'''
con.execute("create table products(id integer primary key autoincrement, prod_name text not null, image text not null, "
           "price float not null, category text not null,quantity integer not null);")
con.execute("INSERT INTO products VALUES ('000001', 'Real Mixed Fruit Juice 1L','real_juice.png',100,'Beverages',20)")
con.execute(
    "INSERT INTO products VALUES ('000002', 'Cadbury Hot Chocolate Powder Mix 200g','cadbury_hot.png',165, 'Beverages',15)")
con.execute("INSERT INTO products VALUES ('000003', 'Cadbury Bournvita Health 500g','bournvita.png',89, 'Beverages',20)")
con.execute("INSERT INTO products VALUES ('000004', 'Coca-Cola PET Bottle 2L','coke.png',85,'Beverages',50)")
con.execute("INSERT INTO products VALUES ('000005', 'Nestea Iced Tea Lemon 400g','iced_tea.png',190, 'Beverages',10)")
con.execute(
    "INSERT INTO products VALUES ('000006', 'Hershey Choclate Flavor Syrup 200g','hershey_syrup.png',90, 'Beverages',25)")
con.execute("INSERT INTO products VALUES ('000007', 'TANG Orange Instant Drink Mix 500g','tang.png',135, 'Beverages',20)")
con.execute("INSERT INTO products VALUES ('000008', 'BRU Gold Instant Coffee 100g','coffee.png',295, 'Beverages',100)")

con.execute("INSERT INTO products VALUES ('100000', 'amul butter','butter.png',47, 'Dairy',50)")
con.execute("INSERT INTO products VALUES ('100001', 'mother dairy milk','milk.png',30, 'Dairy',200)")
con.execute("INSERT INTO products VALUES ('100002', 'Amul Dahi','amul_dahi.png',47, 'Dairy',50)")
con.execute("INSERT INTO products VALUES ('100003', 'amul paneer','amul_paneer.png',30, 'Dairy',50)")

con.execute("INSERT INTO products VALUES ('200000', 'Potato Fresh 1Kg','Potato Fresh 1Kg.png',50, 'Fruits&veggies',200)")
con.execute("INSERT INTO products VALUES ('200001', 'Onion 1kg','Onion 1kg.png',80,'Fruits&veggies',200)")
con.execute("INSERT INTO products VALUES ('200002', 'Cauliflower 1Kg','Cauliflower 1Kg.png',40, 'Fruits&veggies',50)")
con.execute("INSERT INTO products VALUES ('200003', 'Fresh Green Peas 1Kg','Fresh Green Peas 1Kg.png',80,"
            "'Fruits&veggies',50)")
con.execute("INSERT INTO products VALUES ('200004', 'Mango 1Kg','Mango 1Kg.png',280, 'Fruits&veggies',50)")
con.execute("INSERT INTO products VALUES ('200005', 'Apple 1Kg','Apple 1Kg.png',70, 'Fruits&veggies',50)")
con.execute("INSERT INTO products VALUES ('200006', 'Long Grain Rice','Long Grain Rice.png',40,'staples',100)")
con.execute("INSERT INTO products VALUES ('200007', 'AASHIRVAAD AATA','AASHIRVAAD AATA.png',50,'staples',500)")
con.execute("INSERT INTO products VALUES ('200008', 'Rajma Daal','Rajma Daal.png',80, 'staples',50)")
con.execute("INSERT INTO products VALUES ('200009', 'Moong Daal','Moong Daal.png',70,'staples',50)")
con.execute("INSERT INTO products VALUES ('200010', 'TATA SALT','TATA SALT.png',20, 'staples',100)")
con.execute("INSERT INTO products VALUES ('200011', 'Sugar','sugar.png',60,'staples',100)")
con.execute("INSERT INTO products VALUES ('200012', 'TATA TEA','TATA TEA.png',80, 'staples',100)")
'''
con.commit()
print("purchase")
res = con.execute('select * from users')
for i in res:
    print(i[0], i[1], i[2], i[3], i[4])
con.execute("update products set image='Long Grain Rice.png' where id='200006'")
con.execute("update products set image='Rajma Daal.png' where id='200008'")
con.execute("update products set image='Onion 1kg.png' where id='200001'")
con.commit()
