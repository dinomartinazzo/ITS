
 Design a database schema for an online store.
 
Designing a database schema for an online merchandise store involves organizing the data that will be stored in the database, ensuring that it can efficiently handle the store's operations. Below is a simplified example of a database schema for an online merchandise store. Please note that this is a basic representation, and a real-world application may require additional tables and fields to meet specific requirements.

Entities and Relationships: 
1. Customers:
- customer_id (Primary Key)
- first_name
- last_name
- email
- password
- address
- phone_number 
2. Products:
- product_id (Primary Key)
- name
- description
- price
- category_id (Foreign Key)
- manufacturer_id (Foreign Key) 
3. Categories:
- category_id (Primary Key)
- name 
4. Manufacturers:
- manufacturer_id (Primary Key)
- name
- country
- website 
5. Orders:
- order_id (Primary Key)
- customer_id (Foreign Key)
- order_date
- status (e.g., "Processing," "Shipped," "Delivered") 
6. Order_Items:
- order_item_id (Primary Key)
- order_id (Foreign Key)
- product_id (Foreign Key)
- quantity
- item_price (price at the time of purchase) 
7. Reviews:
- review_id (Primary Key)
- product_id (Foreign Key)
- customer_id (Foreign Key)
- rating
- review_text
- review_date 
8. Cart:
- cart_id (Primary Key)
- customer_id (Foreign Key) 
9. Cart_Items:
- cart_item_id (Primary Key)
- cart_id (Foreign Key)
- product_id (Foreign Key)
- quantity

Database Schema Diagram:

```markdown
Customers ----1-----* Orders ----*-----1 Order_Items -----*----1 Products
  |              |              |                      |
  |              |              |                      |
  |              |              |                      |
  * Categories  * Manufacturers  * Reviews             * Cart
```



In this schema:
- Customers can place orders, and each order can contain multiple products.
- Each product belongs to a category and a manufacturer.
- Reviews are associated with products and customers.
- Customers can have items in their shopping cart, and each cart item corresponds to a product.
- The "cart" table stores cart-specific information for each customer, allowing them to add and remove items before making a purchase.
- The "status" field in the "Orders" table can be used to track the order's processing status.

This is a basic schema, and depending on the specific requirements of your online merchandise store, you may need to add more tables or fields to handle things like shipping information, promotions, and payment processing. Additionally, consider implementing data validation, indexing, and appropriate constraints to maintain data integrity and optimize database performance.

 ***

To create the tables in SQLite, you can use SQL statements as follows. SQLite uses a simplified data type system compared to some other database systems. Below is the SQL code for creating the tables using SQLite:

```sql
-- Customers table
CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    address TEXT,
    phone_number TEXT
);

-- Categories table
CREATE TABLE Categories (
    category_id INTEGER PRIMARY KEY,
    name TEXT
);

-- Manufacturers table
CREATE TABLE Manufacturers (
    manufacturer_id INTEGER PRIMARY KEY,
    name TEXT,
    country TEXT,
    website TEXT
);

-- Products table
CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    price REAL,
    category_id INTEGER,
    manufacturer_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id),
    FOREIGN KEY (manufacturer_id) REFERENCES Manufacturers(manufacturer_id)
);

-- Orders table
CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    status TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Order_Items table
CREATE TABLE Order_Items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    item_price REAL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Reviews table
CREATE TABLE Reviews (
    review_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    customer_id INTEGER,
    rating INTEGER,
    review_text TEXT,
    review_date DATE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Cart table
CREATE TABLE Cart (
    cart_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Cart_Items table
CREATE TABLE Cart_Items (
    cart_item_id INTEGER PRIMARY KEY,
    cart_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY (cart_id) REFERENCES Cart(cart_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
```



These SQL statements create the tables in an SQLite database using the appropriate data types and constraints. Note that in SQLite, you generally use `INTEGER` for auto-increment primary keys, `TEXT` for string data, and `REAL` for floating-point numbers. You may adjust the data types as needed based on your specific requirements.

 
I'll provide you with example SQL statements to insert 10 sample values into each of the tables you created in SQLite. Please note that these are just sample values, and you can modify them to match your specific data.

```sql
-- Insert values into the Customers table
INSERT INTO Customers (first_name, last_name, email, password, address, phone_number)
VALUES
    ('John', 'Doe', 'john.doe@email.com', 'password1', '123 Main St', '555-123-4567'),
    ('Jane', 'Smith', 'jane.smith@email.com', 'password2', '456 Elm St', '555-234-5678'),
    ('Bob', 'Johnson', 'bob.johnson@email.com', 'password3', '789 Oak St', '555-345-6789'),
    ('Alice', 'Williams', 'alice.williams@email.com', 'password4', '101 Pine St', '555-456-7890'),
    ('David', 'Lee', 'david.lee@email.com', 'password5', '202 Cedar St', '555-567-8901'),
    ('Sarah', 'Anderson', 'sarah.anderson@email.com', 'password6', '303 Birch St', '555-678-9012'),
    ('Michael', 'Brown', 'michael.brown@email.com', 'password7', '404 Maple St', '555-789-0123'),
    ('Laura', 'Miller', 'laura.miller@email.com', 'password8', '505 Walnut St', '555-890-1234'),
    ('Steven', 'Wilson', 'steven.wilson@email.com', 'password9', '606 Cherry St', '555-901-2345'),
    ('Emily', 'Davis', 'emily.davis@email.com', 'password10', '707 Ash St', '555-012-3456');

-- Insert values into the Categories table
INSERT INTO Categories (name)
VALUES
    ('Clothing'),
    ('Electronics'),
    ('Home & Kitchen'),
    ('Toys & Games'),
    ('Books'),
    ('Sports & Outdoors'),
    ('Health & Beauty'),
    ('Jewelry'),
    ('Automotive'),
    ('Music');

-- Insert values into the Manufacturers table
INSERT INTO Manufacturers (name, country, website)
VALUES
    ('Nike', 'USA', 'www.nike.com'),
    ('Sony', 'Japan', 'www.sony.com'),
    ('KitchenAid', 'USA', 'www.kitchenaid.com'),
    ('LEGO', 'Denmark', 'www.lego.com'),
    ('Penguin Random House', 'USA', 'www.penguinrandomhouse.com'),
    ('Adidas', 'Germany', 'www.adidas.com'),
    ('L'Oréal', 'France', 'www.loreal.com'),
    ('Tiffany & Co.', 'USA', 'www.tiffany.com'),
    ('Ford', 'USA', 'www.ford.com'),
    ('Sony Music', 'USA', 'www.sonymusic.com');

-- Insert values into the Products table
INSERT INTO Products (name, description, price, category_id, manufacturer_id)
VALUES
    ('T-Shirt', 'Cotton T-Shirt', 19.99, 1, 1),
    ('PlayStation 5', 'Gaming Console', 499.99, 2, 2),
    ('Stand Mixer', 'Kitchen Appliance', 299.99, 3, 3),
    ('LEGO Classic', 'Building Blocks', 29.99, 4, 4),
    ('The Great Gatsby', 'Novel', 12.99, 5, 5),
    ('Running Shoes', 'Athletic Shoes', 89.99, 6, 6),
    ('Shampoo', 'Hair Care Product', 6.99, 7, 7),
    ('Diamond Necklace', 'Jewelry', 999.99, 8, 8),
    ('Ford F-150', 'Truck', 39999.99, 9, 9),
    ('Vinyl Record', 'Music', 24.99, 10, 10);

-- Insert values into the Orders table
-- (You'll need to replace customer_id and use a valid value)
INSERT INTO Orders (customer_id, order_date, status)
VALUES
    (1, '2023-11-04', 'Processing'),
    (2, '2023-11-03', 'Shipped'),
    (3, '2023-11-02', 'Delivered'),
    (4, '2023-11-01', 'Processing'),
    (5, '2023-10-31', 'Shipped'),
    (6, '2023-10-30', 'Delivered'),
    (7, '2023-10-29', 'Processing'),
    (8, '2023-10-28', 'Shipped'),
    (9, '2023-10-27', 'Delivered'),
    (10, '2023-10-26', 'Processing');

-- Insert values into the Order_Items table
-- (You'll need to replace order_id and product_id with valid values)
INSERT INTO Order_Items (order_id, product_id, quantity, item_price)
VALUES
    (1, 1, 2, 39.98),
    (2, 2, 1, 499.99),
    (3, 3, 1, 299.99),
    (4, 4, 3, 89.97),
    (5, 5, 4, 51.96),
    (6, 6, 2, 179.98),
    (7, 7, 5, 34.95),
    (8, 8, 1, 999.99),
    (9, 9, 1, 39999.99),
    (10, 10, 3, 74.97);

-- Insert values into the Reviews table
-- (You'll need to replace product_id and customer_id with valid values)
INSERT INTO Reviews (product_id, customer_id, rating, review_text, review_date)
VALUES
    (1, 1, 5, 'Great T-Shirt!', '2023-11-04'),
    (2, 2, 4, 'Awesome console', '2023-11-03'),
    (3, 3, 5, 'Love my mixer', '2023-11-02'),
    (4, 4, 5, 'Best LEGO set', '2023-11-01'),
    (5, 5, 4, 'Classic novel', '2023-10-31'),
    (6, 6, 5, 'Perfect running shoes', '2023-10-30'),
    (7, 7, 3, 'Good shampoo', '2023-10-29'),
    (8, 8, 5, 'Beautiful necklace', '2023-10-28'),
    (9, 9, 4, 'Solid truck', '2023-10-27'),
    (10, 10, 5, 'Awesome record', '2023-10-26');

-- Insert items into the cart (replace cart_id and product_id with actual values)
-- Add 2 units of the product with ID 2 to the cart
-- Add 3 units of the product with ID 5 to the cart

INSERT INTO Cart_Items (cart_id, product_id, quantity)
VALUES
    (1, 2, 2), 
    (1, 5, 3);

```

 ***
SQLite supports a wide range of SQL queries for retrieving, updating, and managing data. Here are some examples of significant queries in SQLite: 
1. **SELECT Statement** : 
- Retrieve all columns from a table:

```sql
SELECT * FROM Customers;
``` 
- Retrieve specific columns from a table:

```sql
SELECT first_name, last_name FROM Customers;
``` 
- Filter rows using a WHERE clause:

```sql
SELECT * FROM Products WHERE price < 50.00;
``` 
- Join multiple tables:

```sql
SELECT Customers.first_name, Orders.order_date
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id;
``` 
2. **INSERT Statement** : 
- Insert a new customer record into the Customers table:

```sql
INSERT INTO Customers (first_name, last_name, email, password, address, phone_number)
VALUES ('New', 'Customer', 'new.customer@email.com', 'newpassword', '123 New St', '555-987-6543');
``` 
3. **UPDATE Statement** : 
- Update a customer's phone number:

```sql
UPDATE Customers
SET phone_number = '555-555-5555'
WHERE customer_id = 1;
``` 
4. **DELETE Statement** : 
- Delete a specific product from the Products table:

```sql
DELETE FROM Products
WHERE product_id = 3;
``` 
5. **Aggregation Queries** : 
- Calculate the total price of all items in an order:

```sql
SELECT SUM(item_price) AS total_price
FROM Order_Items
WHERE order_id = 1;
``` 
- Find the average rating for a product:

```sql
SELECT AVG(rating) AS average_rating
FROM Reviews
WHERE product_id = 1;
``` 
6. **Grouping and Aggregating Data** : 
- Count the number of orders for each customer:

```sql
SELECT customer_id, COUNT(*) AS order_count
FROM Orders
GROUP BY customer_id;
``` 
7. **Subqueries** : 
- Find the customers who placed orders in the last week:

```sql
SELECT customer_id, first_name, last_name
FROM Customers
WHERE customer_id IN (
    SELECT customer_id
    FROM Orders
    WHERE order_date >= DATE('now', '-7 days')
);
``` 
8. **Sorting Results** : 
- Retrieve products in a specific category, ordered by price:

```sql
SELECT name, price
FROM Products
WHERE category_id = 1
ORDER BY price;
``` 
9. **Limiting Results** : 
- Retrieve the top 5 highest-rated products:

```sql
SELECT name, rating
FROM Products
ORDER BY rating DESC
LIMIT 5;
```

These are just a few examples of the types of queries you can perform in SQLite. Depending on your specific application and data, you may need to write more complex queries and use various SQL features provided by SQLite to manipulate and retrieve data as needed.


Here are some significant SQL queries in SQLite that involve multiple tables and utilize relationships between them: 
1. **Retrieve Customer's Orders** : 
- Retrieve a customer's orders along with order details:

```sql
SELECT Customers.first_name, Customers.last_name, Orders.order_id, Order_Items.product_id, Products.name, Order_Items.quantity
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id
JOIN Order_Items ON Orders.order_id = Order_Items.order_id
JOIN Products ON Order_Items.product_id = Products.product_id
WHERE Customers.customer_id = 1;
``` 
2. **Retrieve Product Reviews** : 
- Retrieve product reviews with customer names:

```sql
SELECT Products.name, Reviews.rating, Reviews.review_text, Customers.first_name, Customers.last_name
FROM Products
JOIN Reviews ON Products.product_id = Reviews.product_id
JOIN Customers ON Reviews.customer_id = Customers.customer_id;
``` 
3. **Calculate Total Order Value** : 
- Calculate the total value of each order:

```sql
SELECT Orders.order_id, SUM(Order_Items.item_price) AS total_order_value
FROM Orders
JOIN Order_Items ON Orders.order_id = Order_Items.order_id
GROUP BY Orders.order_id;
``` 
4. **Find Customers with Most Orders** : 
- Find the customers with the most orders:

```sql
SELECT Customers.first_name, Customers.last_name, COUNT(Orders.order_id) AS order_count
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id
GROUP BY Customers.customer_id
ORDER BY order_count DESC
LIMIT 5;
``` 
5. **Retrieve Cart Items for a Customer** : 
- Retrieve items in a customer's shopping cart:

```sql
SELECT Customers.first_name, Customers.last_name, Products.name, Cart_Items.quantity
FROM Customers
JOIN Cart ON Customers.customer_id = Cart.customer_id
JOIN Cart_Items ON Cart.cart_id = Cart_Items.cart_id
JOIN Products ON Cart_Items.product_id = Products.product_id
WHERE Customers.customer_id = 1;
``` 
6. **Find Products with No Reviews** : 
- Find products with no reviews:

```sql
SELECT Products.name
FROM Products
LEFT JOIN Reviews ON Products.product_id = Reviews.product_id
WHERE Reviews.review_id IS NULL;
``` 
7. **Calculate Average Product Price by Category** : 
- Calculate the average price of products in each category:

```sql
SELECT Categories.name, AVG(Products.price) AS avg_price
FROM Categories
JOIN Products ON Categories.category_id = Products.category_id
GROUP BY Categories.category_id;
```

These queries illustrate how you can leverage relationships between tables to retrieve meaningful information from your SQLite database. They involve various SQL operations, such as JOINs, aggregations, and filtering, to perform complex data analysis and retrieval. You can adapt and modify these queries to suit your specific requirements and database schema.

SQL queries in SQLite that involve table relationships: 
1. **Find Customers with Most Expensive Orders** : 
- Find the customers with the highest total order values:

```sql
SELECT Customers.first_name, Customers.last_name, SUM(Order_Items.item_price) AS total_spent
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id
JOIN Order_Items ON Orders.order_id = Order_Items.order_id
GROUP BY Customers.customer_id
ORDER BY total_spent DESC
LIMIT 5;
``` 
2. **Retrieve Latest Review for Each Product** : 
- Retrieve the most recent review for each product:

```sql
SELECT Products.name, Reviews.rating, Reviews.review_text, Reviews.review_date
FROM Products
LEFT JOIN Reviews ON Products.product_id = Reviews.product_id
WHERE Reviews.review_date = (SELECT MAX(review_date) FROM Reviews WHERE product_id = Products.product_id);
``` 
3. **Calculate Total Sales by Manufacturer** : 
- Calculate the total sales for products from each manufacturer:

```sql
SELECT Manufacturers.name, SUM(Order_Items.item_price) AS total_sales
FROM Manufacturers
JOIN Products ON Manufacturers.manufacturer_id = Products.manufacturer_id
JOIN Order_Items ON Products.product_id = Order_Items.product_id
GROUP BY Manufacturers.manufacturer_id;
``` 
4. **Find Out of Stock Products** : 
- Find products that are out of stock (quantity in cart equals zero):

```sql
SELECT Products.name
FROM Products
LEFT JOIN Cart_Items ON Products.product_id = Cart_Items.product_id
WHERE Cart_Items.quantity IS NULL OR Cart_Items.quantity = 0;
``` 
5. **Retrieve Average Ratings by Category** : 
- Retrieve the average ratings of products in each category:

```sql
SELECT Categories.name, AVG(Reviews.rating) AS avg_rating
FROM Categories
JOIN Products ON Categories.category_id = Products.category_id
LEFT JOIN Reviews ON Products.product_id = Reviews.product_id
GROUP BY Categories.category_id;
``` 
6. **Find Customers with Specific Product in Cart** : 
- Find customers who have a specific product in their cart:

```sql
SELECT Customers.first_name, Customers.last_name
FROM Customers
JOIN Cart ON Customers.customer_id = Cart.customer_id
JOIN Cart_Items ON Cart.cart_id = Cart_Items.cart_id
JOIN Products ON Cart_Items.product_id = Products.product_id
WHERE Products.name = 'T-Shirt';
``` 
7. **Retrieve Customers with Multiple Orders on the Same Day** : 
- Retrieve customers who placed multiple orders on the same day:

```sql
SELECT Customers.first_name, Customers.last_name, Orders.order_date
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id
WHERE Orders.order_date IN (
    SELECT order_date
    FROM Orders
    GROUP BY order_date
    HAVING COUNT(order_id) > 1
);
```

These additional queries demonstrate how to extract valuable insights from your database by working with table relationships, performing aggregations, and utilizing various SQL clauses. You can adapt these queries to suit your specific use case and database schema.
