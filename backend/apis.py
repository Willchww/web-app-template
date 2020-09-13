from flask import Blueprint
from flask_restplus import Api

api_blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_blueprint,
          version="1.0",
          prefix="/v1",
          doc="/doc",
          title="API文档",
          description="""
""")
