"""Siersz logo: a two-tone geometric S built from two stacked circles.
Top arc = first life (navy), bottom arc = second life (amber).
Wordmark: heavy geometric capitals, flat caps, mitred joins."""
import math

AMBER = '#f5a524'
NAVY = '#14284b'


def s_paths(cx, y_top, y_bot, r, ang=28):
    """two arcs of an S made from circles centred (cx,y_top) and (cx,y_bot) (tangent at y_mid)"""
    a = math.radians(ang)
    mid = (y_top + y_bot) / 2
    x1, y1 = cx + r * math.cos(a), y_top - r * math.sin(a)
    x2, y2 = cx - r * math.cos(a), y_bot + r * math.sin(a)
    top = f'M{x1:.2f} {y1:.2f}A{r} {r} 0 1 0 {cx} {mid}'
    bot = f'M{cx} {mid}A{r} {r} 0 1 1 {x2:.2f} {y2:.2f}'
    return top, bot


def mark_group(top='currentColor', bottom=AMBER, ox=0, oy=0, scale=1.0):
    r, t = 11.5, 9.5
    tp, bp = s_paths(32, 20.5, 43.5, r)
    # amber arc starts 2 units left of the join so no seam shows; navy arc is drawn over it
    amber = 'M30 32H32' + bp[bp.index('A'):]
    return (f'<g transform="translate({ox} {oy}) scale({scale})" fill="none" stroke-width="{t}" stroke-linecap="butt">'
            f'<path d="{amber}" stroke="{bottom}"/><path d="{tp}" stroke="{top}"/></g>')


def word_group(color='currentColor', ox=0, oy=0, scale=1.0):
    r = 9
    tp, bp = s_paths(16, 13, 31, r)
    S = f'<path d="{tp}A{bp.split(chr(65),1)[1]}"/>'

    def g(tx, body):
        return f'<g transform="translate({tx} 0)">{body}</g>'
    parts = [
        g(-3, S),
        g(36, '<path d="M4 4V40"/>'),
        g(54, '<path d="M28 4H4V40H28M4 22H24"/>'),
        g(96, '<path d="M4 40V4H16A9 9 0 0 1 16 22H4M15 22L28 40"/>'),
        g(135, S),
        g(174, '<path d="M4 4H28L4 40H28"/>'),
    ]
    return (f'<g transform="translate({ox} {oy}) scale({scale})" fill="none" stroke="{color}" stroke-width="8" '
            f'stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10">' + ''.join(parts) + '</g>')


def logo_svg(cls='', top='currentColor', bottom=AMBER, word='currentColor', mark_only=False, tile=None):
    label = 'role="img" aria-label="Siersz"'
    if mark_only:
        bg = f'<rect width="64" height="64" rx="15" fill="{tile}"/>' if tile else ''
        return (f'<svg xmlns="http://www.w3.org/2000/svg" class="{cls}" viewBox="0 0 64 64" {label}>'
                f'{bg}{mark_group(top, bottom)}</svg>')
    sc = .85
    return (f'<svg xmlns="http://www.w3.org/2000/svg" class="{cls}" viewBox="0 0 254 64" {label}>'
            f'{mark_group(top, bottom)}{word_group(word, 76, (64 - 44 * sc) / 2, sc)}</svg>')
