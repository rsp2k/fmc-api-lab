# fmc-api-lab

# Prerequisites
- git
- Python 3.6+
- pip

# First Time setup
- Clone this repository (will fail if the destination directory exists)
- Enter newly created repository directory
- Create virtualenv
  * virtualenv venv --python=python3
  - Make sure virtualenv is loaded
  - Mac/Linux
    * source venv/bin/activate
  - Windows
    * venv\Scripts\activate
- Install requirements
  * pip install -r requirements.txt

# Launch
- From a terminal window, change to the directory where the repository was checked out above
- Make sure virtualenv is loaded
  - Mac/Linux
    * source venv/bin/activate
  - Windows
    * venv\Scripts\activate

- Set evironment variables and start flask (CTRL+C to stop)
  - Mac/Linux
    * export FLASK_DEBUG=1; export FLASK_APP=application.py; flask run
  - Windows
    * set FLASK_DEBUG=1
    * set FLASK_APP=application.py
    * flask run

- Copy and paste the value of app/config.py:SERVER_NAME into your browser and you should see the homepage

