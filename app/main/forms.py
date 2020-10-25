from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField,SelectField
from wtforms.validators import DataRequired

class CommentsForms(FlaskForm):
    comment= TextAreaField('Comment',validators=DataRequired())
    vote=RadioField('default arguments',choices=[('1','UpVote'),('1''DownVote')])
    submit=SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about you',validators=DataRequired())
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category_id = SelectField('Select category',choices=[('1','Interview'),('1','Interview'),('1','Promotion'),('1','Product'),('1','Pick Up lines')])
    content = TextAreaField('Your pitch')
    submit =SubmitField('Create your pitch')