# predict.py
import pickle
import numpy as np

# Load trained artifacts
popular_df = pickle.load(open("popular.pkl", "rb"))
pt = pickle.load(open("pt.pkl", "rb"))
books = pickle.load(open("books.pkl", "rb"))
similarity_scores = pickle.load(open("similarity_scores.pkl", "rb"))

def recommend_books(book_name, top_n=5):
    """
    Recommend similar books based on cosine similarity
    """
    if book_name not in pt.index:
        return []

    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:top_n+1]

    recommendations = []

    for i in similar_items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        recommendations.append({
            "title": temp_df.iloc[0]['Book-Title'],
            "author": temp_df.iloc[0]['Book-Author'],
            "image": temp_df.iloc[0]['Image-URL-M']
        })

    return recommendations


if __name__ == "__main__":
    # CLI testing
    results = recommend_books("Harry Potter and the Sorcerer's Stone")
    for r in results:
        print(r)
