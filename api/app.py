from flask import ( 
    Flask,
    jsonify
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import (
    relationship,
    Session,
    mapped_column,
    Mapped,
    DeclarativeBase
)
from flask_cors import CORS
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    MetaData,
    select,
    func,
    create_engine,
)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql://project-user:secretpassword@localhost:3306/project_db"
)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
metadata_obj = MetaData()

engine = create_engine(
    "mysql://project-user:secretpassword@localhost:3306/project_db", echo=True
)



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

class PointsPerTeamView(Base):
    __tablename__ = "total_points_per_team"

    team_id: Mapped[int] = mapped_column(primary_key=True)
    total_points_sum: Mapped[str]

    def __repr__(self) -> str:
        return f"PointsPerTeamView(team_id={self.team_id}, total_points_sum={self.total_points_sum})"


class PointsPerLeader(Base):
    __tablename__ = "total_points_per_leader"

    leader_person_id: Mapped[int] = mapped_column(primary_key=True)
    sum_points: Mapped[int]
    person_name: Mapped[str]



db = SQLAlchemy(model_class=Base)
db.init_app(app)


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/max_team")
def max_team():
    print("GET request max_team")
    statement = select(PointsPerTeamView).where(PointsPerTeamView.total_points_sum == select(func.max(PointsPerTeamView.total_points_sum)).subquery())
    session = Session(engine)
    row = session.execute(statement).first()
    session.close()
    print(row)
    print(row[0])
    return jsonify({
        "value": row[0].total_points_sum,
        "team_id": row[0].team_id
        })


@app.route("/max_leader")
def max_leader():
    print("GET request max_leader")
    statement = select(PointsPerLeader).where(PointsPerLeader.sum_points == select(func.max(PointsPerLeader.sum_points)).subquery())
    session = Session(engine)
    row = session.execute(statement).first()
    session.close()
    print(row)
    print(row[0])
    return jsonify({
        "sum_points": row[0].sum_points,
        "leader_person_id": row[0].leader_person_id,
        "person_name": row[0].person_name
        })

