from wtforms import StringField, IntegerField, Form
from wtforms.validators import Length, NumberRange


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=99)])
    f = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
    # page = IntegerField(default=1)

    # def validate_page(self,field):
    #     number = field.isdigital
