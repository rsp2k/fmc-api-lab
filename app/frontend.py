# This contains our frontend; since it is a bit messy to use the @app.route
# decorator style when using application factories, all of our routes are
# inside blueprints. This is the front-facing blueprint.
#
# You can find out more about blueprints at
# http://flask.pocoo.org/docs/blueprints/

from flask import Blueprint, render_template, flash, redirect, url_for, request

from .forms import PinholeRequestForm

frontend = Blueprint('frontend', __name__)

# Simple Homepage
@frontend.route('/')
def index():
    return render_template('index.html')

@frontend.route('/pinhole/', methods=('GET', 'POST'))
def pinhole():
    form = PinholeRequestForm()

    if request.method == 'POST' and form.validate():
        # We don't have anything fancy in our application, so we are just
        # flashing a message when a user completes the form successfully.
        #
        # Note that the default flashed messages rendering allows HTML, so
        # we need to escape things if we input user values:
        flash('Creating your pinhole {}:{}'.format(form.ip.data, form.port.data))

        form.data.clear()

        # In a real application, you may wish to avoid this tedious redirect.
        return redirect(url_for('.index'))

    return render_template('pinhole.html', form=form)
