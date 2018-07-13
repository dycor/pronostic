from flask_appbuilder import Model
from flask_appbuilder.models.mixins import ImageColumn

class Team(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
