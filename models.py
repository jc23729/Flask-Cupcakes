"""Models for Cupcake app."""
"""Part One: Cupcake Model
Create Cupcake model in models.py.

It should have the following columns:

id: a unique primary key that is an auto-incrementing integer
flavor: a not-nullable text column
size: a not-nullable text column
rating: a not-nullable column that is a float
image: a non-nullable text column. If an image is not given, default to https://tinyurl.com/demo-cupcake
Make a database called cupcakes.

Once you’ve made this, you can run our seed.py file to add a few sample cupcakes to your database."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    """Cupcake"""
    __tablename__ ="cupcakes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE)

    def to_dict(self):
        """Serialize cupcake to a dict of cupcake info."""
        return {
                "id": self.id,
                "flavor": self.flavor,
                "rating": self.rating,
                "size": self.size,
                "image": self.image,
                }

def connect_db(app):
    """Connect to the database"""
    db.app = app
    db.init_app(app)