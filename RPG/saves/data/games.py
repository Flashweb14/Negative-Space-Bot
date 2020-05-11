import sqlalchemy
from .db_session import SqlAlchemyBase


class DBGame(SqlAlchemyBase):
    __tablename__ = 'games'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    chat_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    player_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    current_location = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    spaceship_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    state = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    player_inventory = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    player_money = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    player_hp = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    player_armor = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    player_weapon = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    player_armor_set = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    player_laser_ammo = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    fight_system_enemy = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    fight_system_max_action_points = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    fight_system_action_points = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    player_quest_items = sqlalchemy.Column(sqlalchemy.String, nullable=True)
