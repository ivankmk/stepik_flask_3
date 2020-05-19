from flask import Flask, render_template, abort
import itertools
import json

app = Flask(__name__)
GOALS = {"travel": "⛱ Для путешествий", 
         "study": "🏫 Для учебы", 
         "work": "🏢 Для работы", 
         "relocate": "🚜 Для переезда"}

DAYS = {"mon": "Понедельник", 
        "tue": "Вторник", 
        "wed": "Среда", 
        "thu": "Четверг", 
        "fri": "Пятница", 
        "sat": "Суббота", 
        "sun": "Воскресенье"}

@app.route('/')
def index():
    all_profiles = json.load(open('data.json'))
    return render_template('index.html', 
                            all_profiles=all_profiles,
                            goals=GOALS)


@app.route('/request')
def request():

    return render_template('request.html')


@app.route('/goals/<goal>')
def goals(goal):
    all_profiles = json.load(open('data.json'))
    try:
        profiles_data = [profile for profile in all_profiles if goal in profile['goals']]
    except IndexError:
        abort(404)
    return render_template('goal.html', 
                            profiles_data=profiles_data,
                            goal=GOALS[goal])



@app.route('/profile/<int:id>')
def profile(id):
    all_profiles = json.load(open('data.json'))
    try:
        profile_data = [profile for profile in all_profiles if profile['id'] == id][0]
    except IndexError:
        abort(404)

    return render_template('profile.html', 
                            profile_data=profile_data, 
                            goals=goals, 
                            days=DAYS)

if __name__ == '__main__':
    app.run()
