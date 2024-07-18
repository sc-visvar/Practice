CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary NUMERIC(10, 2) NOT NULL
);


INSERT INTO employees (name, position, salary) VALUES
('Alice Johnson', 'Software Engineer', 70000.00),
('Bob Smith', 'Project Manager', 85000.00),
('Charlie Brown', 'Data Analyst', 60000.00);
