from flask_jwt_extended import create_access_token, jwt_required
from flask_restplus import Namespace, Resource, reqparse

from config import PASSWORD

ns = Namespace("user", description="用户")
user_login_par = reqparse.RequestParser()
user_login_par.add_argument('username', required=True, help='username')
user_login_par.add_argument('password', required=True, help='password')


@ns.route('/login')
class UserApi(Resource):
    @ns.doc('login')
    @ns.expect(user_login_par)
    def post(self):
        """user login"""
        args = user_login_par.parse_args()
        username = args['username']
        password = args['password']
        if username != 'admin' or password != PASSWORD:
            return {"code": 10001, "msg": "Bad username or password"}, 200
        access_token = create_access_token(identity=username)
        return {
            "code": 0,
            "msg": "success",
            "data": {
                "access_token": access_token
            }
        }, 200
