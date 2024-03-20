from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from flask_cors import CORS
from sqlalchemy import 
Table,
Column,
Integer,
String,
ForeignKey,
MetaData,
select,
func,
create_engine,
Session


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://project-user:secretpassword@localhost:3306/project-db"
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
metadata_obj = MetaData()

engine = create_engine("mysql://project-user:secretpassword@localhost:3306/project-db", echo=True)
session = Session(engine)

class Base(DeclarativeBase):
    pass

class Person(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]


class Team(Base):
    __tablename__ = "team"

    id: Mapped[int] = mapped_column(primary_key=True)
    leader_person_id: Mapped[int] = mapped_column(ForeignKey(Person.id))

points_per_team_view = Table(
    "total_points_per_team",
    metadata_obj,
    Column("team_id", Integer, primary_key=True)
    
    )


db = SQLAlchemy(model_class=Base)
db.init_app(app)

@app.route("/")
def hello_world():
    return "Hello world"

@app.route("/max_team")
def max_team():
    statement = select(func.max(points_per_team_view.c.total_points_sum))
    return session.scalars(statement)
