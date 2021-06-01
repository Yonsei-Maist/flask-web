from datetime import datetime

from web import db
from web.domain.question.model.question_model import Question
from web.domain.question.dao.question_dao import QuestionDao

question_dao = QuestionDao()


class QuestionService:

    def question_list(self, request):
        page = request.args.get('page', type=int, default=1)
        question_list = Question.query.order_by(Question.create_date.desc())
        question_list = question_list.paginate(page, per_page=10)
        return question_list

    def question(self, question_id):
        question = Question.query.get(question_id)
        return question

    # SQLAlchemy 사용
    def create(self, form):
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()

    # MySQL-Connector 사용
    #def create(self, payload):
    #    question_dao.create(payload)