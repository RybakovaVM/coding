CREATE TABLE customers  (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    phone VARCHAR(15)
);
DESCRIBE customers;

CREATE TABLE pizzas   (
    pizza_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    price DECIMAL(5,2) CHECK (price >= 0)
);

CREATE TABLE employees  (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    role VARCHAR(30),
    salary DECIMAL(8,2) CHECK (salary > 0)
);

CREATE TABLE orders  (
    order_id  INT PRIMARY KEY AUTO_INCREMENT,
    customer_id  INT,
    order_date DATE,
    employee_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id )
);

CREATE TABLE order_items  (
    order_id  INT,
    pizza_id  INT,
    quantity  INT CHECK (quantity > 0),
    PRIMARY KEY (order_id, pizza_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (pizza_id) REFERENCES pizzas(pizza_id)
);

INSERT INTO customers (name, phone)
VALUES 
('Анна Иванова', '89990001122'),
('Петр Смирнов', '89990003344'),
('Сергей Кузнецов', '89990005566');

SELECT * FROM customers;

INSERT INTO employees (name, role, salary)
VALUES
('Мария Петрова', 'Повар', 45000.00),
('Игорь Соколов', 'Курьер', 40000.00);

INSERT INTO pizzas (name, price)
VALUES
('Маргарита', 750.00),
('Гавайская', 650.00),
('Мясная', 500.00);

INSERT INTO orders (customer_id, order_date, employee_id)
VALUES (1, CURDATE(), 2);

INSERT INTO order_items (order_id, pizza_id, quantity)
VALUES 
(1, 1, 1),
(1, 2, 1);

INSERT INTO orders (customer_id, order_date, employee_id)
VALUES (2, CURDATE(), 1);

INSERT INTO order_items (order_id, pizza_id, quantity)
VALUES 
(2, 3, 2);

UPDATE pizzas
SET price = price * 1.15;

SELECT * FROM pizzas;

UPDATE customers
SET phone = '89998887766'
WHERE customer_id = 3;

ALTER TABLE pizzas 
ADD category VARCHAR(20);

UPDATE pizzas 
SET category = CASE 
    WHEN name = 'Маргарита' THEN 'Классик'
    WHEN name = 'Гавайская' THEN 'Сладкая'
    WHEN name = 'Мясная' THEN 'Острая'
END;

CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    phone VARCHAR(20)
);

INSERT INTO suppliers (name, phone)
VALUES
('Алексей Кукушкин"', '89997778899'),
('Андрей Сорокин', '89996665544');

ALTER TABLE pizzas
ADD supplier_id INT;

ALTER TABLE pizzas
ADD FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id);

UPDATE pizzas SET supplier_id = 1 WHERE pizza_id IN (1, 2);
UPDATE pizzas SET supplier_id = 2 WHERE pizza_id = 3;

SELECT o.order_id, c.name AS customer_name, e.name AS employee_name, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN employees e ON o.employee_id = e.employee_id;

SELECT pz.name, SUM(oi.quantity) AS total_order
FROM pizzas pz
JOIN order_items oi ON pz.pizza_id = oi.pizza_id
GROUP BY pz.name;

DELETE FROM orders
WHERE order_date < CURDATE();

DELETE FROM customers
WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM orders);

TRUNCATE TABLE suppliers ;
DROP TABLE suppliers ;
