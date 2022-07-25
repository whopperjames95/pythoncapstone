from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from website.models import Note, Travel, Bucket, User
from website import login_manager
from website import database
import json



views = Blueprint('views', __name__)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# landing pages
@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', user=current_user)






# this was originaly the home function 
@views.route('/personal_goals', methods=['GET', 'POST'])
@login_required
def personalGoals():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Goal is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            database.session.add(new_note)
            database.session.commit()
            flash('Goal added!', category='success')


    return render_template("personal_goals.html", user=current_user)


@views.route('/bucket_list', methods=['GET', 'POST'])
@login_required
def bucket():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Activity is Too Short!', category='error')
        else:
            new_note = Bucket(data=note, user_id=current_user.id)
            database.session.add(new_note)
            database.session.commit()
            flash('Activity Added!', category='success')


    return render_template("bucket_list.html", user=current_user)


@views.route('/travel', methods=['GET', 'POST'])
@login_required
def travel():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Travel Plan is Too Short!', category='error')
        else:
            new_note = Travel(data=note, user_id=current_user.id)
            database.session.add(new_note)
            database.session.commit()
            flash('Travel Plan Added!', category='success')


    return render_template("travel.html", user=current_user)




@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            database.session.delete(note)
            database.session.commit()
    
    return jsonify({})
    # return redirect(url_for('home'))





@views.route('/delete-travel', methods=['POST'])
def delete_travel():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Travel.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            database.session.delete(note)
            database.session.commit()
    
    return jsonify({})
    # return redirect(url_for('travel'))

@views.route('/delete-bucket', methods=['POST'])
def delete_bucket():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Bucket.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            database.session.delete(note)
            database.session.commit()
    
    return jsonify({})
    # return redirect(url_for('bucket'))





