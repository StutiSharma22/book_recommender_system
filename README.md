# 📚 Book Recommender System

This project recommends books based on **collaborative filtering**, providing personalized book suggestions for users.

---
<img width="1551" height="937" alt="1" src="https://github.com/user-attachments/assets/4f93f382-60df-4618-b377-d786db6cd87a" />
<img width="1512" height="431" alt="2" src="https://github.com/user-attachments/assets/a825d75a-dcd5-44dc-b1dd-d8337dc602ac" />



## Problem Description

With millions of books available online, users often struggle to find books that match their taste and preferences. Traditional search methods—based on book titles or categories—are limited and cannot provide personalized recommendations.  

A **Book Recommender System** solves this problem by analyzing user behavior and book characteristics to suggest books that the user is likely to enjoy. It leverages historical ratings, user interactions, and content information to recommend books that align with individual preferences.

---

## Objective

The primary objective of this project is to build an intelligent system that recommends books to users based on their past interactions and the similarity between books. Specifically, the system aims to:

- Identify popular books and top-rated books to highlight on the platform.  
- Provide personalized recommendations for a given book using collaborative filtering.  
- Enhance the user experience by suggesting books that users are more likely to enjoy, increasing engagement and retention.  
- Deliver recommendations in a fast and scalable way suitable for integration into a web application.

---

## Key Challenges

Building a book recommender system involves several challenges:

- **Data Sparsity:** Most users rate only a small fraction of books, leading to a sparse user-item matrix, which makes it difficult to find meaningful patterns.  
- **Cold Start Problem:** For new users or new books with no ratings, the system lacks sufficient information to make recommendations.  
- **Scalability:** With large datasets (hundreds of thousands of books and millions of ratings), the system must provide recommendations quickly.  
- **Imbalanced Data:** Some books are rated by many users, while others have very few ratings, which can bias recommendations toward popular books.  
- **Evaluation of Recommendations:** Measuring the quality of recommendations is not straightforward.  
- **Integration with Web Application:** Recommendations must be efficiently served in real-time for a user-friendly experience.

---

## Solution

This app provides a **personalized, data-driven, and user-friendly solution** by:

- Highlighting **popular and top-rated books**.  
- Providing **similar book recommendations** based on collaborative filtering.  
- Using a **Flask web interface** with book images, ratings, and author details.  
- Being **Dockerized** for easy deployment on platforms like Render.  

**Link to live application:** [Book Recommender System](https://book-recommender-system-labm.onrender.com)

---

## Dataset

The system uses the **Book-Crossing dataset** from Kaggle:  
**Link:** [Kaggle Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

### 1. Books Dataset (`Books.csv`)
Contains metadata about books.

| Column Name           | Description |
|----------------------|-------------|
| `ISBN`               | Unique identifier for each book |
| `Book-Title`         | Title of the book |
| `Book-Author`        | Author of the book |
| `Year-Of-Publication`| Year the book was published |
| `Publisher`          | Publisher of the book |
| `Image-URL-S`        | Small cover image URL |
| `Image-URL-M`        | Medium cover image URL (used in the app) |
| `Image-URL-L`        | Large cover image URL |

---

### 2. Ratings Dataset (`Ratings.csv`)
Contains user ratings for books.

| Column Name   | Description |
|---------------|-------------|
| `User-ID`     | Unique identifier for each user |
| `ISBN`        | Book identifier (links to `Books.csv`) |
| `Book-Rating` | Rating given by the user (usually 0–10) |

---

### 3. Users Dataset (`Users.csv`)
Contains information about users.

| Column Name | Description |
|------------|-------------|
| `User-ID`  | Unique identifier for each user |
| `Location` | User’s location (city, state, country) |
| `Age`      | Age of the user (may contain missing/unrealistic values) |

---

## Project Structure
```text
book_recommender_system/
├── app.py # Main Flask application
├── train.py # Script to generate .pkl files from raw CSVs
├── predict.py # Optional script for predicting recommendations
├── requirements.txt # Python dependencies
├── Dockerfile # Docker setup for deployment
├── README.md # Project description and instructions
├── notebooks/ # Jupyter notebooks for EDA and analysis
│ └── notebook.ipynb
├── templates/ # HTML templates for Flask
│ ├── index.html
│ └── recommend.html
├── data/ # Raw datasets
│ ├── Books.csv
│ ├── Ratings.csv
│ └── Users.csv
├── models/ # Precomputed pickled files
│ ├── popular.pkl
│ ├── pt.pkl
│ ├── books.pkl
│ └── similarity_scores.pkl
```

---

## Requirements

- flask==2.3.7
- gunicorn==21.2.0
- numpy==1.26.3
- pandas==2.1.1
- scikit-learn==1.3.1
- matplotlib==3.8.1
- seaborn==0.12.3

---

## Running the App Locally

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd book_recommender_system
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Flask app**
```bash
python app.py
```

5. **Access the app**
Open your browser: http://127.0.0.1:5000/

6. **Running with Docker**
- Build the Docker image
```bash
docker build -t book_recommender_system .
```
- Run the Docker container
```bash
docker run -p 5000:5000 -e PORT=5000 book_recommender_system
```
7. Access the app
Open your browser: http://localhost:5000/
