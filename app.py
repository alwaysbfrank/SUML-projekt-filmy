from flask import Flask, render_template, request

app = Flask(__name__)

genres = ['Animation', 'Comedy', 'Family', 'Adventure', 'Fantasy', 'Romance', 'Drama', 'Action', 'Crime', 'Thriller',
          'Horror', 'History', 'Science Fiction', 'Mystery', 'War', 'Foreign', 'Music', 'Documentary', 'Western', 'TV Movie']
countries = ['USA', 'UK', 'France', 'Germany', 'Italy', 'Spain', 'Australia', 'Canada', 'Japan', 'Hong Kong', 'Russia',
             'Austria', 'Switzerland', 'New Zealand', 'Mexico', 'Taiwan', 'Peru', 'Liechtenstein', 'Ireland', 'Finland',
             'India', 'Hungary', 'Brazil', 'China', 'Denmark', 'Iran', 'South Africa', 'Botswana', 'Israel', 'Netherlands',
             'Iceland', 'Ecuador', 'Luxembourg', 'Bahamas', 'Portugal', 'Sweden', 'Serbia', 'Argentina', 'Norway',
             'Czech Republic', 'Pakistan', 'Thailand', 'Namibia', 'Philippines', 'Belgium', 'South Korea', 'Poland',
             'Greece', 'Romania', 'Morocco', 'Malta', 'Singapore', 'Costa Rica', 'Algeria']
@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return render_template('index.html', genres=genres, countries=countries)

@app.route('/', methods=['POST'])
def post():
    data = request.form
    budget = data['budget']
    year = data['year']
    genre = data['genre']
    country = data['country']
    runtime = data['runtime']
    production = data['production']
    rating = data['rating']
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

