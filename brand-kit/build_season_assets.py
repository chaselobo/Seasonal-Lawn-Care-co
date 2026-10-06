from pathlib import Path
from html import escape

root=Path(__file__).parent/'assets'
navy='#17364D'
icons={
'spring':('<path d="M49 80V53"/><path d="M49 59C26 58 20 44 21 28C40 28 51 38 49 59Z" fill="currentColor" stroke="none"/><path d="M50 48C51 28 66 23 80 24C78 42 67 50 50 48Z" fill="currentColor" stroke="none"/>','#48A34A'),
'summer':('<circle cx="50" cy="50" r="16" fill="currentColor" stroke="none"/><path d="M50 14V23M50 77V86M14 50H23M77 50H86M25 25L31 31M69 69L75 75M25 75L31 69M69 31L75 25"/>','#F8C543'),
'fall':('<path d="M50 14L60 31L72 24L70 42L85 43L74 58L80 66L58 72L50 85L42 72L20 66L27 57L15 43L31 41L28 24L42 31Z" fill="currentColor" stroke="none"/><path d="M50 34V74M34 51L50 64L66 49" stroke="#ED783D" stroke-width="4"/>','#ED783D'),
'winter':('<path d="M50 14V86M19 32L81 68M19 68L81 32M41 21L50 29L59 21M41 79L50 71L59 79M21 43L33 40L32 28M68 72L67 60L79 57M21 57L33 60L32 72M68 28L67 40L79 43"/>','#59AFE0')}

def symbol(name,color='white'):
    return f'<g fill="none" color="{color}" stroke="currentColor" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">{icons[name][0]}</g>'

for name,(_,color) in icons.items():
    s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="{name.title()}"><title>{name.title()}</title><rect x="2" y="2" width="96" height="96" rx="22" fill="{color}" stroke="{navy}" stroke-width="4"/>{symbol(name)}</svg>'
    (root/f'{name}.svg').write_text(s)

content=''
for i,(name,(_,color)) in enumerate(icons.items()):
    x,y=(i%2)*104,(i//2)*104
    content+=f'<g transform="translate({x} {y})"><rect x="2" y="2" width="96" height="96" rx="22" fill="{color}" stroke="{navy}" stroke-width="4"/>{symbol(name)}</g>'
(root/'season-mark.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 204 204" role="img" aria-label="Spring, summer, fall, and winter"><title>Monroe four-season mark</title>{content}</svg>')
(root/'favicon.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 204 204">{content}</svg>')
print('Created four seasonal icons, a companion season mark, and a favicon.')
