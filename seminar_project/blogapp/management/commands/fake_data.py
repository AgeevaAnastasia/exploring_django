from django.core.management.base import BaseCommand
from blogapp.models import Author
from random import randint, choice


class Command(BaseCommand):
    help = "Generate fake authors"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        names = [
            'John', 'Anna', 'Ruth', 'Alice', 'Dan', 'Ethan', 'Eric', 'Sophia', 'Arny', 'Helen',
            'Jane', 'Jude', 'Rina', 'Dana', 'Nina', 'Erin', 'Jack', 'Phil', 'Penn', 'Dennis'
        ]
        lastnames = [
            'Beverly', 'Collins', 'Daniels', 'Davis', 'Miller', 'Taylor', 'Martin', 'Lee', 'Evans',
            'Ford', 'Gilmore', 'Harris', 'Holmes', 'Labert', 'Moore', 'Newman', 'Riley',
            'Stephenson', 'Wallace', 'Washington'
        ]
        count = kwargs.get('count')
        for _ in range(1, count + 1):
            tmp_name = names[randint(0, 19)]
            tmp_lastname = lastnames[randint(0, 19)]
            tmp_date = (choice(["1960", "1961", "1962", "1963", "1964", "1965", "1966", "1967",
                                "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975",
                                "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983",
                                "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991",
                                "1992", "1993", "1994", "1996", "1997", "1998", "1999", "2000",
                                "2001", "2002", "2003", "2004", "2005", "2006"]) + "-"
                        + choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                                  "11", "12"]) + "-"
                        + choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                                  "21", "22", "23", "24", "25", "26", "27", "28"]))
            author = Author(name=f'{tmp_name}',
                            lastname=f'{tmp_lastname}',
                            email=f'{tmp_name.lower()}{tmp_lastname.lower()}@yahoo.com',
                            bio=f'{tmp_name} {tmp_lastname} is our author. '
                                f'{tmp_name} {tmp_lastname} writes articles and make comments',
                            birthdate=f'{tmp_date}')
            author.save()
        self.stdout.write(f'{count} authors created')
