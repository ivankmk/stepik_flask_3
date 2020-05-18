from flask import Flask, render_template, abort
import itertools
import json
from references import goals, days

app = Flask(__name__)


@app.route('/')
def index():
    all_profiles = json.load(open('data.json'))
    return render_template('index.html', 
                            all_profiles=all_profiles,
                            goals=goals)


@app.route('/profile/<int:id>')
def profile(id):
    data_file = json.load(open('data.json'))
    try:
        profile_data = [profile for profile in data_file if profile['id'] == id][0]
    except IndexError:
        abort(404)

    return render_template('profile.html', 
                            profile_data=profile_data, 
                            goals=goals, 
                            days=days)

if __name__ == '__main__':
    app.run()
