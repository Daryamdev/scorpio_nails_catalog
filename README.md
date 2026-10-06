# 🦂 Scorpio Nails Catalog

A clean, responsive product catalog Django web application built for the Scorpio Nails brand. Features custom grid-based CSS layout, modular Django views, and automated unit testing.

## 🚀 Features

- **Product & Category Management**: Dynamic filtering for gels, top coats, base coats, and gel polishes.
- **Responsive Layout**: Custom CSS Grid structure with modern UI design.
- **Automated Server Launch**: Auto-opens the browser on running `runserver`.
- **Testing Suite**: Full unit tests for Django models and views using `pytest` and `pytest-django`.
- **CI/CD Pipeline**: GitHub Actions workflow that automatically runs pytest on push/pull requests.

## 🛠️ Tech Stack

- **Backend**: Python 3.13, Django 5.x
- **Testing**: `pytest`, `pytest-django`
- **Database**: SQLite3
- **CI/CD**: GitHub Actions


## 📦 Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/scorpio_nails_catalog.git](https://github.com/daryamdev/scorpio_nails_catalog.git)

   cd scorpio_nails_catalog
   ```

2. **Create and activate virtual environment**
```bash 
python -m venv enviroment
# on Windows
enviroment/Scripts/activate
#on Mac
source enviroment/bin/activate
```
3. **Install Dependencies**
```bash
pip install requirements.txt
```
4.**Apply migrations**
```bash 
python manage.py migrate
```
5. **Run the development server**
```bash
python manage.py runserver 
```
**Running Tests** 
```bash
pytest
```



