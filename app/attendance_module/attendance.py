from flask import Flask, render_template_string
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, StringField, SubmitField, SelectField, DateField
from wtforms.validators import InputRequired
import flask_login

attendancebp = Blueprint('attendance', __name__)

#single attendance entry
class HourForm(FlaskForm):
    tutorname = StringField('Name')
    hours = SelectField('Hours', choices = [(0, 0), (0.5, 0.5), (1, 1), (1.5, 1.5), (2, 2)])  #value label pairs

class AttendanceForm(FlaskForm):
    name = StringField('Overseer Name', validators=[InputRequired()])
    date = DateField('Today\'s Date:', validators = [InputRequired()])
    add_entry = SubmitField('Add Entry')
    delete_entry = SubmitField('Delete Entry')
    entries = FieldList(FormField(HourForm), min_entries=1)
    submit = SubmitField('Save')



@attendancebp.route('/attendance', methods=['GET', 'POST'])
@flask_login.login_required
def attendance():
    form = AttendanceForm()

    if form.add_entry.data:  #if submitted via add entry
      form.entries.append_entry(None)
    elif form.delete_entry.data:
        form.entries.pop_entry()
    elif form.validate_on_submit():
        #for entry in form.entries.data:
        #    print(entry)
        print(form.entries.data)
    return render_template("attendance.html" ,form=form)