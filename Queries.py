import TableModels
import sqlalchemy as db
from sqlalchemy import func


drivers = TableModels.my_session.query(TableModels.Drivers).all()

for driver in drivers:
    print(driver)

# we have access to fields of class
first = TableModels.my_session.query(TableModels.Drivers).first().first_name
print(first)

# using filter
number_above_ten = TableModels.my_session.query(TableModels.Cars).filter(TableModels.Cars.number > 20).all()
lan_drivers = TableModels.my_session.query(TableModels.Drivers)\
    .filter(TableModels.Drivers.first_name.like('%lan%')).all()

print(number_above_ten)
print(lan_drivers)


# using func
sum_of_numbers = TableModels.my_session.query(func.sum(TableModels.Cars.number)).scalar()
print(sum_of_numbers)

# using limiting and ordering
honda_teams = TableModels.my_session.query(TableModels.Teams).filter(TableModels.Teams.engine_constructor=='Honda')\
    .order_by(db.desc('main_sponsor'))\
    .limit(2).all()
print(honda_teams)

# conjunctions
mercedes_or_shell = TableModels.my_session.query(TableModels.Teams)\
    .filter(db.or_(TableModels.Teams.team_name.like('%Mercedes%'), TableModels.Teams.main_sponsor.like('%Shell%')))\
    .all()
print(mercedes_or_shell)

# join
team_car = TableModels.my_session.query(TableModels.Teams, TableModels.Cars).\
    join(TableModels.Teams, TableModels.Cars.team_id==TableModels.Teams.team_id).all()
print(team_car)