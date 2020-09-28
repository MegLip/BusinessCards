from faker import Faker
fake = Faker("pl_PL")

class BaseContact():                                                             #1 def klasy BaseContact
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.phone}, {self.email}"     
    @property
    def label_length(self):
        return sum([len(self.first_name), len(self.last_name), 1])
    @property
    def contact_number(self):
        return self.phone
    def contact(self):
        return f"Wybieram numer: {self.contact_number} i dzwonię do {self.first_name} {self.last_name}"

class BusinessContact(BaseContact):                                                             #2 def klasy BusinessContact
    def __init__(self, first_name, last_name, phone, email, position, company, work_phone):
        super().__init__(first_name, last_name, phone, email)
        self.position = position
        self.company = company
        self.work_phone = work_phone

    @property
    def contact_number(self):
        return self.work_phone

def create_contacts(card_type, amount):                         #3 def function create_contacts
    cards = []
    for i in range(amount):
        if card_type == "base":
            cards.append(
                BaseContact(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone=fake.phone_number(),
                    email=fake.email(),
                )
            )
        elif card_type == "business":
            cards.append(
                BusinessContact(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone=fake.phone_number(),
                    position=fake.job(),
                    company=fake.company(),
                    work_phone=fake.phone_number(),
                    email=fake.email(),
                )
            )
    return cards