from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator

from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION

# To keep things clean, we keep our Flask-Nav instance in here. We will define
# frontend-specific navbars in the respective frontend, but it is also possible
# to put share navigational items in here.

nav = Nav()

# Menu / navbar
nav.register_element('frontend_top', Navbar(
    View('Home', 'frontend.index'),
   Subgroup(
       'Python',
       Link('Beginners Guide', 'https://wiki.python.org/moin/BeginnersGuide/'),
       Link('Awesome Python', 'https://github.com/vinta/awesome-python'),
       Link('WSGI', 'https://www.python.org/dev/peps/pep-3333/'),
       Link('v3.6 Docs', 'https://docs.python.org/3/'),
       Link('PyVideo', 'http://pyvideo.org/'),
    ),
    Subgroup(
        'Flask',
        Link('Discover Flask', 'https://github.com/realpython/discover-flask'),
        Link('Flask-Bootstrap', 'http://pythonhosted.org/Flask-Bootstrap'),
        Link('Flask-Debug', 'https://github.com/mbr/flask-debug'),
        Link('Flask-DebugToolbar', 'https://flask-debugtoolbar.readthedocs.io'),
    ),
    Subgroup(
       'Bootstrap',
       Link('Getting started', 'http://getbootstrap.com/getting-started/'),
       Link('CSS', 'http://getbootstrap.com/css/'),
       Link('Components', 'http://getbootstrap.com/components/'),
       Link('Javascript', 'http://getbootstrap.com/javascript/'),
       Link('Customize', 'http://getbootstrap.com/customize/'), ),
    Text('Using Flask-Bootstrap {}'.format(FLASK_BOOTSTRAP_VERSION)), ))
