from faker import Faker
fake = Faker("pl_PL")


class BaseContact():             # 1 def klasy BaseContact
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.first_name}{self.last_name}, {self.phone}, {self.email}"

    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")

    @property
    def contact_number(self):
        return self.phone

    def contact(self):
        return f"Wybieram numer: {self.contact_number}\
             \ni dzwonię do {self.first_name} {self.last_name}"


class BusinessContact(BaseContact):    # 2 def klasy BusinessContact
    def __init__(self, first_name, last_name, phone,
                 email, job, company, business_phone):
        super().__init__(first_name, last_name, phone, email)
        self.job = job
        self.company = company
        self.business_phone = business_phone

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.phone},\
                {self.email}, {self.job}, {self.company},\
                    {self.business_phone}"

    @property
    def contact_number(self):
        return self.business_phone


def create_contacts(type_of_card, number):     # 3 def function create_contacts
    card_list = []
    for i in range(number):
        if type_of_card == "base":
            card_list.append(
                BaseContact(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone=fake.phone_number(),
                    email=fake.email(),
                )
            )
        elif type_of_card == "business":
            card_list.append(
                BusinessContact(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone=fake.phone_number(),
                    job=fake.job(),
                    company=fake.company(),
                    business_phone=fake.phone_number(),
                    email=fake.email(),
                )
            )
    return card_list


if __name__ == "__main__":        # 4 Choise type of card and number of copies
    type_of_card = input("Wybierz typ (base lub business): ")
    number = int(input("Podaj liczbę kopii: "))

    if type_of_card == 'base':
        print('\n', "Wizytówki base:", '\n', "***************")
        base_cards = create_contacts("base", number)
        for card in base_cards:
            print(card.contact())
            print("Długość imienia i nazwiska: ", card.label_length, '\n')
    elif type_of_card == 'business':
        print('\n', "Wizytówki biznesowe:", '\n', "********************")
        business_cards = create_contacts("business", number)
        for card in business_cards:
            print(card.contact())
            print("Długość imienia i nazwiska: ", card.label_length, '\n')
