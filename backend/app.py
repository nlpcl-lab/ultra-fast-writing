import argparse
import methods

from datetime import datetime
from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask_sqlalchemy import SQLAlchemy

parser = argparse.ArgumentParser()
parser.add_argument('--index_path', type=str,
                    default='dist/index.html',)
parser.add_argument('--port', type=int, default=5678)
parser.add_argument('--debug', action='store_true')
parser.add_argument('--init_db', action='store_true')
args = parser.parse_args()


app = Flask(__name__, template_folder='./', static_folder='dist/static')

app.config['SECRET_KEY'] = 'NLPCLNLPCL'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../log.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)


class Log(db.Model):
    __tablename__ = 'log'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(30), nullable=False)
    type = db.Column(db.String(30), nullable=False)
    arg = db.Column(db.String(140), nullable=False)
    subarg = db.Column(db.String(140), nullable=True)

    def __init__(self, type, arg, subarg=None):
        self.time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.type = type
        self.arg = arg
        self.subarg = subarg

    def __repr__(self):
        return '<Log(%d, %s, %s, %s, %s)>' % (args.id, args.time, args.type, args.arg, args.subarg)


class Status(Resource):
    def get(self):
        return {'status': True}


class DeterminerCheck(Resource):
    def get(self):
        try:
            req_parser = reqparse.RequestParser()
            req_parser.add_argument('arg', required=True, type=str)
            req_args = req_parser.parse_args()

            log = Log('DET_CHECK', req_args['arg'])
            db.session.add(log)
            db.session.commit()

            res_count, res_sentence = methods.determiner_check(req_args['arg'])

            return {'count': res_count,
                    'sentence': res_sentence}
        except Exception as e:
            return {'error': str(e)}


class DeterminerCheckCaseByCase(Resource):
    def get(self):
        try:
            req_parser = reqparse.RequestParser()
            req_parser.add_argument('arg', required=True, type=str)
            req_parser.add_argument('subarg', required=True, type=str)
            req_args = req_parser.parse_args()

            log = Log('DET_CHECK_CBC', req_args['arg'], req_args['subarg'])
            db.session.add(log)
            db.session.commit()

            usages = methods.determiner_check_case_by_case(
                req_args['arg'], req_args['subarg'])

            return usages
        except Exception as e:
            return {'error': str(e)}


class CheckWordUsage(Resource):
    def get(self):
        try:
            req_parser = reqparse.RequestParser()
            req_parser.add_argument('arg', required=True, type=str)
            req_args = req_parser.parse_args()

            log = Log('CHECK_WORD_USAGE', req_args['arg'])
            db.session.add(log)
            db.session.commit()

            usage_list = methods.check_word_usage(req_args['arg'])

            return usage_list
        except Exception as e:
            return {'error': str(e)}


class CheckPhraseUsage(Resource):
    def get(self):
        try:
            req_parser = reqparse.RequestParser()
            req_parser.add_argument('arg', required=True, type=str)
            req_args = req_parser.parse_args()

            log = Log('CHECK_PHRASE_USAGE', req_args['arg'])
            db.session.add(log)
            db.session.commit()

            usage_list = methods.check_phrase_usage(req_args['arg'])

            return usage_list
        except Exception as e:
            return {'error': str(e)}


class PrepositionCheck(Resource):
    def get(self):
        try:
            req_parser = reqparse.RequestParser()
            req_parser.add_argument('arg', required=True, type=str)
            req_args = req_parser.parse_args()

            log = Log('CHECK_PHRASE_USAGE', req_args['arg'])
            db.session.add(log)
            db.session.commit()

            res_count, res_sentence = methods.preposition_check(
                req_args['arg'])

            return {'count': res_count,
                    'sentence': res_sentence}
        except Exception as e:
            return {'error': str(e)}


class PrepositionCheckCaseByCase(Resource):
    def get(self):
        try:
            req_parser = reqparse.RequestParser()
            req_parser.add_argument('arg', required=True, type=str)
            req_parser.add_argument('subarg', required=True, type=str)
            req_args = req_parser.parse_args()

            log = Log('DET_CHECK_CBC', req_args['arg'], req_args['subarg'])
            db.session.add(log)
            db.session.commit()

            usages = methods.preposition_check_case_by_case(
                req_args['arg'], req_args['subarg'])

            return usages
        except Exception as e:
            return {'error': str(e)}


class GetLog(Resource):
    def get(self):
        logs = Log.query.all()
        res = [{'id': log.id,
                'time': log.time,
                'type': log.type,
                'arg': log.arg,
                'subarg': log.subarg} for log in logs]
        return res


api.add_resource(Status, '/api')
api.add_resource(DeterminerCheck, '/api/determiner_check')
api.add_resource(DeterminerCheckCaseByCase,
                 '/api/determiner_check_case_by_case')
api.add_resource(CheckWordUsage, '/api/check_word_usage')
api.add_resource(CheckPhraseUsage, '/api/check_phrase_usage')
api.add_resource(PrepositionCheck, '/api/preposition_check')
api.add_resource(PrepositionCheckCaseByCase,
                 '/api/preposition_check_case_by_case')
api.add_resource(GetLog, '/api/log')


@app.route('/')
def index():
    return render_template('dist/index.html')


if __name__ == '__main__':
    if args.init_db:
        db.create_all()
    else:
        app.run('0.0.0.0', debug=args.debug, port=args.port, threaded=True)
