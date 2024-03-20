from sqlalchemy.orm import (
    relationship,
    Session,
    mapped_column,
    Mapped,
    DeclarativeBase
)
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
class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]

    def __repr__(this):
        return f"Person(id={this.id}, first_name={this.first_name}, last_name={this.last_name})"


class Team(Base):
    __tablename__ = "team"

    id: Mapped[int] = mapped_column(primary_key=True)
    leader_person_id: Mapped[int] = mapped_column(ForeignKey(Person.id))

    def __repr__(this):
        return f"Team(id={this.id}, leader_person_id={this.leader_person_id})"


class Award(Base):
    __tablename__ = "award"

    id: Mapped[int] = mapped_column(primary_key=True)
    points_per_member: Mapped[int]
    points_per_leader: Mapped[int]

    def __repr__(this):
        return f"Award(id={this.id}, points_per_member={this.points_per_member}, points_per_leader={this.points_per_leader})"


class Project(Base):
    __tablename__ = "project"

    id: Mapped[int] = mapped_column(primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey(Team.id))
    award_id: Mapped[int] = mapped_column(ForeignKey(Award.id))






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
    project_count: Mapped[int]


class PointsPerMember(Base):
    __tablename__ = "total_points_per_member"

    person_id: Mapped[int] = mapped_column(primary_key=True)
    person_name: Mapped[str]
    team_count: Mapped[int]
    project_count: Mapped[int]
    sum_points: Mapped[int]