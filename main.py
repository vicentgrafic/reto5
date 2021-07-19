from model.Geometria import Geometria
from view.View import View

#importa el fiechero con las pruebas unitarias
#from unit_test import test

if __name__ == '__main__':
    g = Geometria(2.00, 3.10, 4.00)
    v = View()
    v.select(g)