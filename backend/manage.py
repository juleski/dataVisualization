from flask_app.app import *
from flask_app.data.dataInit import *
from flask_script import Manager


manager = Manager(app)

@manager.command
def run_server():
	#populate_es_data()
	app.run(debug=True, host='0.0.0.0')
	
@manager.command
def init_data():
	populate_es_data()

if __name__ == "__main__":
    manager.run()