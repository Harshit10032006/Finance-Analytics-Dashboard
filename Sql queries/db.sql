--Creation of the Tables 
CREATE TABLE Users (
    users_id INT PRIMARY KEY,
    names NVARCHAR(200),
    email NVARCHAR(200) NOT NULL,
    created_date DATETIME);

CREATE TABLE Accounts (
    account_id INT PRIMARY KEY,
    users_id INT,
    account_name NVARCHAR(200),
    account_type NVARCHAR(200),
    balance DECIMAL(10,2));

CREATE TABLE Categories (
    category_id INT PRIMARY KEY,
    category_name NVARCHAR(200),
    category_type NVARCHAR(200),
    parent_category_id INT);

CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    category_id INT,
    amount_date DATETIME,
    descriptions NVARCHAR(400),
    type NVARCHAR(200));

CREATE TABLE Budgets (
    budget_id INT PRIMARY KEY,
    users_id INT,
    category_id INT,
    amount DECIMAL(10,2),
    months NVARCHAR(20),
    years INT);

--Inserstion of Data in Tables 

CREATE OR ALTER PROCEDURE Insertion
AS
BEGIN
    IF OBJECT_ID('dbo.Users', 'U') IS NOT NULL
        TRUNCATE TABLE Users;

    BULK INSERT Users
    FROM 'C:\Users\kholi\Downloads\sql-data-warehouse-project\sql-data-warehouse-project\datasets\source_crm\Users_Indian.csv'
    WITH (
        FIRSTROW = 2,
        FIELDTERMINATOR = ',',
      
        TABLOCK
    );

    IF OBJECT_ID('Accounts', 'U') IS NOT NULL
        TRUNCATE TABLE Accounts;

    BULK INSERT Accounts
    FROM 'C:\Users\kholi\Downloads\sql-data-warehouse-project\sql-data-warehouse-project\datasets\source_crm\Accounts_Indian.csv'
    WITH (
        FIRSTROW = 2,
        FIELDTERMINATOR = ',',
      
        TABLOCK
    );
    IF OBJECT_ID('Categories', 'U') IS NOT NULL
        TRUNCATE TABLE Categories;

    BULK INSERT Categories
    FROM 'C:\Users\kholi\Downloads\sql-data-warehouse-project\sql-data-warehouse-project\datasets\source_crm\Categories_Indian.csv'
    WITH (
        FIRSTROW = 2,
        FIELDTERMINATOR = ',',
      
        TABLOCK
    );
    IF OBJECT_ID('Transactions', 'U') IS NOT NULL
        TRUNCATE TABLE Transactions;

    BULK INSERT Users
    FROM 'C:\Users\kholi\Downloads\sql-data-warehouse-project\sql-data-warehouse-project\datasets\source_crm\Transactions_Indian.csv'
    WITH (
        FIRSTROW = 2,
        FIELDTERMINATOR = ',',
      
        TABLOCK
    );
     IF OBJECT_ID('Budgets', 'U') IS NOT NULL
        TRUNCATE TABLE Budgets;

    BULK INSERT Budgets
    FROM 'C:\Users\kholi\Downloads\sql-data-warehouse-project\sql-data-warehouse-project\datasets\source_crm\Budgets_Indian.csv'
    WITH (
        FIRSTROW = 2,
        FIELDTERMINATOR = ',',
      
        TABLOCK);
END;



















