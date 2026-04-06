# Retail Intelligence: Dynamic Pricing & Inventory Optimization Platform

## Project Overview

This project is a retail data engineering and analytics platform designed to improve inventory visibility and support pricing decisions using retail transactional data.

The system processes retail sales data, cleans and stores it in a structured SQL database, then generates analytical insights about product demand, inventory status, and pricing opportunities.

The goal is to help retail managers monitor product performance, detect stock risks, and support better operational decisions.

---

## Dataset

Source: Kaggle Retail Sales Dataset

Main tables:

* Customers
* Products
* Stores
* Transactions

The dataset contains transactional retail data including product sales, customer information, store locations, and purchase records.

---

## Key Features

### Sales Trend Analysis

Analyze daily and monthly sales trends to identify top-performing products and categories.

### Inventory Monitoring

Estimate stock levels using sales volume and initial stock assumptions.

### Low Stock Alerts

Generate alerts when product inventory falls below threshold levels.

### Rule-Based Price Recommendation

Suggest pricing adjustments based on sales velocity and inventory levels.

### Dashboard Visualization

Provide an interactive dashboard for monitoring KPIs and operational insights.

### Forecasting (Extension)

Predict short-term demand using moving averages or Prophet.

---

## Technologies Used

* Python 3.x
* Pandas & NumPy
* SQL (MySQL / PostgreSQL / SQLite)
* Power BI or Streamlit
* Git & GitHub

Optional:

* Prophet
* Telegram Bot API

---

## System Architecture

Raw Data
↓
Cleaning & Transformation
↓
SQL Database
↓
Analysis Engine
↓
Dashboard
↓
Alerts

---

## Team Roles

* Nada Gamal – Project Coordination, Alerts & Monitoring
* Habiba Qawi – Database Design & SQL
* Habiba Kamal – Data Cleaning & ETL
* Seif Mahmoud – Data Processing & Analysis
* Mohamed Mahmoud – Dashboard Development
* Malak Hassan – Documentation & Presentation

---



## Setup

Install required libraries:

pip install pandas numpy openpyxl matplotlib

---      

## Future Enhancements

* Real-time alerts
* Predictive demand forecasting
* Automated pricing simulation
