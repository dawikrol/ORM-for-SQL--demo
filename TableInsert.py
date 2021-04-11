from TableModels import Cars, Teams, Drivers, engine

from sqlalchemy.orm import sessionmaker

session = sessionmaker()
session.configure(bind=engine)
my_session = session()


# insert teams
AlfaRomeo = Teams(team_name='Alfa Romeo', main_sponsor='PKN Orlen', engine_constructor='Ferrari')

my_session.add(AlfaRomeo)
my_session.commit()

Alpine = Teams(team_name='Alpine', main_sponsor='Alpine', engine_constructor='Renault')
AlphaTauri = Teams(team_name='AlphaTauri', main_sponsor='AlphaTauri', engine_constructor='Honda')
AstonMartin = Teams(team_name='Aston Martin', main_sponsor='Cognizant', engine_constructor='Mercedes')
Ferrari = Teams(team_name='Ferrari', main_sponsor='Shell', engine_constructor='Ferrari')
Haas = Teams(team_name='Haas', main_sponsor='1&1', engine_constructor='Ferrari')
McLaren = Teams(team_name='McLaren', main_sponsor='British American Tobacco', engine_constructor='Mercedes')
Mercedes = Teams(team_name='Mercedes', main_sponsor='Petronas', engine_constructor='Mercedes')
RedBull = Teams(team_name='Red Bull', main_sponsor='Red Bull', engine_constructor='Honda')
Williams = Teams(team_name='Williams', main_sponsor='Williams', engine_constructor='Mercedes')

my_session.add_all([Alpine, AlphaTauri, AstonMartin, Ferrari, Haas, McLaren, Mercedes, RedBull, Williams])
my_session.commit()

# insert cars
AR7 = Cars(number=7, team_id=1)
AR99 = Cars(number=99, team_id=1)
AT10 = Cars(number=10, team_id=2)
AT22 = Cars(number=22, team_id=2)
A31 = Cars(number=31, team_id=3)
A14 = Cars(number=14, team_id=3)
AM5 = Cars(number=5, team_id=4)
AM18 = Cars(number=18, team_id=4)
F16 = Cars(number=16, team_id=5)
F55 = Cars(number=55, team_id=5)
H9 = Cars(number=9, team_id=6)
H47 = Cars(number=47, team_id=6)
ML3 = Cars(number=3, team_id=7)
ML4 = Cars(number=4, team_id=7)
M77 = Cars(number=77, team_id=8)
M44 = Cars(number=44, team_id=8)
RB33 = Cars(number=33, team_id=9)
RB11 = Cars(number=11, team_id=9)
W6 = Cars(number=6, team_id=10)
W63 = Cars(number=63, team_id=10)


my_session.add_all([AR7, AR99, AT22, AT10, A31, A14, AM5, AM18, F55, F16,
                    H47, H9, ML4, ML3, M77, M44, RB11, RB33, W63, W6])
my_session.commit()

# insert drivers

Hamilton = Drivers(first_name='Lewis', last_name='Hamilton', car_id=16)
Bottas = Drivers(first_name='Valtteri', last_name='Bottas', car_id=15)
Verstappen = Drivers(first_name='Max', last_name='Verstappen', car_id=18)
Perez = Drivers(first_name='Sergio', last_name='Perez', car_id=17)
Ricciardo = Drivers(first_name='Daniel', last_name='Ricciardo', car_id=14)
Norris = Drivers(first_name='Lando', last_name='Norris', car_id=13)
Stroll = Drivers(first_name='Lance', last_name='Stroll', car_id=8)
Vettel = Drivers(first_name='Sebastian', last_name='Vettel', car_id=7)
Alonso = Drivers(first_name='Fernando', last_name='Alonso', car_id=6)
Ocon = Drivers(first_name='Esteban', last_name='Ocon', car_id=5)
Leclerc = Drivers(first_name='Charles', last_name='Leclerc', car_id=10)
Sainz = Drivers(first_name='Carlos', last_name='Sainz', car_id=9)
Gasly = Drivers(first_name='Pierre', last_name='Gasly', car_id=4)
Tsunoda = Drivers(first_name='Yuki', last_name='Tsunoda', car_id=3)
Raikkonen = Drivers(first_name='Kimi', last_name='Raikkonen', car_id=1)
Giovinazzi = Drivers(first_name='Antonio', last_name='Giovinazzi', car_id=2)
Schumacher = Drivers(first_name='Mick', last_name='Schumacher', car_id=11)
Mazepin = Drivers(first_name='Nikita', last_name='Mazepin', car_id=12)
Russell = Drivers(first_name='George', last_name='Russell', car_id=19)
Latifi = Drivers(first_name='Nicholas', last_name='Latifi', car_id=20)

my_session.add_all([Hamilton, Bottas, Verstappen, Perez, Ricciardo, Norris, Stroll, Vettel, Alonso, Ocon,
                    Leclerc, Sainz, Gasly, Tsunoda, Raikkonen, Giovinazzi, Schumacher, Mazepin, Russell, Latifi])

my_session.commit()








