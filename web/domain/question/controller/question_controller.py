from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from web.common.forms import QuestionForm, AnswerForm
from web.domain.question.service.question_service import QuestionService


bp = Blueprint('question', __name__, url_prefix='/question')
question_service = QuestionService()


class QuestionController:

    @bp.route('/list')
    def question_list(*args):
        question_list = question_service.question_list(request)
        return render_template('question/question_list.html', question_list=question_list)

    @bp.route('/detail/<int:question_id>')
    def detail(*args, question_id):
        form = AnswerForm()
        question = question_service.question(question_id)
        return render_template('question/question_detail.html', question=question, form=form)

    @bp.route('/create', methods=('GET', 'POST'))
    def create(*args):
        form = QuestionForm()
        if request.method == 'POST' and form.validate_on_submit():
            question_service.create(form)
            return redirect(url_for('main.index'))
        return render_template('question/question_form.html', form=form)