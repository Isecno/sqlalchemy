from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField('Job Title', validators=[DataRequired()])
    leader = StringField('Team Leader id', validators=[DataRequired()])
    work_size = StringField('Work size')
    collaborators = StringField("Collaborators", validators=[DataRequired()])
    is_finish = StringField("Is job finished?")
    submit = SubmitField('add')
