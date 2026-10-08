import json,html,re
src=open('/home/claude/site2/gen5.py').read()
ns={}
exec('import json,html\n'+src[src.index('P=['):src.index('e=html.escape')],ns)
P=ns['P']
exec(src[src.index('svc=['):src.index('SERVICES=')],ns)
exec(src[src.index('steps=['):src.index('STEPS=')],ns)
exec(src[src.index('faqs=['):src.index('FAQ=')],ns)
svc,steps,faqs=ns['svc'],ns['steps'],ns['faqs']
R=json.load(open('reviews.json'))
e=html.escape
CAL='https://calendly.com/joelifeanyichukwu6/20min'
def words(lines):
    o=[];i=0
    for k,ln in enumerate(lines):
        sp=[]
        for w in ln.split(' '):
            hl=w.startswith('*'); w=w.strip('*')
            sp.append('<span%s style="--i:%d">%s</span>'%(' class="hl"' if hl else '',i,e(w)));i+=1
        o.append('<span class="ln">'+' '.join(sp)+'</span>')
    return ''.join(o)
H1=words(['For the communities','people *actually use'])
tools=["Circle.so","Skool","Discord","GoHighLevel","Stripe paywalls","Zapier","Make","Notion","Google Sheets","Automation"]
TOOLS=''.join(f'<span>{e(t)}</span>' for t in tools)
SERVICES=''.join(f'<div class="fc rv" style="--d:{k*.08}s"><span class="n">0{k+1}</span><h3 class="disp">{e(a)}</h3><p>{e(b)}</p><div class="tg">{"".join(f"<i>{e(t)}</i>" for t in c)}</div></div>' for k,(a,b,c) in enumerate(svc))
cards=[]
for k,p in enumerate(P):
    nums=''.join(f'<div><b>{e(n)}</b><span>{e(l)}</span></div>' for n,l in p['stats'])
    cards.append(f'<article class="card c{k%3}" id="p-{p["id"]}" style="--k:{k}"><header><div style="display:flex;align-items:baseline;flex-wrap:wrap"><span class="ix">{k+1:02d}</span><h3>{e(p["name"])} <small>{e(p["plat"])} / {e(p["tag"])}</small></h3></div><button class="pill sm" type="button" data-vid="{p["id"]}">Watch case study</button></header><div class="body"><button class="shot" type="button" data-vid="{p["id"]}" aria-label="Play {e(p["name"])} case study"><img src="img/{p["id"]}-poster.jpg" alt="{e(p["name"])} {e(p["plat"])} community case study video thumbnail" width="1280" height="720" loading="lazy"><span class="play"></span></button><div class="info"><p>{e(p["line"])}</p><div class="nums">{nums}</div></div></div></article>')
CARDS=''.join(cards)
REVIEWS=''.join(f'<figure class="rc rv" style="margin:0"><div class="st" aria-label="5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</div><blockquote>&ldquo;{e(r["t"])}&rdquo;</blockquote><figcaption class="who"><b>{e(r["h"])}</b>Verified Upwork client, {e(r["d"])}</figcaption></figure>' for r in R)
STEPS=''.join(f'<div class="st4 rv" style="--d:{i*.08}s"><div class="no">{i+1:02d}</div><h3 class="disp">{e(a)}</h3><p>{e(b)}</p></div>' for i,(a,b) in enumerate(steps))
offers=[("Start here","Audit",["A look at the structure, members, offer and where people drop off","A written plan in fix order","Scope and timeline agreed in writing"],False),
("Most asked for","Build",["Circle.so, Skool or Discord set up and tested end to end","Roles, paywalls, onboarding and automations","Walkthrough and SOP so your team can run it"],True),
("Ongoing","Manage",["Daily community management on Skool","Posts, replies, recognition and reports","Or take the handover and run it yourself"],False)]
OFFERS=''.join(f'<div class="oc{" feat" if f else ""} rv" style="--d:{i*.08}s"><span class="tag">{e(t)}</span><h3 class="disp">{e(n)}</h3><div class="q">Quote after a short call</div><ul>{"".join(f"<li>{e(x)}</li>" for x in li)}</ul><a class="pill" href="{CAL}" target="_blank" rel="noopener">Book a 20 min call</a></div>' for i,(t,n,li,f) in enumerate(offers))
STICKERS=''.join(f'<div class="stk k{i%5}" role="img" aria-label="{e(t)} sticker">{e(t)}</div>' for i,t in enumerate(tools))
FAQ=''.join(f'<details><summary>{e(q)}</summary><div class="a">{e(a)}</div></details>' for q,a in faqs)
tpl=open('tplK.html').read()
out=(tpl.replace('{{CAL}}',CAL).replace('{{H1}}',H1).replace('{{TOOLS}}',TOOLS).replace('{{SERVICES}}',SERVICES).replace('{{CARDS}}',CARDS).replace('{{REVIEWS}}',REVIEWS)
 .replace('{{STEPS}}',STEPS).replace('{{OFFERS}}',OFFERS).replace('{{STICKERS}}',STICKERS).replace('{{FAQ}}',FAQ).replace('{{DATA}}',json.dumps({p['id']:dict(name=p['name']) for p in P})))
U='https://joelbuildscommunities.space/'
T='Joel | Circle.so, Skool and Discord Community Builder'
D='Joel builds and manages paid communities on Circle.so, Skool and Discord for coaches, creators and brands. Nine case studies with video. Book a free 20 minute call.'
ld=[{"@context":"https://schema.org","@type":"ProfessionalService","name":"Joelbuildscommunities","url":U,"image":U+"og-image.jpg","description":D,"founder":{"@type":"Person","name":"Joel Ifeanyichukwu Nnamani","jobTitle":"Community Builder"},"areaServed":"Worldwide"},
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}]
head=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>{T}</title><meta name="description" content="{D}"><meta name="theme-color" content="#580d14"><meta name="robots" content="noindex,nofollow">
<meta property="og:type" content="website"><meta property="og:title" content="{T}"><meta property="og:description" content="{D}"><meta property="og:image" content="og-image.jpg">
<link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png"><link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preload" as="font" type="font/woff2" href="fonts/anton.woff2" crossorigin><link rel="preload" as="image" href="img/joel-front3.webp">
<script type="application/ld+json">{json.dumps(ld)}</script>'''
i=out.index('<nav')
page=head+out[:i]+'</head><body>'+out[i:]+'</body></html>'
open('index.html','w').write(page)
print(len(page),page.count('—'),'Fasuyi' in page,'[platform]' in page)
open('pageK.html','w').write('<title>Joel Builds Communities Preview</title>\n'+out)
