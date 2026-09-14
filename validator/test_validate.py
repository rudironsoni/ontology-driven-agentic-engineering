import copy
import json
import unittest
from pathlib import Path

from validator.validate import validate_document


EXAMPLE = Path(__file__).parents[1] / "examples" / "minimal" / "odae.json"


class ValidateTest(unittest.TestCase):
    def test_complete_example(self):
        document = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        self.assertEqual(validate_document(document), [])

    def test_unresolved_relation(self):
        document = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        invalid = copy.deepcopy(document)
        invalid["relations"][0]["to"] = "semantic:missing"
        self.assertEqual(
            validate_document(invalid),
            ["relations[0].to: unresolved semantic:missing"],
        )


if __name__ == "__main__":
    unittest.main()
