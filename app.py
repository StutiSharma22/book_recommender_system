# app.py
from flask import Flask, render_template, request
from predict import recommend_books, popular_df, pt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
         votes=list(popular_df['Num_ratings'].values),  
        rating=list(popular_df['Avg_rating'].values) )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html', book_list=list(pt.index))

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    data = recommend_books(user_input)
    return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    
