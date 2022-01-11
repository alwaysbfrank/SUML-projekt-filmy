from flask import Flask, render_template, request
from pypmml import Model

app = Flask(__name__)

genres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Foreign',
          'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'Thriller', 'War', 'Western']
countries = ['Argentina', 'Australia', 'Austria', 'Bahamas', 'Belgium', 'Botswana', 'Brazil', 'Canada', 'China',
             'Costa Rica', 'Czech Republic', 'Denmark', 'Finland', 'France', 'Germany', 'Greece', 'Hong Kong',
             'Hungary', 'Iceland', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Luxembourg', 'Malta', 'Mexico',
             'Morocco', 'Netherlands', 'New Zealand', 'Norway', 'Pakistan', 'Peru', 'Philippines', 'Poland', 'Portugal',
             'Romania', 'Russia', 'Serbia', 'Singapore', 'South Africa', 'South Korea', 'Spain', 'Sweden',
             'Switzerland', 'Taiwan', 'Thailand', 'United Kingdom', 'United States of America']


@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return render_template('index.html', genres=genres, countries=countries)


@app.route('/', methods=['POST'])
def post():
    data = request.form
    modelRequest = prepareRequest(data)
    audienceRatingModel = Model.fromFile('predict-audience_rating.pmml')
    audienceRatingPrediction = audienceRatingModel.predict(modelRequest)
    return render_template('index.html')


def prepareRequest(data):
    filmBudget = float(data['budget'])
    filmYear = float(data['year'])
    filmGenre = data['genre']
    filmCountry = data['country']
    filmRuntime = float(data['runtime'])
    filmProduction = data['production']
    filmRating = data['rating']
    result = {}
    for country in countries:
        result['production' + country] = "1" if filmCountry == country else "0"
    for genre in genres:
        result['movies_' + genre] = "true" if genre == filmGenre else "false"
    result['content_rating'] = filmRating
    result['production_company'] = filmProduction
    result['imdb_startYear'] = filmYear
    result['movies_budget'] = filmBudget
    result['movies_runtime'] = filmRuntime
    return result


if __name__ == '__main__':
    app.run()
