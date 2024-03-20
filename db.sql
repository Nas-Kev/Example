
-- DATABASE DEFINITION

create table person (
    id int not null AUTO_INCREMENT,
    first_name not null varchar(255),
    last_name not null varchar(255)
);

create table team (
    id int not null AUTO_INCREMENT,
    leader_person_id int not null,
    primary key(id),
    Foreign Key (leader_person_id) REFERENCES person(id)
);

create table award (
    id int not null AUTO_INCREMENT,
    points_per_member int not null,
    points_per_leader int not null,
    primary key(id)
);


create table team_member (
    id int not null AUTO_INCREMENT,
    person_id int not null,
    team_id int not null,
    primary key(id),
    foreign key(person_id) references person(id),
    foreign key(team_id) references team(id)
);

create table project (
    id int not null AUTO_INCREMENT,
    `name` varchar(255),
    team_id int not null,
    award_id int not null,
    primary key(id),
    foreign key(team_id) references team(id),
    foreign key(award_id) references award(id) 
);

-- EXAMPLE DATA


insert into person(first_name, last_name) values 
('Anna', 'Mueller'),
('Franz', 'Meier'),
('Bob', 'Maler'),
('Rita', 'Ribisel'),
('Herbert', 'Orange'),
('Günther', 'Apfel'),
('Gottfried', 'Ingwer'),
('Richard', 'Rauscher'),
('Philipp', 'Neumann'),
('Christina', 'Kürbis'),
('Lukas', 'Lang'),
('Fabian', 'Wärter'),
('Rosemarie', 'Kellner'),
('Wilhelm', 'Bauer'),
('Irina', 'Friedrich');

insert into award(points_per_member, points_per_leader) values 
(10, 100),
(20, 50),
(5, 10),
(50, 300),
(25, 200),
(75, 100),
(55, 100),
(30, 75),
(25, 30),
(50, 150),
(35, 105);


insert into team(leader_person_id) values 
(1),
(3),
(2),
(1),
(6),
(5),
(2),
(3),
(4),
(8),
(9),
(11);

insert into team_member(team_id, person_id) values 
(1, 2),
(1, 3),
(1, 4),
(2, 5),
(2, 4),
(3, 5),
(3, 6),
(3, 1),
(3, 4),
(4, 5),
(4, 2),
(4, 3),
(4, 6), 
(5, 1),
(5, 8),
(5, 9),
(5, 10),
(5, 5),
(5, 2);

insert into project(name, team_id, award_id) values 
("Projekt1", 1, 1),
("Projekt2", 2, 10),
("Projekt3", 3, 7),
("Projekt4", 4, 3),
("Projekt5", 5, 5),
("Projekt6", 1, 6),
("Projekt7", 2, 8),
("Projekt8", 3, 9),
("Projekt9", 4, 2),
("Projekt10", 5, 1),
("Projekt11", 1, 4),
("Projekt12", 2, 8),
("Projekt13", 3, 7),
("Projekt14", 4, 9),
("Projekt15", 5, 10),
("Projekt16", 1, 11),
("Projekt17", 2, 1);


-- FIND BEST TEAM (most total points)

select team_id, sum(points_sum) as total_points_sum from (select team.id as team_id, project.id as project_id, sum(award.points_per_member) + award.points_per_leader as points_sum from team 
inner join project on project.team_id = team.id
inner join award on award.id = project.award_id
inner join team_member tm on tm.team_id = team.id  
group by team.id, project.id) my_select 
group by team_id
order by total_points_sum desc


-- FIND BEST TEAM MEMBER

-- VIEW total_points_per_member
select (select person.id as "person_id",
team.id as "team_id",
project.id as "project_id",
sum(award.points_per_member) as "sum_points"
from person 
inner join team_member tm on tm.person_id = person.id 
inner join team on team.id = tm.team_id
inner join project on project.team_id = team.id 
inner join award on award.id = project.award_id

group by person_id
order by person_id) total_points_per_member;

SELECT * FROM `total_points_per_member` t WHERE t.sum_points = (select max(sum_points) from total_points_per_member);

-- VIEW total_points_per_leader 

select team.id as team_id, project.id as project_id, 
team.leader_person_id, 
sum(award.points_per_leader) as sum_points,
concat(person.first_name, ' ', person.last_name) as person_name
from team 
inner join project on project.team_id = team.id 
inner join award on award.id = project.award_id
inner join person on person.id = team.leader_person_id
group by team.leader_person_id