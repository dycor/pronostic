def init():
    # global myList
    # myList = []

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/python'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '2.7.0Kaaris'

    db = SQLAlchemy(app)
    global app,db