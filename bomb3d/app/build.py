#!/usr/bin/env python3
"""Build the offline app version of Bomb 3D Simulator into app/www/.

Run it again after every change to ../index.html:  python3 build.py
It swaps the internet links (3D engine, fonts) for the copies in vendor/,
and wraps the page in a full HTML document for the iPhone/iPad app.
"""
import os, re, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'index.html')
WWW = os.path.join(HERE, 'www')

src = open(SRC, encoding='utf-8').read()
title = re.search(r'<title>(.*?)</title>', src).group(1)
src = re.sub(r'<title>.*?</title>\n', '', src, count=1)
src = src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
# fonts: local files instead of Google Fonts
src = re.sub(r'<link rel="preconnect"[^>]*>\n', '', src)
src = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^"]*">\n', '<link rel="stylesheet" href="fonts/fonts.css">\n', src)
# 3D engine: local files instead of the CDN
src = src.replace('https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js', 'lib/three.min.js')
src = re.sub(r'https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/(?:shaders|postprocessing)/', 'lib/', src)
assert 'https://cdn' not in src and 'fonts.googleapis' not in src, 'an internet link is left'

head = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#ff7a1a">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="manifest" href="manifest.webmanifest">
<title>{title}</title>
<style>:root{{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}html,body{{margin:0;height:100%;overscroll-behavior:none;-webkit-user-select:none;user-select:none;-webkit-touch-callout:none;-webkit-tap-highlight-color:transparent}}body{{font:14px system-ui,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
'''
out = head + src + '\n</body>\n</html>\n'

if os.path.exists(WWW): shutil.rmtree(WWW)
os.makedirs(os.path.join(WWW, 'lib')); os.makedirs(os.path.join(WWW, 'fonts'))
for f in os.listdir(os.path.join(HERE, 'vendor', 'three')): shutil.copy(os.path.join(HERE, 'vendor', 'three', f), os.path.join(WWW, 'lib', f))
faces = ''
for f in sorted(os.listdir(os.path.join(HERE, 'vendor', 'fonts'))):
    shutil.copy(os.path.join(HERE, 'vendor', 'fonts', f), os.path.join(WWW, 'fonts', f))
    if f.startswith('Fredoka-'): faces += f"@font-face{{font-family:'Fredoka';font-weight:{f[8:11]};font-display:swap;src:url('{f}') format('truetype')}}\n"
    elif f.startswith('LuckiestGuy'): faces += f"@font-face{{font-family:'Luckiest Guy';font-weight:400;font-display:swap;src:url('{f}') format('truetype')}}\n"
open(os.path.join(WWW, 'fonts', 'fonts.css'), 'w').write(faces)
for f in os.listdir(os.path.join(HERE, 'assets')):
    if f.startswith('icon-') and f.endswith('.png'): shutil.copy(os.path.join(HERE, 'assets', f), os.path.join(WWW, f))
open(os.path.join(WWW, 'manifest.webmanifest'), 'w').write('{"name":"Bomb 3D Simulator","short_name":"Bomb 3D","display":"fullscreen","orientation":"any","background_color":"#ff7a1a","theme_color":"#ff7a1a","start_url":"index.html","icons":[{"src":"icon-512.png","sizes":"512x512","type":"image/png"},{"src":"icon-1024.png","sizes":"1024x1024","type":"image/png"}]}')
open(os.path.join(WWW, 'index.html'), 'w', encoding='utf-8').write(out)
print('built', os.path.relpath(WWW), len(out) // 1024, 'KB')
