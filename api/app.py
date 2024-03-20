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
from models import PointsPerTeamView, PointsPerLeader, Base, PointsPerMember


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql://project-user:secretpassword@localhost:3306/project_db"
)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
metadata_obj = MetaData()

engine = create_engine(
    "mysql://project-user:secretpassword@localhost:3306/project_db", echo=True
)







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
        "person_name": row[0].person_name,
        "project_count": row[0].project_count
        })


@app.route("/max_member")
def max_member():
    print("GET request max_member")
    
    statement = select(PointsPerMember).where(PointsPerMember.sum_points == select(func.max(PointsPerMember.sum_points)).subquery())
    session = Session(engine)
    row = session.execute(statement).first()
    session.close()
    print(row)
    print(row[0])
    return jsonify({
        "sum_points": row[0].sum_points,
        "person_id": row[0].person_id,
        "person_name": row[0].person_name,
        "project_count": row[0].project_count,
        "team_count": row[0].team_count
        })