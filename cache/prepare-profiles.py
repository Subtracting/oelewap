import json
from pathlib import Path

old_roasts = {p['name']: p['roast'] for p in json.loads(Path('src/politicians.json').read_text(encoding='utf-8'))}

mapping = {
 'Sandra Beckerman': {'image': 'https://www.tweedekamer.nl/sites/default/files/styles/medium/public/2025-11/SP_Beckerman.jpg?itok=tnwArKwc', 'imageWidth': 773, 'file': 'https://www.tweedekamer.nl/kamerleden_en_commissies/alle_kamerleden/beckerman-sm-sp', 'credit': 'Portret: Tweede Kamer der Staten-Generaal'},
 'Diederik Boomsma': {'image': 'https://www.houseofrepresentatives.nl/sites/default/files/styles/medium/public/2025-11/JA21_Boomsma.jpg?itok=wuFgRGh3', 'imageWidth': 773, 'file': 'https://www.houseofrepresentatives.nl/members_of_parliament/members_of_parliament/boomsma-dt-ja21', 'credit': 'Portret: Tweede Kamer der Staten-Generaal'},
 'Martin Bosma': {'image': 'https://upload.wikimedia.org/wikipedia/commons/4/46/Martin-Bosma_%28cropped%29.jpg', 'imageWidth': 1023, 'file': 'https://commons.wikimedia.org/wiki/File:Martin-Bosma_(cropped).jpg', 'credit': 'Foto: SDVBou · CC BY-SA 4.0'},
 'Ruben Brekelmans': {'image': 'https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a6/Minister_van_Defensie_Ruben_Pieter_Brekelmans.jpg/1920px-Minister_van_Defensie_Ruben_Pieter_Brekelmans.jpg', 'imageWidth': 1600, 'file': 'https://commons.wikimedia.org/wiki/File:Minister_van_Defensie_Ruben_Pieter_Brekelmans.jpg', 'credit': 'Foto: Ministerie van Defensie · CC BY-SA 4.0'},
 'Dion Graus': {'image': 'https://www.tweedekamer.nl/sites/default/files/styles/medium/public/atoms/images/pvv_graus.jpg?itok=FoqT3vWg', 'imageWidth': 773, 'file': 'https://www.tweedekamer.nl/kamerleden_en_commissies/alle_kamerleden/graus-djg-pvv', 'credit': 'Portret: Tweede Kamer der Staten-Generaal'},
  'Gidi Markuszower': {'image': 'https://upload.wikimedia.org/wikipedia/commons/e/ec/Gidi_Markuszower.jpg', 'imageWidth': 317, 'file': 'https://commons.wikimedia.org/wiki/File:Gidi_Markuszower.jpg', 'credit': 'Portret: Tweede Kamer der Staten-Generaal · CC BY 3.0'},
 'Alexander Kops': {'image': 'https://www.tweedekamer.nl/sites/default/files/styles/medium/public/2025-11/PVV_Kops.jpg?itok=nj_34jkz', 'imageWidth': 773, 'file': 'https://www.tweedekamer.nl/kamerleden_en_commissies/alle_kamerleden/kops-pvv', 'credit': 'Portret: Tweede Kamer der Staten-Generaal'},
 'Edgar Mulder': {'image': 'https://www.tweedekamer.nl/sites/default/files/styles/medium/public/2025-11/PVV_Mulder.jpg?itok=7joK7hGL', 'imageWidth': 773, 'file': 'https://www.tweedekamer.nl/kamerleden_en_commissies/alle_kamerleden/mulder-e-pvv', 'credit': 'Portret: Tweede Kamer der Staten-Generaal'},
}
raw = json.loads(Path('cache/large-portraits.json').read_text(encoding='utf-8'))
requested_names = {p['name'] for p in json.loads(Path('src/politicians.json').read_text(encoding='utf-8'))}
large = {p['name']: p for p in raw['members']}
base = set(mapping)
roasts = {
'Martin Bosma': 'Heeft een voorzittershamer en denkt nu dat hij Thor is.',
'Ruben Brekelmans': 'Een PowerPoint in een net jasje, en toch ontbreekt de conclusie.',
'Sandra Beckerman': 'Een wandelende motie. De nietmachine is alvast gevlucht.',

'Diederik Boomsma': 'De man die van één standpunt een proefschrift maakt.',

'Laurens Dassen': 'Een pratende agenda-uitnodiging met een mening.',
'Ralf Dekker': 'Klinkt als een beleidsstuk dat zichzelf heeft leren praten.',
'Jimmy Dijk': 'Zelfs de interruptiemicrofoon zucht als deze opengaat.',
'Inge van Dijk': 'Een wandelende vergaderpauze met een zelfverzekerde hoofdlijn.',
'Joost Eerdmans': 'Kwam voor het debat, bleef hangen voor z’n eigen interruptie.',
'Marjolein Faber': '“Even praktisch,” zegt ze, en start een werkgroep.',
'Alexander Kops': 'Een motie van wantrouwen tegen de volumeknop.',
'Dion Graus': 'Een pannenkoek met spreektijd en een naamkaartje.',

'Barbara Kathmann': 'De spreadsheet vroeg om een woordvoerder. Toen ging het mis.',
'Mona Keijzer': 'Heeft “kort gezegd” nog nooit kort gezegd.',
'Jesse Klaver': 'LinkedIn in mensengedaante, met een extra schep gel in het haar.',
'Alexander Kops': 'Een motie van wantrouwen tegen de volumeknop.',
'Ines Kostić': 'Alsof een commissievergadering een menselijke vorm aannam.',
'Tom van der Lee': 'Burgemeester van Bijlage 7, met spreekrecht over de koffie.',
'Gidi Markuszower': 'Een persverklaring die op verzenden bleef hangen.',
'Edgar Mulder': 'Een beleidsnota met veters. Geen alinea komt ter zake.',
'Edgar Mulder': 'Een beleidsnota met veters. Geen alinea komt ter zake.',

'Edgar Mulder': 'Een beleidsnota met veters. Geen alinea komt ter zake.',
'Songül Mutluer': 'Kwam één punt maken en bouwde er een mappenstructuur omheen.',
'Annabel Nanninga': 'Een goober met interruptiekaart en alle tijd van de wereld.',
'Esther Ouwehand': 'De voorzitter zei “laatste vraag”. Zij hoorde “minstens drie”.',
'Jan Paternotte': 'Een wandelende motie. De punt ontbreekt nog.',
'Caroline van der Plas': 'Een wandelende frikandel speciaal met een microfoon.',
'Joost Sneller': 'Heeft “ter informatie” als persoonlijkheidskenmerk.',
'Chris Stoffer': 'De microfoon staat aan. De kern is nog onderweg.',
'Henk Vermeer': 'Een pannenkoek met een spreektijdslot en een reserve-slot.',
'Lisa Westerveld': 'De vergadering kon een mail zijn. Zij maakte er drie debatten van.',
'Geert Wilders': 'Burgemeester van Sukkelstad. De ambtsketting is van drop.',

'Geert Wilders': 'Burgemeester van Sukkelstad. De ambtsketting is van drop.',
}
people = []
for m in raw['members']:
    if m['name'] not in requested_names:
        continue
    if m['name'] in base:
        source = mapping[m['name']]
    elif m['name'] in large:
        im = large[m['name']]
        source = {'image': im['image'], 'imageWidth': im['width'], 'file': f"https://commons.wikimedia.org/wiki/File:{im['image'].split('/')[-1].replace('1920px-','').split('?')[0]}", 'credit': 'Foto: Wikimedia Commons'}
    else:
        raise RuntimeError('No image for active profile: ' + m['name'])
    if m['name'] in large:
        author_licenses = {
            'Mirjam Bikker': ('Nienke van Denderen', 'CC BY-SA 4.0'), 'Henri Bontenbal': ('Leonard Walpot', 'CC BY 4.0'), 'Martin Bosma': ('SDVBou', 'CC BY-SA 4.0'),
            'Ruben Brekelmans': ('Ministerie van Defensie', 'CC BY-SA 4.0'), 'Laurens Dassen': ('Ministerie van Buitenlandse Zaken', 'CC BY-SA 2.0'), 'Ralf Dekker': ('S. Perquin', 'CC BY-SA 4.0'),
            'Jimmy Dijk': ('GeeJee', 'CC BY-SA 4.0'), 'Inge van Dijk': ('DutchTB', 'CC BY-SA 4.0'), 'Joost Eerdmans': ('Tweede Kamer der Staten-Generaal', 'CC BY 4.0'),
            'Marjolein Faber': ('Polish presidency of the Council of the EU 2025', 'Public domain'), 'Habtamu de Hoop': ('Partij van de Arbeid', 'CC BY 2.0'),
            'Barbara Kathmann': ('Partij van de Arbeid', 'CC BY 2.0'), 'Mona Keijzer': ('Jennifer Jacquemart / European Commission', 'CC BY 4.0'), 'Jesse Klaver': ('GroenLinks', 'CC BY-SA 4.0'),
            'Ines Kostić': ('Partij voor de Dieren', 'CC BY-SA 4.0'), 'Tom van der Lee': ('GroenLinks', 'CC BY-SA 4.0'), 'Mohammed Mohandis': ('Partij van de Arbeid', 'CC BY 2.0'),
            'Songül Mutluer': ('Partij van de Arbeid', 'CC BY 2.0'), 'Annabel Nanninga': ('Room for Discussion', 'CC BY 3.0'), 'Esther Ouwehand': ('Partij voor de Dieren', 'CC BY-SA 4.0'),
            'Jan Paternotte': ('Jan Buteijn / D66', 'CC BY-SA 4.0'), 'Caroline van der Plas': ('Tweede Kamer', 'CC BY-SA 4.0'), 'Joost Sneller': ('Jan Buteijn / D66', 'CC BY-SA 4.0'),
            'Chris Stoffer': ('Cees van der Wal', 'Attribution'), 'Henk Vermeer': ('Saskia Beek', 'CC BY-SA 4.0'), 'Lisa Westerveld': ('GroenLinks', 'CC BY-SA 4.0'),
            'Femke Wiersma': ('Marzia Cosenza / European Commission', 'CC BY 4.0'), 'Geert Wilders': ('Vox España', 'CC0')}
        author, license = author_licenses[m['name']]
        source['credit'] = f'Foto: {author} · {license}'
    if m['name'] in old_roasts:
        roasts[m['name']] = old_roasts[m['name']]
    people.append({'name': m['name'], 'role': m['party'] + ' · Tweede Kamerlid', 'roast': roasts[m['name']], **source, 'tweedekamer': m['url']})
assert len(people) == len(requested_names) == 34
assert set(roasts) == requested_names
Path('src/politicians.json').write_text(json.dumps(people, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Prepared', len(people), 'members with official page links, source credits and a higher-resolution portrait candidate.')
