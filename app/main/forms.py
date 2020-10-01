from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required, Email, Length


class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    description = TextAreaField('Description', validators=[Required()])
    owners = TextAreaField('Owners/Members', validators=[Required()])
    technologies = TextAreaField('Technologies used', validators=[Required()])
    cohort = SelectField('Select cohort', choices=[('mc1', 'COHORT-1'),('mc2', 'COHORT-2'),
    ('mc3', 'COHORT-3'),('mc4', 'COHORT-4'),('mc5', 'COHORT-5'),('mc6', 'COHORT-6'),
    ('mc7', 'COHORT-7'),('mc8', 'COHORT-8'),('mc9', 'COHORT-9'),('mc10', 'COHORT-10'),
    ('mc11', 'COHORT-11'),('mc12', 'COHORT-12'),('mc13', 'COHORT-13'),('mc14', 'COHORT-14'),
    ('mc15', 'COHORT-15')])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Post Comment', validators=[Required()])
    submit = SubmitField('Submit')