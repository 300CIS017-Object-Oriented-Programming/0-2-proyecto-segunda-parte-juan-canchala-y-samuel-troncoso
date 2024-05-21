import unittest
from unittest.mock import patch
from io import StringIO
from pages.Evento import *  class TestEvento(unittest.TestCase):

    @patch("builtins.input", side_effect=["Daniel", "1001316869", "ejemplo@gmail.com", "301257069", "Rels B", "Nombre del evento", "2024-05-25", "10:00", "13:00", "Javeriana Cali", "Calle 20 # 11-30", "Yumbo", "realizado", "10000", "8000", "100", "1"])
    def test_crear_evento_bar(self, mock_input):
        eventos_bar_esperados = [EventoBar(Artista("Daniel", "1001316869", "ejemplo@gmail.com", "301257069", "Rels B", "Nombre del evento"), "Nombre del evento", datetime.date(2024, 5, 25), datetime.time(10, 100), datetime.time(130, 0), "Javeriana Cali", "Calle 20 # 11-30", "Yumbo", "realizado", 10000, 8000, "vacio", 100, 1)]
        eventos_bar_obtenidos = []

        with patch("sys.stdout", new=StringIO()) as fake_out:
            artistaslist.clear() 
            artistaslist.append(Artista("Daniel", "1001316869", "ejemplo@gmail.com", "301257069", "Rels B", "Nombre del evento"))
            crear_evento_bar()

            eventos_bar_obtenidos = eventosbar

        self.assertEqual(eventos_bar_esperados, eventos_bar_obtenidos)

if __name__ == "__main__":
    unittest.main()
