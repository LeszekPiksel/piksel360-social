"""Piksel360 social slide kit v2: photo-led HTML slides rendered with Playwright."""
import json, os, subprocess, pathlib, html as H

SITE = '/mnt/project-files/piksel360.pl STRONA/piksel360.pl/img/'
LOGO = 'file://' + SITE + 'logo-białe-piksel-360.png'
FONT = '/usr/share/fonts/opentype/inter/Inter-'
HERE = pathlib.Path(__file__).parent

def u(p):
    if p.startswith('http') or p.startswith('file://'): return p
    return 'file://' + os.path.abspath(p)

# lucide-style icons (24x24, stroke)
IC = {
 'home': '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>',
 'pin': '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 'news': '<rect x="3" y="4" width="15" height="16" rx="2"/><path d="M18 8h3v10a2 2 0 0 1-2 2"/><path d="M7 8h7M7 12h7M7 16h4"/>',
 'phone': '<rect x="7" y="2" width="10" height="20" rx="2.5"/><path d="M11 18h2"/>',
 'check': '<path d="M4 12.5 9.5 18 20 6"/>',
 'zap': '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 'calendar': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 'chart': '<path d="M4 20V10M10 20V4M16 20v-8M22 20H2"/>',
 'cart': '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.5 12h11.5l2-8H6.5"/>',
 'search': '<circle cx="11" cy="11" r="7"/><path d="m21 21-5-5"/>',
 'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18.5 20a6.5 6.5 0 0 0-2-4.7"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 'star': '<path d="m12 3 2.8 5.8 6.2.9-4.5 4.4 1 6.2L12 17.4 6.5 20.3l1-6.2L3 9.7l6.2-.9z"/>',
 'wrench': '<path d="M14.5 6.5a4 4 0 0 0 5 5L21 13l-8 8-3-3 8-8-1.5-1.5a4 4 0 0 1-5-5L8 0"/><path d="M15 3a4 4 0 0 1 6 6l-3-1-2-2z"/>',
 'code': '<path d="m8 7-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/>',
 'truck': '<path d="M2 6h12v10H2zM14 10h4l4 3v3h-8"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/>',
 'box': '<path d="M3 7.5 12 3l9 4.5v9L12 21l-9-4.5z"/><path d="M3 7.5 12 12l9-4.5M12 12v9"/>',
 'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
 'sparkle': '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
 'shield': '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
 'bell': '<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 21h4"/>',
 'file': '<path d="M6 2h8l5 5v15H6z"/><path d="M14 2v5h5M9 13h6M9 17h6"/>',
 'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
 'cpu': '<rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>',
 'pen': '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="m13.5 6.5 4 4"/>',
 'car': '<path d="M5 17H3v-5l2-5h14l2 5v5h-2"/><path d="M3 12h18"/><circle cx="7.5" cy="17" r="2"/><circle cx="16.5" cy="17" r="2"/>',
 'camera': '<path d="M3 8h4l2-3h6l2 3h4v12H3z"/><circle cx="12" cy="13" r="4"/>',
 'refresh': '<path d="M20 11a8 8 0 0 0-14.9-3M4 4v4h4M4 13a8 8 0 0 0 14.9 3M20 20v-4h-4"/>',
 'calc': '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 11h.01M12 11h.01M16 11h.01M8 15h.01M12 15h.01M16 15h.01M8 18h8"/>',
 'puzzle': '<path d="M4 8h4a2 2 0 1 1 4 0h4v4a2 2 0 1 1 0 4v4h-4a2 2 0 1 0-4 0H4v-4a2 2 0 1 0 0-4z"/>',
 'image': '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="m21 16-5-5-8 9"/>',
 'factory': '<path d="M3 21V10l6 4V10l6 4V6h6v15z"/><path d="M7 17h2M12 17h2M17 17h2"/>',
 'wallet': '<rect x="3" y="6" width="18" height="14" rx="2"/><path d="M16 13h2M3 10h18"/>',
 'heart': '<path d="M12 20s-8-4.8-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 9c0 6.2-8 11-8 11z"/>',
}
def icon(name, size=34, color='currentColor', sw=2):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{IC[name]}</svg>'

CSS = f"""
@font-face{{font-family:I;src:url(file://{FONT}Regular.otf);font-weight:400}}
@font-face{{font-family:I;src:url(file://{FONT}Medium.otf);font-weight:500}}
@font-face{{font-family:I;src:url(file://{FONT}SemiBold.otf);font-weight:600}}
@font-face{{font-family:I;src:url(file://{FONT}Bold.otf);font-weight:700}}
@font-face{{font-family:I;src:url(file://{FONT}ExtraBold.otf);font-weight:800}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1080px;background:#060a16;font-family:I,sans-serif;color:#fff;overflow:hidden}}
.s{{position:relative;width:1080px;height:1080px;overflow:hidden;background:#060a16}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.blur{{filter:blur(18px) brightness(.55) saturate(1.1);transform:scale(1.1)}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,10,22,.75) 0%,rgba(6,10,22,0) 22%,rgba(6,10,22,0) 42%,rgba(6,10,22,.88) 72%,rgba(6,10,22,.97) 100%)}}
.shade2{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,10,22,.7) 0%,rgba(6,10,22,.25) 30%,rgba(6,10,22,.25) 60%,rgba(6,10,22,.85) 100%)}}
.glow{{position:absolute;border-radius:50%;filter:blur(120px)}}
.top{{position:absolute;left:56px;right:56px;top:50px;display:flex;justify-content:space-between;align-items:center;z-index:5}}
.top img{{height:46px}}
.pill{{background:#B5D333;color:#060a16;font-weight:700;font-size:20px;letter-spacing:.06em;padding:11px 20px;border-radius:30px;text-transform:uppercase}}
.foot{{position:absolute;left:56px;right:56px;bottom:44px;display:flex;justify-content:space-between;align-items:center;font-size:22px;color:#a0aec0;font-weight:500;z-index:5}}
.foot b{{color:#B5D333;font-weight:700}}
.dots{{display:flex;gap:8px}} .dots i{{width:10px;height:10px;border-radius:5px;background:rgba(255,255,255,.3)}} .dots i.on{{background:#B5D333;width:28px}}
.kick{{color:#B5D333;font-weight:700;font-size:24px;letter-spacing:.12em;text-transform:uppercase;display:flex;align-items:center;gap:12px}}
.kick:before{{content:"";width:44px;height:5px;background:#B5D333;border-radius:3px}}
h1{{font-size:84px;line-height:1.02;font-weight:800;letter-spacing:-.025em}}
h2{{font-size:58px;line-height:1.08;font-weight:800;letter-spacing:-.02em}}
.sub{{font-size:30px;line-height:1.35;color:#d5dce6;font-weight:400}}
.lime{{color:#B5D333}}
.glass{{background:rgba(10,16,36,.72);backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,.12);border-radius:28px}}
.feat{{display:flex;align-items:center;gap:22px;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.08)}}
.feat:last-child{{border-bottom:0}}
.ico{{flex:none;width:68px;height:68px;border-radius:20px;background:rgba(181,211,51,.14);border:1px solid rgba(181,211,51,.4);display:flex;align-items:center;justify-content:center;color:#B5D333}}
.feat .t{{font-size:30px;font-weight:700;line-height:1.15}} .feat .d{{font-size:22px;color:#b7c1cf;margin-top:4px;line-height:1.3}}
.browser{{position:absolute;border-radius:16px;overflow:hidden;background:#0f1633;border:1px solid #2a355a;box-shadow:0 40px 80px rgba(0,0,0,.6)}}
.browser .bar{{height:44px;display:flex;align-items:center;gap:9px;padding:0 18px;background:#141c3d}}
.browser .bar i{{width:13px;height:13px;border-radius:50%}}
.browser .url{{margin-left:16px;flex:1;height:26px;border-radius:13px;background:#0b1130;color:#a0aec0;font-size:17px;display:flex;align-items:center;justify-content:center}}
.browser .vp{{position:absolute;top:44px;left:0;right:0;bottom:0;overflow:hidden}}
.browser .vp img{{width:100%;display:block}}
.phone{{position:absolute;border-radius:46px;background:#0b0f1d;border:2px solid #343f63;padding:12px;box-shadow:0 40px 80px rgba(0,0,0,.65)}}
.phone .scr{{width:100%;height:100%;border-radius:34px;overflow:hidden;position:relative}}
.phone .scr img{{width:100%;display:block}}
.phone .notch{{position:absolute;top:22px;left:50%;transform:translateX(-50%);width:90px;height:24px;border-radius:12px;background:#0b0f1d;z-index:2}}
.ph{{position:absolute;overflow:hidden;border-radius:22px;box-shadow:0 30px 60px rgba(0,0,0,.5)}}
.ph img{{width:100%;height:100%;object-fit:cover;display:block}}
.btn{{display:inline-flex;align-items:center;gap:14px;background:#B5D333;color:#060a16;font-weight:800;font-size:32px;padding:24px 36px;border-radius:20px}}
.chip{{display:inline-flex;align-items:center;gap:10px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);padding:12px 20px;border-radius:30px;font-size:22px;font-weight:600}}
.stat{{font-size:150px;font-weight:800;line-height:1;color:#B5D333;letter-spacing:-.04em}}
"""

def page(body):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s">{body}</div></body></html>'

def chrome(tag, foot, i, n):
    dots = ''.join(f'<i class="{"on" if k==i else ""}"></i>' for k in range(1, n+1))
    return (f'<div class="top"><img src="{LOGO}"><span class="pill">{H.escape(tag)}</span></div>'
            f'<div class="foot"><span>{foot}</span><span class="dots">{dots}</span></div>')

def browser(shot, url, x, y, w, h, pos='top', off=0):
    return (f'<div class="browser" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'<div class="bar"><i style="background:#ff5f57"></i><i style="background:#febc2e"></i><i style="background:#28c840"></i><span class="url">{url}</span></div>'
            f'<div class="vp"><img src="{u(shot)}" style="margin-top:-{off}%"></div></div>')

def phone(shot, x, y, h=620, rot=0, off=0):
    w = int(h * 0.49)
    return (f'<div class="phone" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({rot}deg)">'
            f'<div class="notch"></div><div class="scr"><img src="{u(shot)}" style="margin-top:-{off}%"></div></div>')

# ---------- slide layouts ----------
def s_hero(photo, kicker, title, sub, tag, foot, i, n, extra='', pos='center'):
    return page(f'<img class="bg" src="{u(photo)}" style="object-position:{pos}"><div class="shade"></div>{extra}'
                f'<div style="position:absolute;left:56px;right:56px;bottom:120px;z-index:4">'
                f'<div class="kick">{kicker}</div><h1 style="margin-top:22px">{title}</h1>'
                f'<p class="sub" style="margin-top:20px;max-width:900px">{sub}</p></div>' + chrome(tag, foot, i, n))

def s_features(photo, kicker, title, feats, tag, foot, i, n, pos='center'):
    rows = ''.join(f'<div class="feat"><div class="ico">{icon(ic,36)}</div><div><div class="t">{t}</div>'
                   + (f'<div class="d">{d}</div>' if d else '') + '</div></div>' for ic, t, d in feats)
    return page(f'<img class="bg" src="{u(photo)}" style="object-position:{pos}"><div class="shade2"></div>'
                f'<div style="position:absolute;left:56px;right:56px;top:140px;z-index:4"><div class="kick">{kicker}</div>'
                f'<h2 style="margin-top:18px;text-shadow:0 4px 30px rgba(0,0,0,.6)">{title}</h2></div>'
                f'<div class="glass" style="position:absolute;left:56px;right:56px;bottom:110px;padding:18px 36px;z-index:4">{rows}</div>'
                + chrome(tag, foot, i, n))

def s_mockup(bgphoto, desk, mob, url, kicker, title, tag, foot, i, n, doff=0, moff=0):
    return page(f'<img class="bg blur" src="{u(bgphoto)}">'
                f'<div class="glow" style="width:600px;height:600px;right:-200px;top:-200px;background:rgba(181,211,51,.18)"></div>'
                f'<div style="position:absolute;left:56px;right:56px;top:140px;z-index:4"><div class="kick">{kicker}</div>'
                f'<h2 style="margin-top:18px">{title}</h2></div>'
                + browser(desk, url, 56, 400, 820, 540, off=doff)
                + phone(mob, 730, 430, 560, off=moff)
                + chrome(tag, foot, i, n))

def s_collage(photos, kicker, title, tag, foot, i, n):
    a, b, c = [u(p) for p in photos[:3]]
    return page(f'<div class="glow" style="width:700px;height:700px;right:-250px;top:-300px;background:rgba(20,48,31,.9)"></div>'
                f'<div class="glow" style="width:700px;height:700px;left:-300px;bottom:-300px;background:rgba(12,21,48,.9)"></div>'
                f'<div style="position:absolute;left:56px;right:56px;top:136px;z-index:4"><div class="kick">{kicker}</div>'
                f'<h2 style="margin-top:18px;font-size:52px">{title}</h2></div>'
                f'<div class="ph" style="left:56px;top:390px;width:600px;height:560px"><img src="{a}"></div>'
                f'<div class="ph" style="left:676px;top:390px;width:348px;height:270px"><img src="{b}"></div>'
                f'<div class="ph" style="left:676px;top:680px;width:348px;height:270px"><img src="{c}"></div>'
                + chrome(tag, foot, i, n).replace('bottom:44px', 'bottom:44px'))

def s_cta(photo, title, sub, tag, foot, i, n, btn='Napisz do nas', pos='center', site='piksel360.pl'):
    return page(f'<img class="bg" src="{u(photo)}" style="object-position:{pos}">'
                f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,10,22,.82),rgba(6,10,22,.93))"></div>'
                f'<div class="glow" style="width:700px;height:700px;right:-300px;top:-250px;background:rgba(181,211,51,.16)"></div>'
                f'<div style="position:absolute;left:56px;right:56px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;z-index:4">'
                f'<h2 style="font-size:66px">{title}</h2><p class="sub" style="margin-top:26px;max-width:880px">{sub}</p>'
                f'<div style="margin-top:46px;display:flex;align-items:center;gap:26px"><span class="btn">{btn} {icon("arrow",34,"#060a16",2.6)}</span>'
                f'<span style="font-size:30px;font-weight:700">{site}</span></div></div>'
                + chrome(tag, foot, i, n))

def s_stat(photo, kicker, stat, label, sub, tag, foot, i, n, pos='center'):
    return page(f'<img class="bg" src="{u(photo)}" style="object-position:{pos}"><div class="shade"></div>'
                f'<div style="position:absolute;left:56px;right:56px;bottom:120px;z-index:4"><div class="kick">{kicker}</div>'
                f'<div class="stat" style="margin-top:20px">{stat}</div><h2 style="margin-top:8px;font-size:50px">{label}</h2>'
                f'<p class="sub" style="margin-top:16px">{sub}</p></div>' + chrome(tag, foot, i, n))

def s_split(photo, kicker, title, body, tag, foot, i, n, pos='center', icon_name=None):
    ic = f'<div class="ico" style="margin-bottom:26px">{icon(icon_name,36)}</div>' if icon_name else ''
    return page(f'<div class="ph" style="left:0;top:0;width:1080px;height:560px;border-radius:0"><img src="{u(photo)}" style="object-position:{pos}"></div>'
                f'<div style="position:absolute;left:0;right:0;top:300px;height:270px;background:linear-gradient(180deg,rgba(6,10,22,0),#060a16)"></div>'
                f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,10,22,.6) 0%,rgba(6,10,22,0) 18%)"></div>'
                f'<div style="position:absolute;left:56px;right:56px;top:520px;z-index:4">{ic}<div class="kick">{kicker}</div>'
                f'<h2 style="margin-top:16px;font-size:52px">{title}</h2><p class="sub" style="margin-top:18px;font-size:28px">{body}</p></div>'
                + chrome(tag, foot, i, n))

def render(jobs, outdir):
    """jobs: list of (name, html). Renders to outdir/name.jpg"""
    os.makedirs(outdir, exist_ok=True)
    tmp = HERE / 'html'; tmp.mkdir(exist_ok=True)
    lst = []
    for name, h in jobs:
        p = tmp / (pathlib.Path(outdir).name + '-' + name + '.html'); p.write_text(h)
        lst.append({'html': str(p), 'png': os.path.join(outdir, name + '.png')})
    (HERE / 'jobs.json').write_text(json.dumps(lst))
    subprocess.run(['node', str(HERE / 'render.js'), str(HERE / 'jobs.json')], check=True)
    from PIL import Image
    outs = []
    for j in lst:
        jp = j['png'][:-4] + '.jpg'; Image.open(j['png']).convert('RGB').save(jp, quality=90, optimize=True); os.remove(j['png']); outs.append(jp)
    return outs

def s_screen(bgphoto, shot, url, kicker, title, tag, foot, i, n, off=0):
    return page(f'<img class="bg blur" src="{u(bgphoto)}">'
                f'<div class="glow" style="width:600px;height:600px;right:-200px;top:-200px;background:rgba(181,211,51,.18)"></div>'
                f'<div style="position:absolute;left:56px;right:56px;top:140px;z-index:4"><div class="kick">{kicker}</div>'
                f'<h2 style="margin-top:18px">{title}</h2></div>'
                + browser(shot, url, 56, 420, 968, 540, off=off)
                + chrome(tag, foot, i, n))
