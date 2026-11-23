"""src/template.html + src/data.json -> index.html"""
import pathlib
root = pathlib.Path(__file__).resolve().parent
html = (root / 'template.html').read_text(encoding='utf-8')
data = (root / 'data.json').read_text(encoding='utf-8').replace('</', '<\\/')
(root.parent / 'index.html').write_text(html.replace('__DATA__', data), encoding='utf-8')
print('index.html built')
