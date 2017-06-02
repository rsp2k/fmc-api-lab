from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired, IPAddress, NumberRange

class PinholeRequestForm(FlaskForm):
    ip = StringField(u'Destination address', validators=[DataRequired(), IPAddress(message="Enter a valid IP")])
    port = IntegerField(u'Destination Port', validators=[DataRequired(), NumberRange(min=1024,max=65536)])
    lifetime = IntegerField(u'Lifetime (in seconds)', validators=[DataRequired(), NumberRange(min=300,max=3600)

    submit = SubmitField(u'Create Pinhole')
