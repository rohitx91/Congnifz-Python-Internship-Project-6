# Congnifz-Python-Internship-Project-6
Level 3 Task 1: Web Scraper for Cognifyz Python Internship.

📌 Project Overview

This project demonstrates how to extract structured data from a website using Python’s web-scraping libraries.
The scraper fetches quotes and authors from a sample website (quotes.toscrape.com) and prints them in a clean, readable format.

📍This task improves understanding of:
- Working with HTML pages
- Parsing data using BeautifulSoup
- Sending HTTP requests
- Extracting specific information from websites

🎯 Objectives
- Understand the basics of web scraping
- Learn to send HTTP requests using requests
- Parse HTML content using BeautifulSoup
- Extract selected data (quotes + authors)
- Display structured data in console

🧰 Tools & Libraries Used
Tool / Library	Purpose
- 🐍 Python 3.x	Main programming language
- 🌐 requests	Fetching website HTML content
- 🍜 BeautifulSoup (bs4)	Parsing & extracting data from HTML
- 🖥️ VS Code / IDE	Writing & running Python scripts
- 🌐 quotes.toscrape.com	Free website for scraping practice

🧠 How the Scraper Works
- Sends a GET request to the website
- Downloads the HTML content
- BeautifulSoup parses the HTML
- Extracts:
    - Text of each quote
    - Name of the author
- Prints output line-by-line
