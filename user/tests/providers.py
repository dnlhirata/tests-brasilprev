from faker.providers import BaseProvider
from random import randint


class DocumentProvider(BaseProvider):
    def cpf(self):
        return str(randint(10000000000, 99999999999))

    def cnpj(self):
        return str(randint(10000000000000, 99999999999999))