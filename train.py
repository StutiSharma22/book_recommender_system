# train.py
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def train_model():
    books = pd.read_csv("data/Books.csv", low_memory=False)
    ratings = pd.read_csv("data/Ratings.csv")

    # Merge
    df = ratings.merge(books, on="ISBN")

    # ---- FILTER USERS ----
    user_counts = df.groupby('User-ID').count()['Book-Rating']
    active_users = user_counts[user_counts >= 200].index

    # ---- FILTER BOOKS ----
    book_counts = df.groupby('Book-Title').count()['Book-Rating']
    popular_books = book_counts[book_counts >= 50].index

    df = df[
        (df['User-ID'].isin(active_users)) &
        (df['Book-Title'].isin(popular_books))
    ]

    # ---- PIVOT TABLE ----
    pt = df.pivot_table(
        index='Book-Title',
        columns='User-ID',
        values='Book-Rating'
    )

    pt.fillna(0, inplace=True)

    # ---- COSINE SIMILARITY ----
    similarity_scores = cosine_similarity(pt)

    # ---- POPULAR BOOKS DF ----
    popular_df = (
        df.groupby('Book-Title')
        .agg(
            Num_ratings=('Book-Rating', 'count'),
            Avg_rating=('Book-Rating', 'mean')
        )
        .reset_index()
    )

    popular_df = popular_df.merge(
        books[['Book-Title', 'Book-Author', 'Image-URL-M']],
        on='Book-Title'
    ).drop_duplicates('Book-Title')

    # ---- SAVE FILES ----
    pickle.dump(popular_df, open("popular.pkl", "wb"))
    pickle.dump(pt, open("pt.pkl", "wb"))
    pickle.dump(books, open("books.pkl", "wb"))
    pickle.dump(similarity_scores, open("similarity_scores.pkl", "wb"))

    print("✅ Training completed successfully")

if __name__ == "__main__":
    train_model()
