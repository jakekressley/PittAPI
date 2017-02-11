import pprint
import unittest
import timeout_decorator

from PittAPI import dining, course

pp = pprint.PrettyPrinter(indent=2)

class PittServerDownException(Exception):
    """Raise when a Pitt server is down or timing out"""

class UnitTest(unittest.TestCase):
    def test_dining_encode_dining_location(self):
        self.assertEqual(dining._encode_dining_location('Cup & Chaucer - Hilman Library'), 'cup_&_chaucer-hillman')
        self.assertEqual(dining._encode_dining_location('Hill Top Grille - Sutherland Hall'), 'hill_top_grille-sutherland')
        self.assertEqual(dining._encode_dining_location('Market Central - Litchfield Towers'), 'market_central-towers')
        self.assertEqual(dining._encode_dining_location("Mato's - Sutherland Hall"), 'mato\'s-sutherland')
        self.assertEqual(dining._encode_dining_location('Quick Zone - Sutherland Hall'), 'quick_zone-sutherland')
        self.assertEqual(dining._encode_dining_location('Red Hot Chef - Sutherland Hall'), 'red_hot_chef-sutherland')
        self.assertEqual(dining._encode_dining_location(u'Bookstore Caf\xe9'), 'bookstore_cafe')
        self.assertEqual(dining._encode_dining_location('Bunsen Brewer - Chevron Science Center'), 'bunsen_brewer-chevron')
        self.assertEqual(dining._encode_dining_location('Burger King - Petersen Events Center Food Court'), 'burger_king-petersen')
        self.assertEqual(dining._encode_dining_location(u'Caf\xe9 at the Pete - Petersen Events Center Food Court'), 'cafe_at_the_pete-petersen')
        self.assertEqual(dining._encode_dining_location(u'Caf\xe9 Victoria'), 'cafe_victoria')
        self.assertEqual(dining._encode_dining_location(u'Cathedral Caf\xe9'), 'cathedral_cafe')
        self.assertEqual(dining._encode_dining_location('Cathedral Coffee'), 'cathedral_coffee')
        self.assertEqual(dining._encode_dining_location('Common Grounds - Litchfield Towers'), 'common_grounds-towers')
        self.assertEqual(dining._encode_dining_location('Culinary Classics - Schenley Cafe'), 'culinary_classics-schenley_cafe')
        self.assertEqual(dining._encode_dining_location('Einstein Bros Bagels - Benedum Hall'), 'einstein_bros_bagels-benedum')
        self.assertEqual(dining._encode_dining_location('Einstein Bros Bagels - Wesley W. Posvar, Second Floor'), 'einstein_bros_bagels-posvar')
        self.assertEqual(dining._encode_dining_location("Hill O' Beans - Sutherland Hall"), 'hill_o\'_beans-sutherland')
        self.assertEqual(dining._encode_dining_location("Nicola's Garden - Schenley Cafe"), 'nicola\'s_garden-schenley_cafe')
        self.assertEqual(dining._encode_dining_location('Oakland Bakery and Market - Amos Hall'), 'oakland_bakery_and_market-amos')
        self.assertEqual(dining._encode_dining_location('Pasta Plus - Petersen Events Center Food Court'), 'pasta_plus-petersen')
        self.assertEqual(dining._encode_dining_location('Pizza Hut Express - Schenley Cafe'), 'pizza_hut_express-schenley_cafe')
        self.assertEqual(dining._encode_dining_location('Salad Sensations - Petersen Events Center Food Court'), 'salad_sensations-petersen')
        self.assertEqual(dining._encode_dining_location('Simply To GO - Langley Hall'), 'simply_to_go-langley')
        self.assertEqual(dining._encode_dining_location('Strutters - Schenley Cafe'), 'strutters-schenley_cafe')
        self.assertEqual(dining._encode_dining_location('Sub Connection'), 'sub_connection')
        self.assertEqual(dining._encode_dining_location('Sub Connection - Schenley Cafe'), 'sub_connection-schenley_cafe')
        self.assertEqual(dining._encode_dining_location('Taco Bell - Schenley Cafe'), 'taco_bell-schenley_cafe')
        self.assertEqual(dining._encode_dining_location('The Pennsylvania Perk'), 'the_pennsylvania_perk')
        self.assertEqual(dining._encode_dining_location('The Side Bar - Barco Law Building'), 'the_side_bar-barco')
        self.assertEqual(dining._encode_dining_location('Thirst & Ten - Panther Hall'), 'thirst_&_ten-panther')

    def test_dining_decode_dining_location(self):
        self.assertEqual(dining._decode_dining_location('cup_&_chaucer-hillman'), 'Cup & Chaucer - Hilman Library')
        self.assertEqual(dining._decode_dining_location('hill_top_grille-sutherland'), 'Hill Top Grille - Sutherland Hall')
        self.assertEqual(dining._decode_dining_location('market_central-towers'), 'Market Central - Litchfield Towers')
        self.assertEqual(dining._decode_dining_location('mato\'s-sutherland'), "Mato's - Sutherland Hall")
        self.assertEqual(dining._decode_dining_location('quick_zone-sutherland'), 'Quick Zone - Sutherland Hall')
        self.assertEqual(dining._decode_dining_location('red_hot_chef-sutherland'), 'Red Hot Chef - Sutherland Hall')
        self.assertEqual(dining._decode_dining_location('bookstore_cafe'), 'Bookstore Caf\xe9')
        self.assertEqual(dining._decode_dining_location('bunsen_brewer-chevron'), 'Bunsen Brewer - Chevron Science Center')
        self.assertEqual(dining._decode_dining_location('burger_king-petersen'), 'Burger King - Petersen Events Center Food Court')
        self.assertEqual(dining._decode_dining_location('cafe_at_the_pete-petersen'), 'Caf\xe9 at the Pete - Petersen Events Center Food Court')
        self.assertEqual(dining._decode_dining_location('cafe_victoria'), 'Caf\xe9 Victoria')
        self.assertEqual(dining._decode_dining_location('cathedral_cafe'), 'Cathedral Caf\xe9')
        self.assertEqual(dining._decode_dining_location('cathedral_coffee'), 'Cathedral Coffee')
        self.assertEqual(dining._decode_dining_location('common_grounds-towers'), 'Common Grounds - Litchfield Towers')
        self.assertEqual(dining._decode_dining_location('culinary_classics-schenley_cafe'), 'Culinary Classics - Schenley Cafe')
        self.assertEqual(dining._decode_dining_location('einstein_bros_bagels-benedum'), 'Einstein Bros Bagels - Benedum Hall')
        self.assertEqual(dining._decode_dining_location('einstein_bros_bagels-posvar'), 'Einstein Bros Bagels - Wesley W. Posvar, Second Floor')
        self.assertEqual(dining._decode_dining_location('hill_o\'_beans-sutherland'), 'Hill O\' Beans - Sutherland Hall')
        self.assertEqual(dining._decode_dining_location('nicola\'s_garden-schenley_cafe'), "Nicola's Garden - Schenley Cafe")
        self.assertEqual(dining._decode_dining_location('oakland_bakery_and_market-amos'), 'Oakland Bakery and Market - Amos Hall')
        self.assertEqual(dining._decode_dining_location('pasta_plus-petersen'), 'Pasta Plus - Petersen Events Center Food Court')
        self.assertEqual(dining._decode_dining_location('pizza_hut_express-schenley_cafe'), 'Pizza Hut Express - Schenley Cafe')
        self.assertEqual(dining._decode_dining_location('salad_sensations-petersen'), 'Salad Sensations - Petersen Events Center Food Court')
        self.assertEqual(dining._decode_dining_location('simply_to_go-langley'), 'Simply To GO - Langley Hall')
        self.assertEqual(dining._decode_dining_location('strutters-schenley_cafe'), 'Strutters - Schenley Cafe')
        self.assertEqual(dining._decode_dining_location('sub_connection'), 'Sub Connection')
        self.assertEqual(dining._decode_dining_location('sub_connection-schenley_cafe'), 'Sub Connection - Schenley Cafe')
        self.assertEqual(dining._decode_dining_location('taco_bell-schenley_cafe'), 'Taco Bell - Schenley Cafe')
        self.assertEqual(dining._decode_dining_location('the_pennsylvania_perk'), 'The Pennsylvania Perk')
        self.assertEqual(dining._decode_dining_location('the_side_bar-barco'), 'The Side Bar - Barco Law Building')
        self.assertEqual(dining._decode_dining_location('thirst_&_ten-panther'), 'Thirst & Ten - Panther Hall')

    @timeout_decorator.timeout(15, timeout_exception=PittServerDownException)
    def test_dining_get_dining_locations(self):
        self.assertIsInstance(dining.get_dining_locations(), dict)

    @timeout_decorator.timeout(10, timeout_exception=PittServerDownException)
    def test_course_get_courses(self):
        self.assertIsInstance(course.get_courses("2177", "CS"), list)

    @timeout_decorator.timeout(10, timeout_exception=PittServerDownException)
    def test_course_get_courses_by_req(self):
        self.assertIsInstance(course.get_courses_by_req("2177", "Q"), list)

    @timeout_decorator.timeout(10, timeout_exception=PittServerDownException)
    def test_course_get_class_description(self):
        self.assertIsInstance(course.get_class_description("2177", "10045"), str)

if __name__ == '__main__':
    unittest.main()
