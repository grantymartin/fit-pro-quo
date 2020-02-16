import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = 'fitness_tracker'

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/fit_track')
def fit_track():
    action_trackers=mongo.db.action_tracker.find().sort("date", -1)
    return render_template("fittrack.html", action_tracker= action_trackers )
    
@app.route('/addexercise')
def addexercise():
    return render_template('addexercise.html', action=mongo.db.action.find())

@app.route('/insert_exercise', methods=['POST'])
def insert_exercise():
    action_tracker = mongo.db.action_tracker
    action_tracker.insert_one(request.form.to_dict())
    return redirect(url_for('fit_track'))
    
@app.route('/edit_action/<action_id>')
def edit_action(action_id):
    the_action = mongo.db.action_tracker.find_one({"_id":ObjectId(action_id)})
    sport = mongo.db.action.find()
    return render_template('editaction.html', action_tracker=the_action, action=sport)
    
@app.route('/update_action/<action_id>', methods=["POST"])
def update_action(action_id):
    action_tracker = mongo.db.action_tracker
    action_tracker.update( {'_id': ObjectId(action_id)},
    {
        'session_name':request.form.get('session_name'),
        'action_name':request.form.get('action_name'),
        'action_description': request.form.get('action_description'),
        'planned_fatigue': request.form.get('planned_fatigue'),
        'date':request.form.get('date'),
        'actual_fatigue': request.form.get('actual_fatigue'),
        'feedback': request.form.get('feedback')
    })
    return redirect(url_for('fit_track'))
    
@app.route('/delete_action/<action_id>')
def delete_action(action_id):
    mongo.db.action_tracker.remove({'_id': ObjectId(action_id)})
    return redirect(url_for('fit_track'))

@app.route('/sports')
def sports():
    action=mongo.db.action.find()
    action_trackers=mongo.db.action_tracker.find()
    return render_template("sports.html", actions=action, action_tracker=action_trackers )
    
@app.route('/addsport')
def addsport():
    return render_template('addsport.html', action=mongo.db.action.find())

@app.route('/insert_sport', methods=['POST'])
def insert_sport():
    action_doc = {'action_name': request.form.get('action_name')}
    mongo.db.action.insert_one(action_doc)
    return redirect(url_for('sports'))
    
@app.route('/delete_sport/<act_id>')
def delete_sport(act_id):
    mongo.db.action.remove({'_id':ObjectId(act_id)})
    return redirect(url_for('sports'))
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)