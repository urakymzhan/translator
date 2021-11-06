# pip install --upgrade "ibm-watson>=5.3.0" # watson api install
# pip install pylint # checks for linting

""" module is responsible for translating english to french"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# config vars
URL_LT = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/079f130c-0aab-4219-ae98-8d5f8f5e0f41"
APIKEY_LT = "7T2SvoV0qUjUGMtK-kTg_lYooeAs-IxkJZ39SxVuiYao"
VERSION_LT='2018-05-01'

# setup
authenticator = IAMAuthenticator(APIKEY_LT)
language_translator = LanguageTranslatorV3(version=VERSION_LT, authenticator=authenticator)
language_translator.set_service_url(URL_LT)

def englishtofrench(text_to_tranlsate):
    """ function returns the english to french translation"""
    translation_res = language_translator.translate(
    text=text_to_tranlsate, model_id='en-fr')
    translation = translation_res.get_result()
    french_translation = translation['translations'][0]['translation']
    return french_translation

def englishtogerman(text_to_tranlsate):
    """ function returns the english to german translation"""
    translation_res = language_translator.translate(
    text=text_to_tranlsate, model_id='en-de')
    translation = translation_res.get_result()
    german_translation = translation['translations'][0]['translation']
    return german_translation


# TEST

import unittest
from translator import englishtofrench, englishtogerman

class TestEnglishToFrench(unittest.TestCase):

    def test_city(self):
        self.assertEqual(englishtofrench('City'), 'Ville') # test when text is City.

    def test_hello(self):
        self.assertEqual(englishtofrench('Hello'), 'Bonjour') # test when text is Hello.
    
    def test_null_reg(self):
        self.assertRaisesRegex(ValueError, 'text must be provided', englishtofrench, None) # test when text is None.

    def test_null(self):
        self.assertRaises(ValueError, englishtofrench, None) # test when text is None.

    def test_goat(self):
        self.assertEqual(englishtofrench('My name is goat'), 'Mon nom est la chèvre') # test when text is My name is goat.

class TestEnglishToGerman(unittest.TestCase):

    def test_city(self):
        self.assertEqual(englishtogerman('City'), 'Stadt') # test when text is City.

    def test_hello(self):
        self.assertEqual(englishtogerman('Hello'), 'Hallo') # test when text is Hello.
    
    def test_null_reg(self):
        self.assertRaisesRegex(ValueError, 'text must be provided', englishtogerman, None) # test when text is None.

    def test_null(self):
        self.assertRaises(ValueError, englishtogerman, None) # test when text is None.

    def test_cats(self):
        self.assertEqual(englishtogerman('I love cats'), 'Ich liebe Katzen') # test when text is I love cats.


if __name__ == '__main__':
    unittest.main()



# Example
def square(number):
    """
    This function returns the square of a given number
    """
    return number ** 2


def double(number):
    """
    This function returns twice the value of a given number
    """
    return number * 2 


# Example Test
import unittest

from mymodule import square, double

class TestSquare(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.


class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.

unittest.main()