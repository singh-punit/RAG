import unittest
from pythonclass import count_letters


class TestCountLetters(unittest.TestCase):

    def test_basic_string(self):
        """Test with a simple string containing only letters"""
        self.assertEqual(count_letters("hello"), 5)
        self.assertEqual(count_letters("Python"), 6)

    def test_string_with_spaces(self):
        """Test with strings containing spaces"""
        self.assertEqual(count_letters("hello world"), 10)
        self.assertEqual(count_letters("Punit Singh"), 10)

    def test_string_with_numbers(self):
        """Test with strings containing numbers"""
        self.assertEqual(count_letters("abc123"), 3)
        self.assertEqual(count_letters("test123test"), 8)

    def test_string_with_special_characters(self):
        """Test with strings containing special characters"""
        self.assertEqual(count_letters("hello!@#"), 5)
        self.assertEqual(count_letters("test-case_example"), 15)

    def test_mixed_case(self):
        """Test with mixed uppercase and lowercase"""
        self.assertEqual(count_letters("HeLLo WoRLd"), 10)
        self.assertEqual(count_letters("PyThOn"), 6)

    def test_empty_string(self):
        """Test with empty string"""
        self.assertEqual(count_letters(""), 0)

    def test_only_numbers(self):
        """Test with string containing only numbers"""
        self.assertEqual(count_letters("12345"), 0)

    def test_only_special_characters(self):
        """Test with string containing only special characters"""
        self.assertEqual(count_letters("!@#$%^&*()"), 0)

    def test_only_spaces(self):
        """Test with string containing only spaces"""
        self.assertEqual(count_letters("   "), 0)

    def test_unicode_letters(self):
        """Test with unicode letters"""
        self.assertEqual(count_letters("café"), 4)
        self.assertEqual(count_letters("naïve"), 5)


if __name__ == "__main__":
    unittest.main()
