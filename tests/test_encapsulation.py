import unittest
from controllers import Encapsulation

class TestEncapsulation(unittest.TestCase):

    def test_success(self):
        name = Encapsulation.Name()
        name.setFirstName("Ken Dan")
        name.setMiddleName("S.")
        name.setLastName("Tinio")

        firstName  = name.getFirstName()
        middleName = name.getMiddleName()
        lastName   = name.getLastName()

        self.assertEqual(firstName+" "+middleName+" "+lastName, "Ken Dan S. Tinio")

    def test_error(self):
        name = Encapsulation.Name()
        name.setFirstName("Ken Dan")
        name.setMiddleName("S.")
        name.setLastName("Tinio")

        firstName  = name.getFirstName()
        middleName = name.getMiddleName()
        lastName   = name.getLastName()

        self.assertNotEqual(firstName+" "+middleName+" "+lastName, "Nenn kenn Tinio")
