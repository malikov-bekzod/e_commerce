from connection import postgres_conn

cursor = postgres_conn.cursor()

def insert_data():
    countries = ["uzbekistan","america","korea","russia"]
    for i in countries:
        cursor.execute(f"INSERT INTO country(country) VALUES('{i}')")


    regions = ['Samarqand','andijan', 'fergana', 'tashkent']
    for i in regions:
        cursor.execute(F"""INSERT INTO region(region, country_id) VALUES('{i}',1)""")

    
    addresses = ["124 oqsaroy","134 qorakocha", "47A gulbog", "234 oybek"]
    for i in addresses:
        cursor.execute(f"INSERT INTO address(address, address2, district, region_id, phone) VALUES('{i}','','nurafshon',4,'+998-93-668-00-43')")


    datas = [("alien","max","jared.ely@sakilacustomer.org","user123"),
             ("john","brown","mary.smith@sakilacustomer.org","adminuser"),
             ("smith","jake","patricia.johnson@sakilacustomer.org","userqwerty"),
             ("robert","alberto","linda.williams@sakilacustomer.org","user")]
    for i,j,k,l in datas:
        cursor.execute(f"INSERT INTO customer(first_name,last_name,email,username,password,address_id,create_date) VALUES('{i}','{j}','{k}','{l}','12345678',1,'2020-10-23')")


    for i in range(1,4):
        cursor.execute(f"INSERT INTO basket(customer_id) VALUES({i})")


    categories = ["clothes","electronics","food","toys for children"]
    for i in categories:
        cursor.execute(f"INSERT INTO category(name) VALUES('{i}')")


    stores = [("techno","bizning dokonda eng arzon va sifatli mahsulotlar sotiladi"),
              ("smart","son sifat belgisi emas"),
              ("techno","eng arzon va raqobatdosh mahsulotlar sotiladi"),]
    for i,j in stores:
        cursor.execute(f"INSERT INTO store(name,description) VALUES('{i}','{j}')")


    cursor.execute("INSERT INTO product(name,description,price,amount,category_id,store_id) VALUES('smartphone Samsung Galaxy A15 6GB RAM, 128GB, FHD+ 90 Hz', 'Galaxy A15 6,5 dyuymli Super AMOLED displeyga ega',2_099_000,55,2,1)")

    cursor.execute("INSERT INTO product(name,description,price,amount,category_id,store_id) VALUES('Oila tanlovi, tozalangan va deodorizatsiyalangan, 900 ml', 'Oila tanlovi kungaboqar yogi - mehr bilan tayyorlangan taomlar uchun. Yuqori sifatli kungaboqar uruglaridan tayyorlangan, boy vitamin tarkibi va soglom yogli kislotalarga ega.',10_000,27,3,2)")

    cursor.execute("INSERT INTO product(name,description,price,amount,category_id,store_id) VALUES('smartphone Samsung Galaxy A71 6GB RAM, 128GB, FHD+ 90 Hz', 'Galaxy A71 6,5 dyuymli Super AMOLED displeyga ega',4_300_000.154,10,2,3)")


    for i in range(1,4):
        cursor.execute(f"INSERT INTO \"order\" VALUES({i},{i})")
    

    cursor.execute("INSERT INTO \"basket_product\" VALUES(1,2)")
    cursor.execute("INSERT INTO \"basket_product\" VALUES(1,2)")
    cursor.execute("INSERT INTO \"basket_product\" VALUES(3,3)")


    print("INSERT 0 1")
    
    postgres_conn.commit()
