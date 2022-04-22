import sqlite3
from datetime import datetime

from cs50 import SQL
from flask import Flask, render_template, request, session

from flask_session import Session

# # Instantiate Flask object named app
app = Flask(__name__, static_url_path='/static')

# # Configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Creates a connection to the database
db = SQL("sqlite:///projectDB.db")


@app.route("/")
def loginPage():
    return render_template("login1.html")


@app.route("/home")
def home():
    return render_template("userhome.html")


@app.route("/admin")
def adminpage():
    return render_template("/admin/admin.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/about')
def aboutPage():
    return render_template("about.html")


@app.route("/support")
def support():
    return render_template("support.html")


@app.route("/complaint", methods=["POST"])
def complaint():
    id = int(request.form["id"])
    user = request.form["name"]
    prodname = request.form["pname"]
    query = request.form["subject"]
    date = request.form["date"]
    try:
        with sqlite3.connect('projectDB.db') as conn:
            res = conn.execute("select * from purchases where uid=?", (id,))
            for i in res:
                pid = i[0]
                print("akdkandkandk", type(pid))
                print(type(id))
                # prod_name = i[1]
                # user = i[2]
            if id == pid:
                conn.execute("insert into complaint (order_id,name,prod_name,date,descr) values(?,?,?,?,?)",
                             (id, user, prodname, date, query))
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                res = cur.execute("select * from complaint where name=?", (user,))
                for i in res:
                    pid = i[0]
                    cname = i[1]
                    pname = i[2]
                    date = i[3]
                    query = i[4]
                # rows = conn.fetchall()
                return render_template("complaint_register.html", ms1=pid, ms2=cname, ms3=pname, ms4=date,
                                       ms5=query)
    except:
        return pid, cname, pname, date, query


@app.route("/signup", methods=["POST"])
def add():
    t = ""
    if request.method == "POST":
        try:
            a = request.form["username"]
            b = request.form["gender"]
            c = request.form["email"]
            d = request.form["mobile"]
            e = request.form["password"]
            with sqlite3.connect("projectDB.db") as con:
                cur = con.cursor()
                cur.execute("insert into users (name,gender,email,phone,password) values (?,?,?,?,?)", (a, b, c, d, e))
                con.commit()
            session["email"] = request.form.get("email")
        except Exception as err:
            cur.rollback()
            t = "Can't be registered {}".format(err)
        finally:
            return render_template("login1.html")


@app.route("/verify", methods=["POST"])
def verify():
    email = request.form["uemail"]
    password = request.form["pwd"]
    p = ""
    if email == "admin" and password == "12345":
        return render_template("/admin/admin.html")
    else:
        try:
            with sqlite3.connect("projectDB.db") as con:
                cur = con.cursor()
                s = "Select password from users where email==?"
                result = cur.execute(s, (email,))
                for row in result:
                    p = row[0]
        except Exception as err:
            con.rollback()
            return "{}".format(err)
        finally:
            if p == password:
                query = "SELECT * FROM users WHERE email = :email AND password = :password"
                rows = db.execute(query, email=email, password=password)

                # If username and password match a record in database, set session variables
                if len(rows) == 1:
                    session['mail'] = email
                    session['time'] = datetime.now()
                    session['mail'] = rows[0]["email"]
                return render_template("userhome.html")
            else:
                return "Invalid Credentials"


@app.route("/index")
def index():
    products = db.execute("SELECT * FROM products ORDER BY id")
    productsLen = len(products)
    # Initialize variables
    shoppingCart = []
    shopLen = len(shoppingCart)
    totItems, total, display = 0, 0, 0
    if 'user' in session:
        shoppingCart = db.execute("SELECT name, image, SUM(qty), SUM(subTotal), price, id FROM cart GROUP BY name")
        shopLen = len(shoppingCart)
        for i in range(shopLen):
            total += shoppingCart[i]["SUM(subTotal)"]
            totItems += shoppingCart[i]["SUM(qty)"]
        products = db.execute("SELECT * FROM products ORDER BY name ASC")
        productsLen = len(products)
        return render_template("index.html", shoppingCart=shoppingCart, products=products, shopLen=shopLen,
                               productsLen=productsLen, total=total, totItems=totItems, display=display,
                               session=session)

    return render_template("index.html", products=products, shoppingCart=shoppingCart, productsLen=productsLen,
                           shopLen=shopLen, total=total, totItems=totItems, display=display)


@app.route("/cart/")
def cart():
    # Clear shopping cart variables
    totItems, total, display = 0, 0, 0
    # Grab info currently in database
    shoppingCart = db.execute("SELECT name, image, SUM(qty), SUM(subTotal), price, id FROM cart GROUP BY name")
    # Get variable values
    shopLen = len(shoppingCart)
    for i in range(shopLen):
        total += shoppingCart[i]["SUM(subTotal)"]
        totItems += shoppingCart[i]["SUM(qty)"]
    # Render shopping cart
    return render_template("cart.html", shoppingCart=shoppingCart, shopLen=shopLen, total=total, totItems=totItems,
                           display=display, session=session)


@app.route("/filter/")
def filter():
    if request.args.get('category'):
        query = request.args.get('category')
        products = db.execute("SELECT * FROM products WHERE category = :query ORDER BY id ", query=query)
    productsLen = len(products)
    # Initialize shopping cart variables
    shoppingCart = []
    shopLen = len(shoppingCart)
    totItems, total, display = 0, 0, 0
    if 'user' in session:
        # Rebuild shopping cart
        shoppingCart = db.execute("SELECT name, image, SUM(qty), SUM(subTotal), price, id FROM cart GROUP BY category")
        shopLen = len(shoppingCart)
        for i in range(shopLen):
            total += shoppingCart[i]["SUM(subTotal)"]
            totItems += shoppingCart[i]["SUM(qty)"]
        # Render filtered view
        return render_template("index.html", shoppingCart=shoppingCart, products=products, shopLen=shopLen,
                               productsLen=productsLen, total=total, totItems=totItems, display=display,
                               session=session)
    # Render filtered view
    return render_template("index.html", products=products, shoppingCart=shoppingCart, productsLen=productsLen,
                           shopLen=shopLen, total=total, totItems=totItems, display=display)


@app.route("/buy/")
def buy():
    # Initialize shopping cart variables
    shoppingCart = []
    shopLen = len(shoppingCart)
    totItems, total, display = 0, 0, 0
    qty = int(request.args.get('quantity'))

    # Store id of the selected shirt
    id = int(request.args.get('id'))
    # Select info of selected shirt from database
    goods = db.execute("SELECT * FROM products WHERE id = :id", id=id)
    # Extract values from selected shirt record
    # Check if shirt is on sale to determine price
    price = goods[0]["price"]
    name = goods[0]["prod_name"]
    image = goods[0]["image"]
    subTotal = qty * price
    # Insert selected grocery into shopping cart
    db.execute("INSERT INTO cart (id, qty, name, image, price, subTotal) VALUES (:id, :qty, :name, :image, :price, "
               ":subTotal)", id=id, qty=qty, name=name, image=image, price=price, subTotal=subTotal)
    shoppingCart = db.execute("SELECT name, image, SUM(qty), SUM(subTotal), price, id FROM cart GROUP BY name")
    shopLen = len(shoppingCart)
    # Rebuild shopping cart
    for i in range(shopLen):
        total += shoppingCart[i]["SUM(subTotal)"]
        totItems += shoppingCart[i]["SUM(qty)"]
        # Select all shirts for home page view
    products = db.execute("SELECT * FROM products ORDER BY id ")
    productsLen = len(products)
    # Go back to home page
    return render_template("index.html", shoppingCart=shoppingCart, products=products, shopLen=shopLen,
                           productsLen=productsLen, total=total, totItems=totItems, display=display, session=session)


@app.route("/update/")
def update():
    # Initialize shopping cart variables
    shoppingCart = []
    totItems, total, display = 0, 0, 0
    qty = int(request.args.get('quantity'))

    # Store id of the selected shirt
    id = int(request.args.get('id'))
    db.execute("DELETE FROM cart WHERE id = :id", id=id)
    # Select info of selected shirt from database
    goods = db.execute("SELECT * FROM products WHERE id = :id", id=id)
    # Extract values from selected shirt record
    # Check if shirt is on sale to determine price
    price = goods[0]["price"]
    name = goods[0]["prod_name"]
    image = goods[0]["image"]
    subTotal = qty * price
    # Insert selected shirt into shopping cart
    db.execute(
        "INSERT INTO cart (id, qty, name, image, price, subTotal) VALUES (:id, :qty, :name, :image, :price, :subTotal)",
        id=id, qty=qty, name=name, image=image, price=price, subTotal=subTotal)
    shoppingCart = db.execute("SELECT name, image, SUM(qty), SUM(subTotal), price, id FROM cart GROUP BY name")
    shopLen = len(shoppingCart)
    # Rebuild shopping cart
    for i in range(shopLen):
        total += shoppingCart[i]["SUM(subTotal)"]
        totItems += shoppingCart[i]["SUM(qty)"]
        # Go back to cart page
    return render_template("cart.html", shoppingCart=shoppingCart, shopLen=shopLen, total=total, totItems=totItems,
                           display=display, session=session)


@app.route("/forgot")
def forget():
    return render_template("forgot.html")


@app.route("/forgot-pass", methods=['POST'])
def give_pass():
    if request.method == "POST":
        username = request.form["user"]
        email = request.form["mail"]
        phone = int(request.form["phone"])
        try:
            with sqlite3.connect("projectDB.db") as conn:
                res = conn.execute("select * from users where email=?", (email,))
                for i in res:
                    name = i[0]
                    pass1 = i[4]
                    mail = i[2]
                    mob = i[3]
                if name == username and mail == email:
                    return render_template("give_credentials.html", msg=name, ms1=pass1)
        except:
            return render_template("forgot.html")


@app.route("/remove/", methods=["GET"])
def remove():
    # Get the id of shirt selected to be removed
    out = int(request.args.get("id"))
    # Remove shirt from shopping cart
    db.execute("DELETE from cart WHERE id=:id", id=out)
    # Initialize shopping cart variables
    totItems, total, display = 0, 0, 0
    # Rebuild shopping cart
    shoppingCart = db.execute("SELECT name, image, SUM(qty), SUM(subTotal), price, id FROM cart GROUP BY name")
    shopLen = len(shoppingCart)
    for i in range(shopLen):
        total += shoppingCart[i]["SUM(subTotal)"]
        totItems += shoppingCart[i]["SUM(qty)"]
    # Turn on "remove success" flag
    display = 1
    # Render shopping cart
    return render_template("cart.html", shoppingCart=shoppingCart, shopLen=shopLen, total=total, totItems=totItems,
                           display=display, session=session)


@app.route("/placeOrder", methods=["POST"])
def placeOrder():
    name = request.form["q8_fullName"]
    phone = request.form["q11_contactNumber"]
    delivery = request.form["q12_selectDelivery"]
    # email = request.form["q7_email"]
    payment = request.form['q10_paymentMethod']
    msg = request.form["q4_message4"]
    db.execute(
        "INSERT INTO deliveryDetails (name,mobile,ddate,mail,method,address) VALUES(:a, :b, :c, :d, :e, :f)",
        d=session["email"], a=name, b=phone, c=delivery, e=payment, f=msg)
    totItems, total, display = 0, 0, 0
    # Grab info currently in database
    shoppingCart = db.execute("SELECT name, image, SUM(qty), SUM(subTotal), price, id FROM cart GROUP BY name")
    # Get variable values
    shopLen = len(shoppingCart)
    for i in range(shopLen):
        total += shoppingCart[i]["SUM(subTotal)"]
        totItems += shoppingCart[i]["SUM(qty)"]
    # Render shopping cart
    db.execute("DELETE from cart")
    return render_template("success.html", shoppingCart=shoppingCart, shopLen=shopLen, total=total, totItems=totItems,
                           display=display, session=session)


@app.route("/checkout/")
def checkout():
    order = db.execute("SELECT * from cart")
    # Update purchase history of current customer
    for item in order:
        db.execute(
            "INSERT INTO purchases (name, image, quantity,mail, date) VALUES(:name, :image, :quantity,:email, :date)",
            email=session["email"], name=item["name"], image=item["image"], quantity=item["qty"],
            date=session['time'])
    # Clear shopping cart
    # db.execute("DELETE from cart")
    # shoppingCart = []
    # shopLen = len(shoppingCart)
    # totItems, total, display = 0, 0, 0
    # Redirect to home page
    return render_template("checkout.html")


@app.route("/history/")
def history():
    # Initialize shopping cart variables
    shoppingCart = []
    shopLen = len(shoppingCart)
    totItems, total, display = 0, 0, 0
    # Retrieve all shirts ever bought by current user
    myProucts = db.execute("SELECT * FROM purchases WHERE mail=:email", email=session["email"])
    myProuctsLen = len(myProucts)
    # Render table with shopping history of current user
    return render_template("history.html", shoppingCart=shoppingCart, shopLen=shopLen, total=total, totItems=totItems,
                           display=display, session=session, myProucts=myProucts, myProuctsLen=myProuctsLen)


@app.route("/Showusers")
def view():
    con = sqlite3.connect("projectDB.db")
    con.row_factory = sqlite3.Row  # Converts the records in Dictionary format, it ain't in just object form anymore
    c = con.cursor()
    rows = c.execute("select * from users")
    return render_template("/admin/show_users.html", rows=rows)


@app.route("/viewhistory")
def viewhistory():
    con = sqlite3.connect("projectDB.db")
    con.row_factory = sqlite3.Row  # Converts the records in Dictionary format, it ain't in just object form anymore
    c = con.cursor()
    c.execute("select * from purchases")
    rows = c.fetchall()
    return render_template("viewhistory.html", rows=rows)


@app.route("/viewdelivery")
def viewdelivery():
    con = sqlite3.connect("projectDB.db")
    con.row_factory = sqlite3.Row  # Converts the records in Dictionary format, it ain't in just object form anymore
    c = con.cursor()
    c.execute("select * from deliveryDetails")
    rows = c.fetchall()
    return render_template("viewdelivery.html", rows=rows)


# ************************ADMIN MODULE*******************************************

@app.route('/ShowAllProducts', methods=['GET', 'POST'])
def show_all_products():
    with sqlite3.connect("projectDB.db") as conn:
        product_details = conn.execute("select id,prod_name,price,category,quantity from products")
        return render_template('/admin/show_products.html', product_details=product_details)


@app.route("/showcomplaints", methods=['GET', 'POST'])
def show_complaints():
    with sqlite3.connect("projectDB.db") as conn:
        complaints = conn.execute("select * from complaint")
        return render_template("/admin/show_complaints.html", complaints=complaints)


@app.route("/Showusers", methods=['GET', 'POST'])
def show_Users():
    with sqlite3.connect("projectDB.db") as conn:
        user_details = conn.execute("select name,gender,email,phone from users")
        return render_template("/admin/show_users.html", user=user_details)


@app.route('/InsertProduct', methods=['GET', 'POST'])
def add_products():
    if request.method == 'POST':
        if 'add_product' in request.form:
            # Take data from page
            id = request.form['product_id']
            name = request.form['product_name']
            category = request.form['product_category']
            price = request.form['product_price']
            quantity = request.form['product_quantity']
            image = request.form['image']

            # Insert in sql databaseProduct.add_product(pysql, name, category, price, seller, quantity)
            with sqlite3.connect("projectDB.db") as conn:
                ans = conn.execute(
                    "insert into products (id,prod_name,category,image,price,quantity) values(?,?,?,?,?)",
                    (id, name, category, price, image, quantity))
                if ans:
                    print('Successfully Added')
                else:
                    print('Error adding product in table')

    return render_template('/Admin/admin_insert.html')


@app.route('/updateproducts', methods=['GET', 'POST'])
def update_products():
    if request.method == 'POST':
        if 'update_prod' in request.form:

            id = request.form['product_id']
            name = request.form['product_name']
            category = request.form['product_category']
            price = request.form['product_price']
            quantity = request.form['product_quantity']
            image = request.form['image']

            with sqlite3.connect("projectDB.db") as conn:
                ans = conn.execute(
                    "update products set prod_name=?,category=?,price=?,quantity=? where id=?",
                    (name, category, price, quantity, id))
            if ans:
                print('Successfully Added')
            else:
                print('Error adding delivery executive in table')

    return render_template('/Admin/update.html')


@app.route('/deleteproducts', methods=['GET', 'POST'])
def Delete_products():
    if request.method == 'POST':
        if 'delete_prod' in request.form:
            id = request.form['product_id']
            with sqlite3.connect("projectDB.db") as conn:
                ans = conn.execute("delete from products where id=?", (id,))

    return render_template('/Admin/delete_prod.html')


@app.errorhandler(404)
def pageNotFound(e):
    if 'user' in session:
        return render_template("404.html", session=session)
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(debug=True, port=1000)
