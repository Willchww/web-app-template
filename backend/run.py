from app import create_app, jwt
from app.db import db, reset_database

app = create_app()

jwt.init_app(app)
db.init_app(app)
with app.app_context():
    from app.db.models import *

    reset_database()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=9527)
