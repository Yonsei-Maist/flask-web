from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm): # FlaskForm 상속
    subject = StringField('제목', validators=[DataRequired('제목은 필수 입력 항목입니다.')]) # 폼 라벨, 필드값 검증
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목입니다.')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목입니다.')])