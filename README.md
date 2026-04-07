# 🍕 Pizza Sales Analytics

## 📌 Project Overview

This project analyzes pizza sales data to uncover revenue trends, customer ordering patterns, and product performance. The goal is to provide actionable insights for inventory planning, promotional strategies, and menu optimization.

## 🛠️ Tools Used

- **MySQL** – Data extraction, aggregation, and KPI calculation  
- **Power BI** – Interactive dashboard with DAX measures  
- **Excel** – Initial data inspection and validation  

## 📊 Dataset

- **Records:** 48,000+ pizza orders  
- **Fields:** order date, order time, pizza name, pizza category, pizza size, quantity, unit price, total price  

## 🔍 Key SQL Queries

Examples of queries written for this analysis:

### 1. Total Revenue
```sql
SELECT ROUND(SUM(total_price), 2) AS total_revenue FROM pizza_sales;
```

### 2. Top 5 Best-Selling Pizzas by Revenue
```sql
SELECT pizza_name, ROUND(SUM(total_price), 2) AS total_revenue
FROM pizza_sales
GROUP BY pizza_name
ORDER BY total_revenue DESC
LIMIT 5;
```

### 3. Peak Order Hours
```sql
SELECT HOUR(order_time) AS order_hour, COUNT(order_id) AS order_count
FROM pizza_sales
GROUP BY HOUR(order_time)
ORDER BY order_count DESC;
```
