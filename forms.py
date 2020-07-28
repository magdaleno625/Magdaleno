from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length


class SignupForm(FlaskForm):
	name = StringField('User Name', validators=[DataRequired(), Length(min=3, max=50, message="Nombre incorrecto")])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30, message="Contraseña invalida")])
	apellidos = StringField('Apellidos', validators=[DataRequired(), Length(min=10, max=80, message="Apellidos incorrectos")])
	biografia = StringField('Biografia', validators=[DataRequired(), Length(min=20, max=120, message="Descripcion Incorrecta")])
	correo = StringField('Correo', validators=[DataRequired(), Length(min=8, max=30, message="Correo Incorrecto")])
	telefono = StringField('Telefono', validators=[DataRequired(), Length(min=10, max=11, message="Telefono Incorrecto")])
	
	
class LoginForm(FlaskForm):
	name = StringField('User Name', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

class HomeForm(FlaskForm):
	comment = TextAreaField('Comentario', validators=[DataRequired(), Length(min=3, max=250, message="Publicacion Incorrecta")])