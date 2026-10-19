import re, json, os
from html.parser import HTMLParser
from playwright.sync_api import sync_playwright
src=open('index.html').read()
# A. tag balance
void={'meta','img','br','link','input','hr'}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.st=[]; s.err=[]
    def handle_starttag(s,t,a):
        if t not in void: s.st.append(t)
    def handle_endtag(s,t):
        if t in void: return
        if s.st and s.st[-1]==t: s.st.pop()
        else: s.err.append((t,s.getpos()))
p=P(); p.feed(src); print('TAG BALANCE: unclosed',p.st,'mismatch',p.err)
# B. links
for m in re.finditer(r'href="([^"]*)"',src): print('LINK',m.group(1))
print('empty hrefs:',len(re.findall(r'href=""',src)),' js:',bool(re.search(r'<script|onclick',src,re.I)))
# C. images
for m in re.finditer(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"',src):
    f='assets/'+m.group(1).split('/')[-1]; print('IMG',f,os.path.exists(f),'alt:',bool(m.group(2)))
with sync_playwright() as pw:
    b=pw.chromium.launch()
    for w in (600,390,375,320):
        pg=b.new_page(viewport={'width':w,'height':900}); pg.goto('file://'+os.path.abspath('preview-local.html'))
        r=pg.evaluate('''()=>{const c=document.querySelector('table.container').getBoundingClientRect();
        const imgs=[...document.images].map(i=>({s:i.src.split('/').pop(),nw:i.naturalWidth,nh:i.naturalHeight,w:Math.round(i.getBoundingClientRect().width),h:Math.round(i.getBoundingClientRect().height)}));
        const a=[...document.querySelectorAll('a')].find(a=>a.textContent.trim()=='SCHEDULE A TOUR').getBoundingClientRect();
        return {sw:document.documentElement.scrollWidth,cw:Math.round(c.width),imgs,btn:[Math.round(a.width),Math.round(a.height)],fs:getComputedStyle(document.querySelector('p')).fontSize}}''')
        print('VIEW',w,'scrollW',r['sw'],'container',r['cw'],'btn',r['btn'],'body font',r['fs'])
        for i in r['imgs']: print('   ',i,'ratio_nat',round(i['nw']/i['nh'],3),'ratio_disp',round(i['w']/i['h'],3))
        if w in (600,390): pg.screenshot(path={600:'preview-desktop.png',390:'preview-mobile.png'}[w],full_page=True)
    b.close()
