from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    role = SelectField("Role", choices=[("admin", "Admin"), ("staff", "Staff")], validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")

class ItemForm(FlaskForm):
    name = StringField("Item Name", validators=[DataRequired()])
    category = StringField("Category")
    description = StringField("Description")
    quantity = IntegerField("Quantity", validators=[DataRequired()])
    price = DecimalField("Price", places=2, validators=[DataRequired()])
    supplier = StringField("Supplier")

    submit = SubmitField("Save Item")
    

class SaleForm(FlaskForm):
    item = SelectField("Item", coerce=int, validators=[DataRequired()])
    quantity = IntegerField("Quantity", validators=[DataRequired()])
    submit = SubmitField("Record Sale")

