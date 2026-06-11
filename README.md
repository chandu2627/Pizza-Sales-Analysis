# 🍕 Pizza Sales Analytics

> **Interactive Sales Intelligence Dashboard** — An end-to-end analytics project exploring pizza sales trends, customer preferences, and revenue performance using SQL and Power BI.

---

## 📌 Project Overview

This project analyzes 48,000+ pizza orders to uncover revenue trends, customer ordering patterns, and product performance. The goal is to provide actionable insights for inventory planning, promotional strategies, and menu optimization.

---

## 🎯 Problem Statement

Pizza businesses often struggle to identify:
- 📉 Which products drive the most revenue vs which underperform
- ⏰ Peak ordering hours and days for staffing optimization
- 🔄 Customer ordering patterns and preferences by category/size
- 📦 Inventory needs based on historical demand trends

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| ![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white) | Data extraction, aggregation & KPI calculation |
| ![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black) | Interactive dashboard with DAX measures |

---

## 📊 Dataset

| Field | Details |
|-------|---------|
| **Records** | 48,000+ pizza orders |
| **Fields** | order date, order time, pizza name, pizza category, pizza size, quantity, unit price, total price |
| **File** | `pizza_sales.csv` |

---

## 🔑 Key SQL Queries

### 1. Total Revenue
```sql
SELECT ROUND(SUM(total_price), 2) AS total_revenue 
FROM pizza_sales;
```

### 2. Top 5 Best-Selling Pizzas by Revenue
```sql
SELECT pizza_name, 
       ROUND(SUM(total_price), 2) AS total_revenue
FROM pizza_sales
GROUP BY pizza_name
ORDER BY total_revenue DESC
LIMIT 5;
```

### 3. Peak Order Hours
```sql
SELECT HOUR(order_time) AS order_hour, 
       COUNT(order_id) AS order_count
FROM pizza_sales
GROUP BY HOUR(order_time)
ORDER BY order_count DESC;
```

### 4. Revenue by Pizza Category
```sql
SELECT pizza_category,
       ROUND(SUM(total_price), 2) AS total_revenue,
       COUNT(order_id) AS total_orders
FROM pizza_sales
GROUP BY pizza_category
ORDER BY total_revenue DESC;
```

### 5. Average Order Value
```sql
SELECT ROUND(SUM(total_price) / COUNT(DISTINCT order_id), 2) AS avg_order_value
FROM pizza_sales;
```

---

## 💡 Key Insights

- 🏆 **Classic and Supreme** categories generate the highest revenue
- ⏰ **Lunch (12–1 PM) and Evening (6–8 PM)** are peak ordering hours
- 📦 **Large size** pizzas are most ordered across all categories
- 📅 **Fridays** record the highest order volume of the week
- 🔻 **Brie Carre** is the lowest performing pizza by revenue

---

## 📁 Repository Files

| File | Description |
|------|-------------|
| `pizza_sales.csv` | Raw dataset with 48,000+ orders |
| `Pizza_sales.sql` | All SQL queries for KPI analysis |
| `pizza Dashboard.pbix` | Power BI interactive dashboard |
| `pizza.pdf` | Project report/presentation |

---

## 👤 Author

**Chandu Manikanta**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/chandumanikanta)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white)](https://github.com/chandu2627)

---

<p align="center">⭐ If you found this project helpful, please give it a star!</p>
