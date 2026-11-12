import json
from pathlib import Path
from urllib.parse import unquote

root = Path('.')
previous = json.loads((root / 'src/politicians.json').read_text(encoding='utf-8'))
by_name = {person['name']: person for person in previous}
source = json.loads((root / 'cache/large-portraits.json').read_text(encoding='utf-8'))['members']
credits = {
    'Mirjam Bikker': ('Nienke van Denderen', 'CC BY-SA 4.0'),
    'Henri Bontenbal': ('Leonard Walpot', 'CC BY 4.0'),
    'Martin Bosma': ('SDVBou', 'CC BY-SA 4.0'),
    'Ruben Brekelmans': ('Ministerie van Defensie', 'CC BY-SA 4.0'),
    'Laurens Dassen': ('Ministerie van Buitenlandse Zaken', 'CC BY-SA 2.0'),
    'Ralf Dekker': ('S. Perquin', 'CC BY-SA 4.0'),
    'Jimmy Dijk': ('GeeJee', 'CC BY-SA 4.0'),
    'Inge van Dijk': ('DutchTB', 'CC BY-SA 4.0'),
    'Joost Eerdmans': ('Tweede Kamer der Staten-Generaal', 'CC BY 4.0'),
    'Marjolein Faber': ('Polish presidency of the Council of the EU 2025', 'Public domain'),
    'Habtamu de Hoop': ('Partij van de Arbeid', 'CC BY 2.0'),
    'Barbara Kathmann': ('Partij van de Arbeid', 'CC BY 2.0'),
    'Mona Keijzer': ('Jennifer Jacquemart / European Commission', 'CC BY 4.0'),
    'Jesse Klaver': ('GroenLinks', 'CC BY-SA 4.0'),
    'Ines Kostić': ('Partij voor de Dieren', 'CC BY-SA 4.0'),
    'Tom van der Lee': ('GroenLinks', 'CC BY-SA 4.0'),
    'Mohammed Mohandis': ('Partij van de Arbeid', 'CC BY 2.0'),
    'Songül Mutluer': ('Partij van de Arbeid', 'CC BY 2.0'),
    'Annabel Nanninga': ('Room for Discussion', 'CC BY 3.0'),
    'Esther Ouwehand': ('Partij voor de Dieren', 'CC BY-SA 4.0'),
    'Jan Paternotte': ('Jan Buteijn / D66', 'CC BY-SA 4.0'),
    'Caroline van der Plas': ('Tweede Kamer', 'CC BY-SA 4.0'),
    'Joost Sneller': ('Jan Buteijn / D66', 'CC BY-SA 4.0'),
    'Chris Stoffer': ('Cees van der Wal', 'Attribution'),
    'Henk Vermeer': ('Saskia Beek', 'CC BY-SA 4.0'),
    'Lisa Westerveld': ('GroenLinks', 'CC BY-SA 4.0'),
    'Femke Wiersma': ('Marzia Cosenza / European Commission', 'CC BY 4.0'),
    'Geert Wilders': ('Vox España', 'CC0'),
}
large_by_name = {person['name']: person for person in source}
people = []
for name, image in large_by_name.items():
    if name not in by_name:
        continue
    assert image['width'] >= 800, (name, image['width'])
    assert name in credits, f'No checked photo credit for {name}'
    old = by_name[name]
    filename = unquote(image['image'].split('/')[-1].split('?')[0])
    if filename.startswith('1920px-'):
        filename = filename[len('1920px-'):]
    filename = filename.replace(' ', '_')
    author, license_name = credits[name]
    people.append({
        **old,
        'image': image['image'].split('?')[0],
        'imageWidth': image['width'],
        'file': 'https://commons.wikimedia.org/wiki/File:' + filename,
        'credit': f'Foto: {author} · {license_name}',
    })
assert len(people) == 28, f'Expected 28 existing profiles with verified large portraits, got {len(people)}'
assert len({p['name'] for p in people}) == len(people)
assert all(p.get('roast') and p.get('tweedekamer') for p in people)
(root / 'src/politicians.json').write_text(json.dumps(people, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Updated', len(people), 'portraits to Commons images with verified source attribution.')
for p in people:
    print(f"{p['name']}: {p['imageWidth']} px — {p['credit']}")
print('Dropped profiles lacking an 800px Commons photo:', ', '.join(sorted(set(by_name) - {p['name'] for p in people})))
