# E-commerce-System
This project is a command-line-based e-commerce system designed to simulate an online shopping platform. It allows users to perform various shopping operations and administrators to manage the system efficiently.

**Features**

**Customers:**
1. Login and browse products.
2. Purchase items and view order history.
3. Generate consumption reports.

**Administrators:**
1. Manage customers, products, and orders (create, delete, view).
2. Access statistical insights about the system.
3. Classes and Structure

The system is implemented using object-oriented principles, with the following key classes:

**2. Instruction**
**2.1. User Class**

Defines attributes and behaviors shared by all users (customers and admins).

**2.2. Customer Class**

Inherits from the User class and includes customer-specific attributes and methods, such as order history and report generation.

**2.3. Admin Class**

Inherits from the User class and includes admin-specific attributes and methods, such as user management and statistics viewing.

**2.4. Product Class**

Represents the product entity with details like name, price, and stock.

**2.5. Order Class**

Manages order-related attributes and tracks order details for customers.

**2.6. UserOperation Class**

Defines common operations for users, such as login and authentication.

**2.7. CustomerOperation Class**

Handles customer-specific actions, including purchasing and viewing order history.

**2.8. AdminOperation Class**

Manages admin-specific actions, such as managing users and accessing system statistics.

**2.9. ProductOperation Class**

Handles operations related to managing products, including adding, updating, and deleting products.

**2.10. OrderOperation Class**

Handles order-related actions, such as processing purchases and generating order reports.

**2.11. Interface Class**

Provides a well-structured user interface for interaction with the system, guiding users through operations with clear prompts.

**2.12. Main File**

The entry point for the application, coordinating the overall flow of the system.

**Data Source**

Product data is sourced from an open dataset hosted on data.world, consisting of 9 files containing product information.

**Usage**

1. Clone this repository.
2. Run the Main File to start the application.
3. Follow the prompts on the command-line interface to navigate the system.
