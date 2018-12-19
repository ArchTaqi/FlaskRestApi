from app import db


class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Post(Base):
    __tablename__ = 'posts'

    title = db.Column(db.Text, nullable=False)
    slug = db.Column(db.Text, nullable=False)
    category = db.Column(db.Text)
    excrept = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    published = db.Column(db.Boolean, default=False, unique=False)
    author_id = db.Column(db.Text, unique = False)
    author_name = db.Column(db.Text, unique=False)
    views = db.Column(db.Integer, default=0)
    image_url = db.Column(db.Text, unique=False, nullable=True)
    suspended = db.Column(db.Boolean, unique=False, nullable=False)

    def __init__(self, title, slug, category, excrept, content, published, author_id, author_name, views, image_url, suspended):
        self.title = title
        self.slug = slug
        self.category = category
        self.excrept = excrept
        self.content = content
        self.published = published
        self.author_id = author_id
        self.author_name = author_name
        self.views = views
        self.image_url = image_url
        self.suspended = suspended

    def __repr__(self):
        return '<Post %r>' % (self.title)
