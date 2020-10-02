from flask import Blueprint, render_template


error_bp = Blueprint('errors_bp',__name__)

@error_bp.app_errorhandler(404)
def handle_404(e):
    """ 404 not found """

    return render_template('error.html',error=404),404

@error_bp.app_errorhandler(403)
def handle_403(error_code):
    """ 403 forbidden """

    return render_template('error.html',error=403), 403

@error_bp.app_errorhandler(410)
def handle_410(error_code):
    """ 410 gone """

    return render_template('error.html',error=410), 410

@error_bp.app_errorhandler(500)
def handle_500(error_code):
    """ 500 Internal Server error """

    return render_template('error.html',error=500), 410
