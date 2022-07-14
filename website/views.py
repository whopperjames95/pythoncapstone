from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from.models import Note, Travel, Bucket
from .import db
import json



views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Goal is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Goal added!', category='success')


    return render_template("home.html", user=current_user)


@views.route('/bucket_list', methods=['GET', 'POST'])
@login_required
def bucket():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Activity is Too Short!', category='error')
        else:
            new_note = Bucket(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
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
            db.session.add(new_note)
            db.session.commit()
            flash('Travel Plan Added!', category='success')


    return render_template("travel.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})





