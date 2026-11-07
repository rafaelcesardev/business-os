# Imagens geradas e composição em HTML

Combine imagens geradas com HTML/CSS para posicionar texto, alternar planos e aplicar máscaras e sobreposições. A copy permanece editável. Materiais, intensidade visual e efeitos seguem a identidade e o pedido do negócio.

## Distribuir o trabalho

Decida elemento por elemento, antes de produzir, o que é HTML e o que é imagem gerada. A peça não é "uma imagem com um texto colado ao lado": texto e imagem são planos de uma mesma composição.

| Elemento | Onde fazer | Por quê |
| --- | --- | --- |
| Texto padrão, sem efeito: títulos, apoio, CTA, numeração, rodapé | HTML | Copy exata, acentos corretos, editável, fonte da marca |
| Logo oficial | HTML, arquivo da marca | Não se redesenha a marca |
| Fundo liso ou com textura sutil (branco, preto, cinza da marca) | HTML ou imagem simples | Controle de cor e respiro |
| Objeto principal, cena, material, luz, reflexo, sombra no chão | Imagem gerada | Volume e realismo que CSS não produz |
| Objeto que fica na frente do texto, cobrindo parte dele | Imagem gerada em recorte com transparência real, acima da camada de texto | Dá profundidade sem perder o texto editável |
| Texto com efeito material: vidro, metal, neon, gelo, relevo, texto impresso ou gravado na superfície de um objeto, texto deformado pela perspectiva | Imagem gerada, com a frase exata no prompt | O efeito depende de luz e material; em HTML fica falso |
| Palavra gigante de fundo que o objeto atravessa | HTML (tipografia da marca) atrás do recorte; imagem gerada só se a palavra precisar de efeito material | Recurso pontual, não padrão: no máximo uma peça da série, e só se a palavra continuar legível com o objeto na frente |

Regras:

- Mínimo de elementos. Uma ideia, um objeto principal, fundo limpo. O que distrai sai.
- Sobreposição não pode apagar a leitura: se o objeto cobre tanto a palavra que não dá para entender o que está escrito, reduza a sobreposição ou tire a palavra.
- Texto gerado em imagem: copie a frase literal, curta, no prompt; abra o resultado e confira letra por letra, acentos inclusos. Se errar, gere de novo ou passe esse texto para HTML.
- Para sobreposição (objeto à frente de parte do texto), gere o objeto já pensando no espaço do texto: posição, escala e área livre descritas no prompt, e recorte com transparência.
- Exportação: navegador renderiza cada slide na dimensão final e salva o PNG. O HTML e os arquivos de imagem permanecem como fonte editável.

O efeito tridimensional pode vir de uma imagem com volume e de como ela se relaciona com as outras camadas; não exige criar um motor 3D.

## Planejar os planos

Defina o que fica no fundo, atrás do texto, no mesmo plano e na frente. Use posicionamento e ordem de empilhamento explícitos.

Para texto parcialmente atrás de um objeto, mantenha o texto em uma camada inferior e o recorte transparente na superior. Para mostrar partes de um elemento à frente e outras atrás, use camadas coerentes, recortes ou máscaras; um PNG com fundo opaco não passa a ser recorte apenas por mudar sua ordem.

Use `mask-image`, `clip-path` ou opacidade para apagados e revelações quando contribuírem para a ideia. Preserve a leitura de palavras, acentos, CTA e logo; uma palavra pode participar da composição sem perder seu sentido.

Sombras, gradientes e desfoque precisam combinar com a iluminação e o foco da imagem. Não distribuir efeitos por todas as camadas apenas para demonstrar o recurso.

O formato dos cantos e das bordas segue a identidade da empresa. Ajuste pela escala do elemento e mantenha consistência entre blocos equivalentes da peça; uma preferência de um cliente não é padrão universal.

## Arquivos da peça

Reutilize a pasta da copy. Um `carrossel.html` reúne os slides, cada um como uma área independente. Salve as imagens, logos e fontes necessários em `assets/`, mantendo caminhos relativos.

Use fontes locais quando disponíveis, para a exportação não depender de uma chamada externa. Reaproveite o navegador e as bibliotecas já instalados. Um renderizador pequeno basta; não crie uma aplicação ou instale um conjunto de dependências para compor uma sequência de imagens.

Salve `render.js` quando ele for necessário para reproduzir a exportação. O script precisa aguardar fontes e imagens, conferir que os recursos carregaram e parar diante de falha de renderização, em vez de entregar um PNG incompleto.

Nos carrosséis de feed deste fluxo, use 1080 × 1350, salvo pedido diferente. Numere os PNGs conforme o README do repositório e preserve a legenda.

## Conferência

Abra os PNGs renderizados e veja a série em conjunto e as páginas em tamanho de celular. Confira cortes, acentos, legibilidade, ordem das páginas e o vínculo entre imagem e mensagem. Verifique áreas de texto e imagens que escapem do quadro sem intenção.

Um apagado decorativo não deve apagar a informação que o leitor precisa. O HTML também deve conter o texto completo e uma descrição útil das imagens.

Para vídeo, os mesmos arquivos podem servir de base a uma composição animada. A geração do carrossel não comprova que a versão em movimento foi renderizada ou testada.
