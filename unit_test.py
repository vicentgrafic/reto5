import unittest
import random
from model.Geometria import Geometria
from view.View import View

class test(unittest.TestCase):

    # 1 "setUp" existe en "unittest", define los atributos globales de la clase "TextFixture"
    def setUp(self):

        print("test.setUp")

        #crea un set de números
        self.testAttyibutes = []

        # parametrización correcta
        self.testAttyibutes.append([1, 2, 3])
        self.testAttyibutes.append([2.00, 3.00, 4.00])
        self.testAttyibutes.append([-2, -3, -4])
        self._selected_figura = random.randint(1, 8)

        # parametrización incorrecta, devolverá algún error en algún "assert()"
        #self._selected_figura = random.randint(-55, 55)
        #self.testAttyibutes.append([-2, 'a', -4])

    # 2.1 test 1
    def test_Geometria__Init__(self):

        print("test.test_Geometria__Init__")

        for value in enumerate(self.testAttyibutes):

            #print(f'index = {value[0]}')
            #print(f'valor = {value[1][0]}, {value[1][1]}, {value[1][2]}')
            #print(f'index + valor = {value}')

            geo = Geometria(value[1][0], value[1][1], value[1][2])

            # el constructor no puede devolver NONE
            self.assertIsNotNone(geo)

            #print(f'next...')

        print("test.test_Geometria__Init__ > OK")

    # 2.2 test 2
    def test_set_figuraName(self):

        print("test.test_set_figuraName")

        for value in enumerate(self.testAttyibutes):

            #print(f'index = {value[0]}')
            #print(f'valor = {value[1][0]}, {value[1][1]}, {value[1][2]}')
            #print(f'index + valor = {value}')

            geo = Geometria(value[1][0], value[1][1], value[1][2])

            #el método siempre devuelve NONE
            self.assertIsNone(geo.set_figuraName(self._selected_figura))

            #print(f'next...')

        print("test.test_set_figuraName > OK")

    # 2.3 test 3
    def test_switch(self):

        print("test.test_switch")

        for value in enumerate(self.testAttyibutes):

            #print(f'index = {value[0]}')
            #print(f'valor = {value[1][0]}, {value[1][1]}, {value[1][2]}')
            #print(f'index + valor = {value}')

            geo = Geometria(value[1][0], value[1][1], value[1][2])

            for i in range(1, 9):

                resul = geo.switch(i)
                print(f'_selected_figura={i}, resul={resul}')

                #el método siempre debe devolver un valor
                self.assertIsNotNone(resul)

                #el método siempre debe devolver valor mayor de 0
                self.assertGreater(resul, 0)

            #print(f'next...')

        print("test.test_switch > OK")

        #"assertEqual" compara todos los resultados de "r" con los valores esperados en la lista
        #self.assertEqual(r, [-6, -4, -2, 0, 2, 4, 6])

    # 2.4 test 4
    def test_view(self):

        print("test.test_view")

        for value in enumerate(self.testAttyibutes):
            # print(f'index = {value[0]}')
            # print(f'valor = {value[1][0]}, {value[1][1]}, {value[1][2]}')
            # print(f'index + valor = {value}')

            geo = Geometria(value[1][0], value[1][1], value[1][2])

            view = View.select(self, geo)
            print(view)

            #el método siempre devuelve NONE
            self.assertIsNone(view)

            # print(f'next...')

        print("test.test_view > OK")

        # "assertEqual" compara todos los resultados de "r" con los valores esperados en la lista
        # self.assertEqual(r, [-6, -4, -2, 0, 2, 4, 6])

    # 3 "tearDown" existe en "unittest", se ejecuta al final de la clase "TextFixture"
    def tearDown(self):

        print("test.tearDown")

        del self._selected_figura
        del self.testAttyibutes
