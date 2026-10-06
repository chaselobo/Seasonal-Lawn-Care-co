from pathlib import Path
from html import escape
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

ROOT = Path(__file__).parent
FOREST, CREAM, GOLD = '#173D32', '#F5F0E6', '#C49A52'
serif = TTFont(ROOT / 'fonts/dm-serif-display.ttf')
sans = TTFont(ROOT / 'fonts/dm-sans.ttf')

def lettering(text, font, size, x, baseline, fill, tracking=0):
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    scale = size / font['head'].unitsPerEm
    out = []
    for char in text:
        glyph = glyphs[cmap[ord(char)]]
        pen = SVGPathPen(glyphs)
        glyph.draw(TransformPen(pen, (scale, 0, 0, -scale, x, baseline)))
        if pen.getCommands():
            out.append(f'<path fill="{fill}" d="{pen.getCommands()}"/>')
        x += glyph.width * scale + tracking
    return ''.join(out)

def mark(color=FOREST, accent=GOLD):
    return ('<path d="M10 106V58a50 50 0 0 1 100 0v48" fill="none" '
            f'stroke="{color}" stroke-width="2.2"/>'
            f'<circle cx="60" cy="25" r="5" fill="{accent}"/>'
            + lettering('M', serif, 78, 22, 91, color)
            + f'<path d="M18 109Q58 92 102 109M27 117Q60 106 93 117" fill="none" '
              f'stroke="{color}" stroke-width="2.2" stroke-linecap="round"/>')

def svg(filename, w, h, content, title):
    title = escape(title, quote=True)
    (ROOT/'assets'/filename).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-label="{title}"><title>{title}</title>{content}</svg>')

for name, color, accent in [('primary', FOREST, GOLD), ('reversed', CREAM, GOLD), ('one-color', FOREST, FOREST)]:
    content = '<g transform="translate(8 8)">'+mark(color,accent)+'</g>'
    content += lettering('MONROE', serif, 63, 151, 73, color, 2.1)
    content += lettering('SEASONAL CO.', sans, 18, 154, 102, color, 4)
    content += lettering('LAWN & EXTERIOR CARE', sans, 12, 154, 128, color, 2.05)
    svg(f'logo-{name}.svg', 490, 145, content, 'Monroe Seasonal Co. — Lawn & Exterior Care')

svg('monogram.svg', 120, 126, mark(), 'Monroe Seasonal Co. monogram')
stack = '<g transform="translate(160 6)">'+mark()+'</g>'
stack += lettering('MONROE',serif,61,63,194,FOREST,2)
stack += lettering('SEASONAL CO.',sans,16,126,226,FOREST,3)
stack += lettering('LAWN & EXTERIOR CARE',sans,10,121,251,FOREST,1.7)
svg('logo-stacked.svg',440,275,stack,'Monroe Seasonal Co. stacked logo')
svg('social-avatar.svg',400,400,f'<rect width="400" height="400" rx="0" fill="{FOREST}"/><g transform="translate(95 88) scale(1.75)">{mark(CREAM,GOLD)}</g>','Monroe Seasonal Co. social avatar')
svg('favicon.svg',64,64,f'<rect width="64" height="64" rx="12" fill="{FOREST}"/>'+lettering('M',serif,49,8,50,CREAM),'Monroe Seasonal Co. favicon')
compact = '<g transform="translate(0 0) scale(.65)">'+mark()+'</g>'
compact += lettering('MONROE',serif,45,94,47,FOREST,1)
compact += lettering('SEASONAL CO.',sans,14,97,72,FOREST,2.1)
svg('logo-compact.svg',330,84,compact,'Monroe Seasonal Co. compact logo')
print('Created eight outlined SVG assets.')
