from RPG.game_classes.base_enemy import BaseEnemy

ESTRAD_NATIVE = BaseEnemy('Местный абориген', 'Из туманных зарослей леса на тебя неожиданно нападает местный абориген',
                          80, 10, 3, 3, 3, 3)

enemies = {'Местный абориген': ESTRAD_NATIVE, '': None}
