import json, urllib.parse, urllib.request
import bs4

base = 'https://www.tweedekamer.nl/kamerleden_en_commissies/alle_kamerleden'
req = urllib.request.Request(base, headers={'User-Agent': 'Mozilla/5.0 Oelewappers/1.0'})
soup = bs4.BeautifulSoup(urllib.request.urlopen(req, timeout=30).read(), 'html.parser')
members = []
for a in soup.select('h3 a'):
    card = a.find_parent(attrs={'data-testid': 'card'})
    if not card:
        continue
    party = card.select_one('.u-text-sm.u-text-primary')
    if party:
        members.append({'name': a.get_text(' ', strip=True), 'party': party.get_text(' ', strip=True), 'url': urllib.parse.urljoin(base, a['href'])})
results = []
for start in range(0, len(members), 35):
    batch = members[start:start+35]
    query = urllib.parse.urlencode({'action':'query','titles':'|'.join(x['name'] for x in batch),'prop':'pageimages','format':'json','piprop':'thumbnail','pithumbsize':1600,'redirects':'1'})
    request = urllib.request.Request('https://en.wikipedia.org/w/api.php?'+query, headers={'User-Agent':'Oelewappers/1.0 (quality portrait research)'})
    pages = json.load(urllib.request.urlopen(request, timeout=40))['query']['pages'].values()
    by_title = {p['title']: p for p in pages}
    for m in batch:
        p = by_title.get(m['name'], {})
        thumb = p.get('thumbnail', {})
        if thumb.get('source') and thumb.get('width', 0) >= 800:
            results.append({**m, 'width':thumb['width'], 'height':thumb['height'], 'image':thumb['source']})
print(json.dumps({'roster_count':len(members),'large_portraits_count':len(results),'members':results}, ensure_ascii=False, indent=2))
