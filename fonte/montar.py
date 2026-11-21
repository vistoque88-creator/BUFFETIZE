"""Gera index.html (site) na raiz e fonte/artifact.html (prévia no Claude) a partir de fonte/pagina.html."""
import pathlib
fonte = pathlib.Path(__file__).parent
raiz = fonte.parent
SITE = 'https://buffetize.com.br/'
SEO = f'''<link rel="canonical" href="{SITE}">
<link rel="icon" type="image/png" href="img/logo.png">
<link rel="apple-touch-icon" href="img/logo.png">
<meta name="theme-color" content="#2a170f">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Buffet Ize">
<meta property="og:title" content="Buffet Ize · Buffet, restaurante e rotisseria em Jaboticabal">
<meta property="og:description" content="Empresa familiar desde 1995. Eventos, restaurante todos os dias das 11h às 14h e marmitas com pedido pelo WhatsApp.">
<meta property="og:url" content="{SITE}">
<meta property="og:image" content="{SITE}img/compartilhar.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
'''
frag = (fonte / 'pagina.html').read_text()
(fonte / 'artifact.html').write_text(frag)
head, rest = frag.split('<style>', 1)
style, body = rest.split('</style>', 1)
full = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', SEO)
        + '<style>' + style + '</style>\n</head>\n<body>' + body + '\n</body>\n</html>\n')
(raiz / 'index.html').write_text(full)
print('ok: index.html e fonte/artifact.html')
