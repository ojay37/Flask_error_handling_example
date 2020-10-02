from flask import abort, Blueprint, render_template


routes_bp = Blueprint('routes_bp',__name__)

@routes_bp.route('/',methods=["GET"])
def homepage():
    return render_template('homepage.html')

@routes_bp.route('/test_404', methods=["GET"])
def test_404():
    abort(404)

@routes_bp.route('/test_403', methods=["GET"])
def test_403():
    abort(403)

@routes_bp.route('/test_410', methods=["GET"])
def test_410():
    abort(410)


@routes_bp.route('/test_500', methods=["GET"])
def test_500():
    abort(500)


