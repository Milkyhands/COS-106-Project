"""Check required pages, duplicate IDs and local file references without dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
ROOT = Path(__file__).resolve().parents[1] / 'pages'
class Document(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.refs=[]; self.tags=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.tags.append(tag)
        if 'id' in a: self.ids.append(a['id'])
        for k in ('src','href','poster'):
            if k in a: self.refs.append(a[k])
for name in ('index','about','projects','planner','contact'):
    path=ROOT/f'{name}.html'; doc=Document(); doc.feed(path.read_text())
    assert len(doc.ids)==len(set(doc.ids)), f'Duplicate IDs in {path.name}'
    assert all(t in doc.tags for t in ('header','nav','main','footer')), path.name
    for ref in doc.refs:
        url=urlsplit(ref)
        if url.scheme or url.netloc: continue
        target=(path.parent/unquote(url.path)) if url.path else path
        assert target.is_file(), f'Missing asset: {path.name} -> {ref}'
        if url.fragment and target.suffix=='.html':
            other=Document(); other.feed(target.read_text())
            assert url.fragment in other.ids, f'Missing anchor: {ref}'
    print(f'PASS: {path.name}')
print('All page, ID, asset and anchor checks passed.')
