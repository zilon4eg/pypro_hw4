import json
import os


class WikiIterator:

    if os.path.exists('countries_url.txt'):
        os.remove('countries_url.txt')
    host = 'https://en.wikipedia.org'

    def __iter__(self):
        data = self.read_json()
        country_names = []
        list(country_names.append(country['name']['common']) for country in data)
        country_names.reverse()
        self.country_names = country_names
        return self


    def __next__(self):
        if not self.country_names:
            raise StopIteration
        country_name = self.country_names.pop()
        country_url = self.host + '/wiki/' + country_name.replace(' ', '_')
        return f'{country_name} - {country_url}'


    def read_json(self, path='countries.json'):
        with open(path, encoding='utf-8') as json_file:
            line = json.load(json_file)
            return line


    def write_txt(self, text, path='countries_url.txt'):
        with open(path, 'a', encoding='utf-8') as document:
            document.write(f'{text}' + '\n')


countries = WikiIterator()

for country in WikiIterator():
    countries.write_txt(country)