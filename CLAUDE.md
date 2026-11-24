# Site Buffet Ize

Site do **Buffet Ize** (buffet, restaurante e rotisseria), empresa familiar desde 1995, em Jaboticabal, SP.
O cliente escreve em português (muitas vezes em CAIXA ALTA). Responda em português, em linguagem simples.

- **Site oficial:** https://buffetize.com.br (GitHub Pages, repositório `vistoque88-creator/buffetize`, branch `main`).
  **Este repositório é a fonte oficial do site.** Cada push na `main` publica em 1–2 minutos.
- **Prévia (artifact do Claude, privado):** https://claude.ai/artifact/4Ezd1wAsnGdjMkn1abVcBZ
  Usar para mostrar mudanças maiores antes de enviar ao site. Sempre republicar nesse mesmo link
  (passar `url` com esse link, porque o arquivo agora está em outro caminho).
- Backup extra no Google Drive do cliente (pasta "Site Buffet Ize - backup").

## Arquivos (raiz do repositório)

| Caminho | O que é |
|---|---|
| `fonte/pagina.html` | **Fonte da página.** Editar sempre aqui. |
| `fonte/montar.py` | Gera `index.html` (site, com SEO/Open Graph) e `fonte/artifact.html` (prévia). Rodar após cada edição: `python3 fonte/montar.py` |
| `index.html` | O site publicado. Não editar à mão. |
| `cardapio.json` | **Cardápio do dia das marmitas** (lido pela página via fetch). |
| `img/` | logo.png, compartilhar.jpg (prévia no WhatsApp), fotos de eventos (Unsplash, ilustrativas) e `img/marmitas/<id>.jpg`. |
| `CNAME` | buffetize.com.br |
| `_config.yml` | Faz o GitHub Pages não publicar CLAUDE.md, fonte/ e README.md. |

Enviar ao ar: `git add -A && git commit -m "..." && git push origin main`.
Prévia: `Artifact` com `url` = link da prévia, `file_path: <repo>/fonte/artifact.html` e, quando mudar arquivos
de apoio, `files: {"cardapio.json": "<repo>/cardapio.json", "img/x.jpg": "<repo>/img/x.jpg"}`.

## Domínio buffetize.com.br

- Registrado pelo cliente no Registro.br (21/11/2026), em nome da empresa.
- DNS no Registro.br: registros A do domínio → 185.199.108.153, 185.199.109.153, 185.199.110.153,
  185.199.111.153; AAAA → 2606:50c0:8000::153, 2606:50c0:8001::153, 2606:50c0:8002::153, 2606:50c0:8003::153;
  `www` CNAME → vistoque88-creator.github.io. Depois ativar "Enforce HTTPS" no GitHub (Settings → Pages).

## Comando diário: "ATUALIZAR MARMITAS"

O cliente anexa um Word com o cardápio do dia e manda só "ATUALIZAR MARMITAS". Fazer:
1. Ler o .docx (pandoc ou python-docx).
2. Reescrever `cardapio.json` neste formato (manter `exemplo: false`):
   ```json
   {"atualizado":"DD/MM/AAAA","exemplo":false,
    "bases":["Arroz branco","Arroz integral","Feijão carioca","Macarrão parisiense"],
    "basesPadrao":["Arroz branco","Feijão carioca"],
    "carnes":[{"nome":"Frango assado","tipo":"branca"},{"nome":"Carne de panela","tipo":"vermelha"}],
    "acompanhamentos":["Farofa"],
    "saladas":["Salada verde"]}
   ```
   - `tipo`: frango/peixe/aves = "branca"; boi/porco/linguiça = "vermelha" (importa nas marmitas de R$110 e R$160).
   - O Word traz vários dias (um por página) com o cardápio do restaurante e um bloco "MARMITAS".
     Usar o dia de hoje (ou a página que o cliente indicar) e só o bloco MARMITAS. O nº de linhas varia:
     - 5 linhas (24/11): carnes / acompanhamentos / feijão e massa / arrozes / saladas.
     - 4 linhas (21/11): carnes e acompanhamentos juntos na 1ª / feijão e massa / arrozes / saladas.
     Itens que não são carne mas vêm na linha das carnes (ex.: salgadinhos) entram em `carnes` com `tipo: ""`.
   - Bases = arrozes + feijão + massa do dia; `basesPadrao` = o que já vem marcado (1º arroz + feijão).
3. Commit + push na `main` (vai direto para buffetize.com.br). Opcional: atualizar também a prévia.
4. Responder curto: o que entrou no cardápio + link do site.

## Regras de negócio (já implementadas)

**WhatsApp:** principal (16) 3204-3321 → `551632043321` (orçamentos, marmitas, encomendas por quilo).
Fim de ano (16) 3202-3260 → `551632023260`.
Todos os formulários montam a mensagem e abrem `https://wa.me/<num>?text=...`.

**Orçamento de eventos:** nome, telefone, tipo de evento (lista), nº de convidados, data prevista.

**Marmitas (valores a partir de 01/12/2026; descrições conforme folheto enviado em 20/11):**
- Individuais (todos os dias): R$20 (500 ml, 1 carne, 1 acomp.); R$28 (800 ml, 2 carnes, 1 acomp.); R$32 (800 ml, 2 carnes, 1 acomp. + salada).
- 2 a 3 pessoas: R$68 (pote 500 ml, 2 carnes, acomp., salada); R$72 somente mistura SEM bases (2 carnes, acomp., salada; 2 potes redondos 800 ml + 1 hamburgueira); R$75 (2 carnes, acomp., salada).
- 4 a 5 pessoas: R$88 (1 carne); R$110 (2 carnes).
- Até 7 pessoas: R$160 (2 arroz, 1 feijão ou massa, 3 carnes).
- Folheto não exige mais carne branca + vermelha (flag `mista` removida dos tamanhos).
- Fotos de cada tamanho em `img/marmitas/<id>.jpg`, recortadas do folheto (f72 é montagem: hamburgueira+redonda e redonda).
- Embalagem adicional R$5; salada adicional R$4 (cliente escolhe o sabor de cada salada extra).
- Obrigatório escolher ao menos 1 item base (arroz/feijão/massa), exceto "somente mistura".
- Segunda a sábado: todas. **Domingos e feriados: só individuais** (calendário automático).
- **Horário para fazer pedidos (Brasília, `HORARIO_PEDIDOS`):** seg–sáb 8h–13h30; domingos e feriados 8h–13h.
  Fora disso a área de pedidos fica bloqueada (marmitas e bebidas) com aviso. Pedidos só para o próprio dia
  (o seletor de data foi removido em 23/11). Hora calculada em America/Sao_Paulo, não no relógio do aparelho.
- **Bebidas (`BEBIDAS`, passo 4):** suco natural 300 ml R$8 (laranja; laranja e morango; laranja, abacaxi e hortelã;
  verde detox; acerola); refrigerante lata R$8 (Coca-Cola, Coca Zero, Guaraná Antarctica, Guaraná Zero, Sprite,
  Fanta Laranja, Fanta Uva, água tônica, tônica zero); água com/sem gás R$5; refrigerante 600 ml R$10 e 2 L R$16
  (Coca, Coca Zero, Guaraná, Guaraná Zero); H2O limão/limoneto R$9; Jaboti 250 ml R$3; Jaboti 2 L R$8.
  Outras bebidas: cliente escreve em "Informações adicionais". Pedido exige ao menos 1 marmita.
- Entrega R$8 (endereço obrigatório) ou retirada. Horário entre 11h e 14h.
- Pagamento: crédito, débito, dinheiro (pergunta troco), PIX chave CNPJ **40.360.468/0001-01** (pedir comprovante).
- Cada tamanho aceita `foto` (caminho em `img/marmitas/`); aparece no cartão e no passo 3 quando selecionada.

**Feriados:** nacionais calculados (inclui Sexta-feira Santa e Corpus Christi pela Páscoa, 20/11) + 09/07 (SP).
Municipais de Jaboticabal: ainda não informados → `FERIADOS_EXTRAS`.
**Dias fechados:** cliente avisa → incluir em `DIAS_FECHADOS` ({data:"AAAA-MM-DD", motivo:"..."}); bloqueia pedidos e mostra "fechado".

**Restaurante:** todos os dias 11h–14h. Self-service por kg: seg–sex R$84,90; sábados e feriados R$98,90; domingos R$101,90.
Prato feito R$40 e à vontade R$70 (seg–sex, exceto feriados). Quadro "Hoje" calcula o preço do dia.
Também temos: pães, roscas, sequilhos, sobremesas, sopas, caldos, massas, molhos, salgados para eventos e muito mais.
(Assumido que os valores do self-service são por quilo; cliente não contestou.)

**Encomendas:** avulsas por quilo (WhatsApp principal); fim de ano (WhatsApp fim de ano) + link do PDF
"Cardápio Fim de Ano 2026" no Drive: https://drive.google.com/file/d/1BhBRwXU1snN-zgU8mXF0DH6hGjGFsReS/view
(Natal até 15/12, Réveillon até 26/12).
No topo (hero) há o botão vermelho "Pedidos de fim de ano" → WhatsApp fim de ano, com prazos e link do cardápio (temporada; retirar depois do Réveillon se o cliente pedir).

**Endereços (botões de rota Google Maps e Waze):**
- Restaurante: Rua Francisco Ferrari, 171, Jardim Morumbi, Jaboticabal - SP
- Escritório comercial: Rua Coronel Odilon Ortiz, 60, Nova Jaboticabal, Jaboticabal - SP

**Linha do tempo:** fundação 1995; anos de casa calculados automaticamente (31 em 2026).
Marcos 2005/2015/2025 são textos genéricos — trocar quando o cliente mandar fatos reais.

**Instagram:** @buffetize_ (não dá para baixar fotos de lá automaticamente; pedir fotos como anexo).

## Visual

Cores da logo: marrom chocolate + dourado + marfim. Fontes: Cormorant Garamond (títulos), Jost (texto),
Pinyon Script (detalhes cursivos). Seções: topo com carrossel → Nossa história → Restaurante → Eventos →
Orçamento → Marmitas → Encomendas → Localização → Rodapé. Botão flutuante de WhatsApp.

## Pendências

- Fotos reais dos eventos; feriados municipais; fatos da história.
- Ligar buffetize.com.br: cliente ativar GitHub Pages (se ainda não estiver) e preencher o DNS no Registro.br.

## Cuidados técnicos

- Imagens coladas no chat às vezes não viram arquivo; procurar em `/tmp/claude-0/.../images/` ou pedir anexo.
- Rede: images.unsplash.com foi liberado no ambiente; Instagram bloqueia acesso automático.
- O artifact bloqueia iframes (sem mapa embutido) e `window.open` pode falhar: o site mostra o botão "Abrir WhatsApp" como alternativa.
