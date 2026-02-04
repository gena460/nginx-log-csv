# 🧾 Nginx Log to CSV Converter

A lightweight and portable tool to **parse Nginx access logs**, convert them into **CSV format**, and optionally **auto-commit the results to a Git repository**. Perfect for analytics, debugging, and integrations with data tools 📊.

---

## ✨ Description

This project reads standard **Nginx access logs**, extracts key request fields, and exports them into a clean **CSV file**.  
You can filter, sort, and version your log exports with Git — all with a simple CLI or Docker container.

---

## 🚀 Features

- 🔍 Parse Nginx access logs into structured fields:
  - IP address
  - Datetime
  - HTTP method
  - URL
  - Protocol
  - Status code
  - Response size
  - Referer
  - User agent
- 📄 Export logs to **CSV** for analytics or data pipelines
- 🎯 Optional filtering:
  - By IP address
  - By HTTP status code
- ⏱ Sort results by datetime
- 🧠 Automatically commit generated CSV files to Git
- 🐳 **Docker support** for easy, portable execution

---

## 📦 Output CSV Format

The generated CSV contains the following columns:

