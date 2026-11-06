# Imagens geradas e composição em HTML

Combine imagens geradas com HTML/CSS para posicionar texto, alternar planos e aplicar máscaras e sobreposições. A copy permanece editável. Materiais, intensidade visual e efeitos seguem a identidade e o pedido do negócio.

## Distribuir o trabalho

- Geração de imagem: objetos, recortes, cenas, material, iluminação e detalhes fotográficos. Pedir sem títulos, legendas, marcas ou interfaces fictícias.
- HTML/CSS: copy exata, tipografia, cores da marca, logo oficial, posição, escala, sombra de composição, desfoque, máscaras e ordem dos planos.
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
