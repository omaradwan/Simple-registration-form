from flask import Blueprint,render_template,request,flash
from flask_login import login_required, current_user
from .models import Note
from .import db
views=Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
@login_required
def hello():
    if request.method =='POST':
        note=request.form.get('note')
        if len(note)<1:
            flash('You cannot submit an empty note', category='error')
        else:
            new_note=Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added successfully", category='success')

    return render_template("home.html",user=current_user)
