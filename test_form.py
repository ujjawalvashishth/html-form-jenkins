import unittest
from html.parser import HTMLParser
from pathlib import Path


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.form_found = False
        self.inputs = {}
        self.submit_found = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.form_found = True

        if tag == "input":
            field_id = attrs.get("id")
            if field_id:
                self.inputs[field_id] = attrs

        if tag == "button" and attrs.get("type") == "submit":
            self.submit_found = True


class TestHTMLForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        html_path = Path(__file__).parent / "index.html"
        cls.html = html_path.read_text(encoding="utf-8")

        cls.parser = FormParser()
        cls.parser.feed(cls.html)

    def test_form_exists(self):
        self.assertTrue(self.parser.form_found)

    def test_name_field_exists(self):
        self.assertIn("name", self.parser.inputs)

    def test_email_field_exists(self):
        self.assertIn("email", self.parser.inputs)

    def test_contact_field_exists(self):
        self.assertIn("contact", self.parser.inputs)

    def test_submit_button_exists(self):
        self.assertTrue(self.parser.submit_found)


if __name__ == "__main__":
    unittest.main(verbosity=2)
