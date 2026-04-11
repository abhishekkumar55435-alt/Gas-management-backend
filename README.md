# Gas Agency Management System

A Python-based command-line application that simulates a basic Gas Agency management system. It provides interfaces for both customers and staff to handle gas cylinder bookings, user registrations, complaints, and order management. 

The application uses MySQL for database management to store customer details, orders, and staff credentials.

## Features

### Customer Interface
* **New User Registration:** Register as a new customer and receive an auto-generated unique User ID.
* **Book Cylinder:** Place an order for a new gas cylinder.
* **View Order:** Check current order status and expected delivery timelines.
* **Billing Details:** View the standard billing amount for the cylinder.
* **File a Complaint:** Submit brief complaints to the agency.
* **Cancel Order:** Cancel an active cylinder booking.
* **Surrender Connection:** Delete your customer account and connection permanently.

### Staff Interface
* **Staff Login:** Secure access for agency administrators.
* **View Orders:** See a list of all active cylinder bookings.
* **Delete Orders:** Manually remove specific orders using a Customer's User ID.
* **Delete Connection:** Terminate a customer's connection and delete their associated orders.

## Prerequisites

Before running this script, ensure you have the following installed on your system:
* **Python 3.x**
* **MySQL Server** (running locally)
* **MySQL Connector for Python**

You can install the required Python library using pip:
```bash
pip install mysql-connector-python
