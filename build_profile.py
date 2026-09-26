"""Edit the profile text below, then run: python3 build_profile.py"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
PORTRAIT = (ROOT / 'portrait.txt').read_text().splitlines()

# Each tuple is (label, value); a None entry adds one blank line.
PROFILE = [
    ('Name', 'Abdullah'),
    ('Role', 'Software Engineer'),
    ('Focus', 'AI Evaluation & Research'),
    None,
    ('about', ''),
    ('', 'I build software and evaluation tools'),
    ('', 'to understand how AI systems perform'),
    ('', 'on real-world tasks.'),
    None,
    ('work', ''),
    ('', 'Agent benchmarks & tool-use evaluation'),
    ('', 'Dataset quality & model assessment'),
    ('', 'Machine learning & full-stack apps'),
    None,
    ('stack', ''),
    ('Languages', 'Python / JavaScript / Dart / SQL'),
    ('Web', 'React / Node.js'),
    ('Apps', 'Flutter / Firebase'),
    None,
    ('interests', ''),
    ('', 'Long-horizon agents'),
    ('', 'Reproducible evaluation'),
    ('', 'Useful software, built carefully.'),
]

def make_svg(dark):
    bg, fg, muted, accent, border = (
        ('#0d1117', '#e6edf3', '#8b949e', '#79c0ff', '#30363d') if dark else
        ('#ffffff', '#24292f', '#57606a', '#0969da', '#d0d7de')
    )
    out = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="690" viewBox="0 0 1200 690" role="img" aria-labelledby="title desc">
<title id="title">Abdullah | Software Engineer</title>
<desc id="desc">An ASCII portrait alongside a terminal-style profile about software engineering, AI evaluation, and agent benchmarks.</desc>
<rect x="1" y="1" width="1198" height="688" rx="16" fill="{bg}" stroke="{border}"/>
<g font-family="DejaVu Sans Mono, monospace">
<text x="30" y="37" font-size="13" fill="{muted}">abdullah@github:~</text>
<text x="1170" y="37" text-anchor="end" font-size="12" fill="{muted}">~/profile</text>
<path d="M1 57H1199" stroke="{border}"/>
''']
    # Preserve all supplied art characters; discard only Markdown escaping.
    for i, line in enumerate(PORTRAIT):
        out.append(f'<text x="28" y="{90+i*9.9:.1f}" font-size="9" fill="{fg}" xml:space="preserve">{escape(line)}</text>')
    out.append(f'<path d="M595 88V640" stroke="{border}"/>')
    out.append(f'<text x="627" y="107" font-size="18" fill="{accent}" font-weight="bold">AbdullahChaudhary0@github</text>')
    out.append(f'<text x="627" y="132" font-size="14" fill="{muted}">------------------------</text>')
    y=160
    for entry in PROFILE:
        if entry is not None:
            label,value=entry
            if label and not value:
                content=f'<tspan fill="{accent}" font-weight="bold">./{escape(label)}</tspan>'
            elif label:
                content=f'<tspan fill="{accent}">{escape(label+":"):11}</tspan><tspan fill="{fg}">{escape(value)}</tspan>'
            else:
                content=f'<tspan fill="{fg}">{escape(value)}</tspan>'
            out.append(f'<text x="627" y="{y}" font-size="13" xml:space="preserve">{content}</text>')
        y+=19
    for i,color in enumerate(['#f85149','#d29922','#3fb950','#58a6ff','#bc8cff','#39c5cf','#8b949e','#e6edf3']):
        out.append(f'<rect x="{627+i*25}" y="622" width="25" height="14" fill="{color}"/>')
    out.append('</g></svg>')
    return '\n'.join(out)

for dark,name in [(True,'dark_mode.svg'),(False,'light_mode.svg')]:
    (ROOT/name).write_text(make_svg(dark))
print('Created dark_mode.svg and light_mode.svg')
