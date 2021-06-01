from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from web.config.config import config_by_name

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # 블루프린트
    from web.domain import main_controller
    from web.domain.question.controller import question_controller
    app.register_blueprint(main_controller.bp)
    app.register_blueprint(question_controller.bp)

    # 필터
    from web.common.filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app