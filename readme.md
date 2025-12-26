# Pulsegen Review Scraper

## Overview

This project is developed as part of the Pulsegen coding assignment.
It is a Python-based command-line tool that scrapes product reviews
from SaaS review platforms based on user inputs and outputs the data
in a structured JSON format.

The script is designed to handle real-world scraping limitations
gracefully while maintaining a clean, extensible, and professional
code structure.

---

## Supported Review Sources

- **G2**
- **Capterra**
- **TrustRadius** _(Bonus – SaaS-focused review platform)_

---

## Features

- Command-line interface using argparse
- Accepts company name, start date, end date, and source as inputs
- Attempts real HTTP-based scraping using `requests`
- Parses HTML responses using `BeautifulSoup`
- Graceful error handling for blocked or failed requests
- Fallback sample data to demonstrate complete workflow
- Uniform functionality across all supported sources
- Clean, modular, and maintainable code structure

---

## Project Structure

review-scraper/
│
├── scraper/
│ ├── init.py
│ ├── g2_scraper.py
│ ├── capterra_scraper.py
│ ├── trustradius_scraper.py
│ └── utils.py
│
├── output/
│ └── reviews.json
│
├── main.py
├── requirements.txt
└── README.md

---

## Installation & Setup

### Prerequisites

- Python 3.8 or above
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt


How to Run the Script
G2 Reviews
 python main.py --company Zoho --source g2 --start 2024-01-01 --end 2024-06-30

Capterra Reviews
python main.py --company Zoho --source capterra --start 2024-01-01 --end 2024-06-30

TrustRadius Reviews (Bonus Source)
python main.py --company Zoho --source trustradius --start 2024-01-01 --end 2024-06-30

```
