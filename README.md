# Libgen Scrapper 

## Table of Contents

- [Project Description](#Project-Description)
- [Features](#Features)
- [Technology Stack](#Technology-Stack)
- [Project Structure](#Project-Structure)
- [Installation](#Installation)



## Project Description
  The Django Celery Libgen Scraper is a project aimed at providing a convenient way to scrape book information 
  and files from the Libgen.is website. It utilizes Django, Celery, and BeautifulSoup to scrape data and store it in a Django database asynchronously.
## Features
- Allows users to enter a search phrase to scrape books related to that phrase from Libgen.is.
- Scrapes book information such as title, author, publisher, publication year, and more.
- Downloads book files and images associated with the scraped books.
- Stores scraped book information in a Django database for later reference.
- Supports asynchronous processing using Celery for efficient scraping and database operations.
- Provides flexibility for customizing the scraping process and data storage.

### Technology Stack

- **Backend Framework:** Django
- **Task Queue:** Celery
- **Database:** Django ORM
- **Web Scraping:** BeautifulSoup, Requests
- **Export Formats:** CSV, XLS, JSON

### Project Structure
- **LibgenScrapper/**
  - `manage.py`: Django management script.
  - **blog/**
    - `models.py`: Defines Django models for the database.
    - `tasks.py`: Contains Celery tasks for web scraping.
    - `views.py`: Implements views for handling web requests.
    - `urls.py`: Configures URL patterns.
    - `templates/`: HTML templates.
  

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MadnessCod/techcrunch_scrapper.git
   cd LibgenScrapper

## OR

1. **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    pip install -r requirements.txt
   
2. **Apply migrations and start the development server:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
3. **Start Redis**
    - Head to https://github.com/tporadowski/redis/releases

4. **Start Celery worker for background tasks:**
    ```bash
    celery -A LibgenScrapper worker --loglevel=info
    ```
   If you encounter issues with tasks becoming stuck or 
unresponsive in Celery, you can take the following action:
    
    ```bash
   celery -A LibgenScrapper worker --loglevel=info -P eventlet
   ```
   remember to install eventlet
    ```bash
   pip install eventlet
    ```
   if you want to monitor celery tasks
   1. **Install flower**
        ```bash
      pip install flower
      ```
   2. **In a different Terminal use flower**
        ```bash
      celery -A libgenScrapper flower
      ```
   3. **Head to http://localhost:5555/**
   
5. **Start Django server**
    ```bash
   python manage.py runserver

### Usage
- Access the web application at http://127.0.0.1:8000/.
- Navigate to the search page (http://127.0.0.1:8000/blog/scrape-and-display/) 
and input search queries to retrieve relevant information.

### Contribution Guidelines
1. **Fork the repository.**
2. **Create a new branch for your feature or bug fix.**
3. **Make changes and submit a pull request.**