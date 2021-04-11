import TableModels
import TableInsert
import sqlalchemy as db

driver = TableInsert.my_session.query(TableModels.Drivers).filter(TableModels.Drivers.driver_id == 1).one()
driver.first_name = 'David'
TableInsert.my_session.commit()

query = db.update(TableModels.Drivers)\
    .where(TableModels.Drivers.driver_id == 1).\
    values(first_name='Hamilton')
TableModels.connection.execute(query)