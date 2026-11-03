import sys,glob
from PIL import Image
T='/root/.claude/projects/-home-claude-piksel360-social/9a00c5b1-7828-5d6a-9040-e8701c1a6c3e/tool-results/'
K=1568/1920
def f(id): return Image.open(glob.glob(T+'*'+id+'.jpg')[0]).convert('RGB')
def one(id,wcss,hcss,out):
    w=round(wcss*K); h=min(758,round(hcss*K)); f(id).crop((0,0,w,h)).save('photos/'+out,quality=95)
def two(id1,id2,wcss,hcss,out):
    w=round(wcss*K); H=round(hcss*K); off=round((hcss-928)*K)
    im=Image.new('RGB',(w,H)); im.paste(f(id1).crop((0,0,w,758)),(0,0))
    a=f(id2).crop((0,758-(H-758),w,758)); im.paste(a,(0,758)); im.save('photos/'+out,quality=95)
