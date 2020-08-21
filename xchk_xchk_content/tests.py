import unittest
from django.test import TestCase
from unittest.mock import Mock, patch, MagicMock
from xchk_core.templatetags.xchk_instructions import node_instructions_2_ul
from xchk_core.strats import StratInstructions, AT_LEAST_ONE_TEXT, ALL_OF_TEXT
from .contentviews import *

class KeyElementsViewTest(TestCase):

    def test_short_form_answer(self):
        text = '2'
        self.assertTrue(KeyElementsView.pattern.fullmatch(text))

    def test_long_form_answer(self):
        text = 'twee'
        self.assertTrue(KeyElementsView.pattern.fullmatch(text))

    def test_incorrect_answer_partial_match(self):
        text = 'twaalf'
        self.assertFalse(KeyElementsView.pattern.fullmatch(text))
  
if __name__ == '__main__':
    unittest.main()
