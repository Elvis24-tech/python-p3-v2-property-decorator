APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        """Initialize a Dog with name and breed."""
        self._name = None  
        self._breed = None  
        self.name = name  
        self.breed = breed  

    @property
    def name(self):
        """Get the dog's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set the dog's name, ensuring it's a string between 1 and 25 characters."""
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            raise ValueError("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        """Get the dog's breed."""
        return self._breed

    @breed.setter
    def breed(self, value):
        """Set the dog's breed, ensuring it's in the approved list."""
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            raise ValueError("Breed must be in list of approved breeds.")