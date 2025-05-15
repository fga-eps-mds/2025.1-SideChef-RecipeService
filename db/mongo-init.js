// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
db = db.getSiblingDB('RecipeService');

db.createCollection('recipes')

// Create a new document in the collection.
db.getCollection('recipes').insertMany(
    [
        {
            "Nome": "Brigadeiro",
            "Tipo": "Doce",
            "Dificuldade": "F\u00e1cil",
            "Ingredientes": "\u2022 1 caixa de leite condensado\n\u2022 1 colher (sopa) de margarina sem sal\n\u2022 7 colheres (sopa) de achocolatado ou 4 colheres (sopa) de chocolate em p\u00f3\n\u2022 chocolate granulado\n  ",
            "Modo de Preparo": "Rende 30 por\u00e7\u00f5es:\n1. Em uma panela funda, acrescente o leite condensado, a margarina e o chocolate em p\u00f3.\n\n2. Cozinhe em fogo m\u00e9dio e mexa at\u00e9 que o brigadeiro comece a desgrudar da panela.\n\n3. Deixe esfriar e fa\u00e7a pequenas bolas com a m\u00e3o passando a massa no chocolate granulado."
        },
        {
            "Nome": "Bolo de Caneca",
            "Tipo": "Doce",
            "Dificuldade": "F\u00e1cil",
            "Ingredientes": " Massa:\n\u2022 1 ovo\n\u2022 2 colheres (sopa) de achocolatado em p\u00f3\n\u2022 3 colheres (sopa) rasas de a\u00e7\u00facar\n\u2022 4 colheres (sopa) rasas de farinha de trigo\n\u2022 1 colher (sopa) de \u00f3leo\n\u2022 fermento em p\u00f3 qu\u00edmico\n\u2022 1 colher (caf\u00e9) rasa de fermento em p\u00f3\n\u2022 4 colheres (sopa) de leite\n\nCalda:\n\u2022 2 colheres (sopa) de achocolatado em p\u00f3\n\u2022 1 colher (sopa) de margarina\n\u2022 1\/2 x\u00edcara de leite",
            "Modo de Preparo": "Rende 1 por\u00e7\u00e3o:\n1. Coloque todos os ingredientes dentro de uma caneca de aproximadamente 300 ml ou mais.\n\n2. Mexa at\u00e9 obter uma massa homog\u00eanea e leve ao micro-ondas por 3 minutos.\n\nCalda:\n\n1. Coloque todos os ingredientes em uma panela, leve ao fogo m\u00e9dio e misture at\u00e9 obter uma consist\u00eancia grossa.\n\n2. Despeje a calda sobre o bolo assim que retir\u00e1-lo do microondas."
        },
        {
            "Nome": "Mousse de Maracuj\u00e1",
            "Tipo": "Doce",
            "Dificuldade": "F\u00e1cil",
            "Ingredientes": "\u2022 1 lata de leite condensado\n\u2022 1 lata de suco de maracuj\u00e1 (medida pela lata de leite condensado)\n\u2022 1 lata de creme de leite sem soro",
            "Modo de Preparo": "Rende 6 por\u00e7\u00f5es:\n1. Em um liquidificador, bata o creme de leite, o leite condensado e o suco concentrado de maracuj\u00e1.\n\n2. Em uma tigela, despeje a mistura e leve \u00e0 geladeira por, no m\u00ednimo, 4 horas."
        },
        {
            "Nome": "Banana Caramelada",
            "Tipo": "Doce",
            "Dificuldade": "F\u00e1cil",
            "Ingredientes": "\u2022 6 bananas maduras (de prefer\u00eancia banana nanica\/prata)\n\u2022 1 x\u00edcara (caf\u00e9) de a\u00e7\u00facar mascavo ou cristal\n\u2022  canela em lasca a gosto",
            "Modo de Preparo": "Rende 4 por\u00e7\u00f5es:\n1. Corte as bananas do tamanho que desejar.\n\n2. Despeje o a\u00e7\u00facar em uma panela m\u00e9dia junto com as bananas.\n\n3. Mexa vagarosamente em fogo m\u00e9dio com uma colher para n\u00e3o desmanchar as banana.\n\n4. Espere o a\u00e7\u00facar chegar no ponto de caramelo(quando estiver derretendo) e desligue o fogo.\n\n5. Coloque as lascas de canela ao gosto.\n\n6. Sirva em uma bandeja de vidro e espere a banana esfriar."
        },
        {
            "Nome": "Pav\u00ea de Bolacha",
            "Tipo": "Doce",
            "Dificuldade": "F\u00e1cil",
            "Ingredientes": "Recheio:\n\n\u2022 3 pacotes de bolacha maizena\n\u2022 1 lata de leite condensado\n\u2022 2 latas de leite (medida da lata de leite condensado)\n\u2022 2 colheres de amido de milho\n\u2022 200 g de coco ralado\n\u2022 2 gemas\n\nCobertura:\n \u2022 1 lata de creme de leite\n \u2022 2 claras\n \u2022 1 x\u00edcara de a\u00e7\u00facar",
            "Modo de Preparo": "Rende 25 por\u00e7\u00f5es\n1. Leve ao fogo o leite condensado, o leite, as gemas e o amido j\u00e1 dissolvido (pode ser em um pouquinho de \u00e1gua).\n\n2. Mexa at\u00e9 engrossar, o segredo \u00e9 n\u00e3o deixar ficar muito grosso, pois as bolachas n\u00e3o precisar\u00e3o ser molhadas.\n\n3. Quando estiver meio grosso, coloque o coco ralado e deixe mais 5 minutos, desligue.\n\nCobertura:\n1. Bata as claras, junte o creme de leite, o a\u00e7\u00facar e mexa, reserve.\n\n2. Em um refrat\u00e1rio, coloque uma camada de recheio, outra de biscoito e quando as camadas completarem o refrat\u00e1rio, adicione a cobertura.\n\n3.Leve \u00e0 geladeira at\u00e9 ficar gelado.."
        },
        {
            "Nome": "Torta de Lim\u00e3o",
            "Tipo": "Doce",
            "Dificuldade": "M\u00e9dia",
            "Ingredientes": "Massa:\n\u2022 200 g de biscoito de maisena\n\u2022 150 g de margarina\n\nRecheio\n\n\u2022 1 lata de leite condensado (395 g)\n\u2022 1 caixa de creme de leite (200 g)\n\u2022 suco de 4 lim\u00f5es\n\u2022 raspas de 2 lim\u00f5es\n\nCobertura:\n\u2022 3 ou 4 claras de ovo\n\u2022 3 colheres (sopa) de a\u00e7\u00facar\n\u2022 raspas de 2 lim\u00f5es para decorar",
            "Modo de Preparo": "Rende 15 por\u00e7\u00f5es:\n\nMassa:\n\n1 .Triture o biscoito de maisena em um liquidificador ou processador.\n\n2. Junte a margarina e bata mais um pouco.\n\n3. Despeje a massa em uma forma de fundo remov\u00edvel (27 cm de di\u00e2metro).\n\n4. Com as m\u00e3os, espalhe os biscoitos triturados no fundo e nas laterais da forma, cobrindo toda \u00e1rea de maneira uniforme.\n\n5. Leve ao forno m\u00e9dio (180\u00b0 C), preaquecido, por aproximadamente 10 minutos.\n\nRecheio:\n\n6. Bata todos os ingredientes no liquidificador at\u00e9 obter um creme liso e firme.\n\n7. Recheie a massa j\u00e1 assada e leve \u00e0 geladeira por 30 minutos.\n\nCobertura:\n\n1. Bata as claras em neve e acrescente o a\u00e7\u00facar.\n\n2. Misture at\u00e9 obter um ponto de suspiro e leve ao forno at\u00e9 dourar.\n\n3. Desenforme a torta (sem retirar o fundo falso)."
        },
        {
            "Nome": "Churros Caseiros",
            "Tipo": "Doce",
            "Dificuldade": "M\u00e9dia",
            "Ingredientes": "\u2022 1 e 1\/2 x\u00edcara (ch\u00e1) de leite\n\u2022 1\/2 x\u00edcara (ch\u00e1) de \u00e1gua\n\u2022 2 colheres (sopa) de margarina ou manteiga\n\u2022 2 x\u00edcaras (ch\u00e1) de farinha de trigo\n\u2022 sal a gosto\n\u2022 a\u00e7\u00facar a gosto\n\u2022 canela a gosto",
            "Modo de Preparo": "Rende 20 por\u00e7\u00f5es\n1.Em uma panela, adicione o leite, a \u00e1gua, a manteiga e o sal.\n\n2. Quando o leite ferver, adicione a farinha de trigo e mexa r\u00e1pido at\u00e9 a massa soltar do fundo da panela.\n\n3. Coloque a massa em um saco de confeiteiro com o bico pitanga, depois fa\u00e7a tirinhas com a massa e frite.\n\n4. Misture a canela e o a\u00e7\u00facar, depois passe nos churros fritos."
        },
        {
            "Nome": "Bolo Red Velvet",
            "Tipo": "Doce",
            "Dificuldade": "M\u00e9dia",
            "Ingredientes": "Massa:\n\u2022 2 ovos\n\u2022 100 g de manteiga sem sal amolecida\n\u2022 1 colher (sopa) de vinagre branco\n\u2022 1 colher (ch\u00e1) de ess\u00eancia de baunilha\n\u2022 4 colheres de corante aliment\u00edcio l\u00edquido cor vermelha\n\u2022 5 colheres (sopa) de suco de lim\u00e3o\n\u2022 3 x\u00edcaras (ch\u00e1) farinha de trigo\n\u2022 2 x\u00edcaras(ch\u00e1) de a\u00e7\u00facar refinado\n\u2022 1 colher (sopa) de cacau em p\u00f3 (N\u00e3o pode ser achocolatado)\n\u2022 1 colher (ch\u00e1) de sal\n\u2022 1 colher (sopa) de bicarbonato de s\u00f3dio\n\u2022 1 colher (sopa) de fermento em p\u00f3\n\u2022 200 ml de leite integral\n\u2022 1 colher (sopa) de suco de lim\u00e3o\n\nCobertura e recheio:\n\n\u2022 100 g de manteiga sem sal amolecida\n\u2022 300 g de cream cheese\n\u2022 200 g de chocolate branco derretido\n\u2022 300 g de a\u00e7\u00facar de confeiteiro\n\u2022 1 colher (sopa) ess\u00eancia de baunilha\n\u2022 100 g de nozes triturada\n\u2022 50 g de nozes n\u00e3o triturada",
            "Modo de Preparo": "Rende 8 por\u00e7\u00f5es:\n\nMassa:\n\n1. Misture 200 ml de leite com 1 colher (sopa) de suco de lim\u00e3o e reserve por 10 minutos.\n\n2. Em uma tigela, misture a farinha de trigo, a\u00e7\u00facar refinado, cacau em p\u00f3, sal, bicarbonato de s\u00f3dio, fermento em p\u00f3 at\u00e9 ficar homog\u00eaneo e reserve.\n\n3. Na batedeira em velocidade m\u00e9dia, bata por 10 minutos a manteiga, ovos, vinagre branco, ess\u00eancia de baunilha, corante aliment\u00edcio vermelho, 05 colheres de suco de lim\u00e3o.\n\n4. Ainda na batedeira, intercale a mistura seca e o leite, adicionando-os \u00e0 massa formada e bata por mais 5 minutos at\u00e9 formar uma massa bem cremosa.\n\n5. Em forno preaquecido a 180\u00baC, unte 2 tabuleiros redondos de 20 cm de di\u00e2metro, divida a massa entre os 2 tabuleiros e asse por aproximadamente 20 a 40 minutos. Ap\u00f3s 20 minutos, verifique se a massa est\u00e1 assada, perfurando o bolo com uma faca, se a mesma sair limpa, a massa estar\u00e1 pronta. Quando a massa estiver pronta, retire do forno e deixe esfriar antes de desenformar.\n\nRecheio e cobertura:\n\n1. Na batedeira em velocidade m\u00e9dia, bata por 10 minutos a manteiga sem sal amolecida, cream cheese, chocolate branco derretido, a\u00e7\u00facar de confeiteiro, ess\u00eancia de baunilha e nozes triturada.\n\n2. Quando formar uma mistura bem fofa e cremosa, reserve.\n\nMontagem:\n\n1. Desenforme os bolos e corte-os ao meio formando 4 camadas. Para cada camada, adicione o recheio at\u00e9 chegar a \u00faltima camada. Ap\u00f3s, utilize uma esp\u00e1tula de confeiteiro e decore todo o bolo com o restante da cobertura, adicionando e confeitando com nozes n\u00e3o trituradas.\n\n\n2. Voc\u00ea pode servir gelado ou n\u00e3o. Se for gelado, depois de pronto, deixe na geladeira por 10 minutos."
        },
        {
            "Nome": "Bolo Mil-folhas",
            "Tipo": "Doce",
            "Dificuldade": "Dif\u00edcil",
            "Ingredientes": "Massa:\n\n\u2022 1 rolo de massa folhada congelada\n\nCreme:\n\n\u2022 4 x\u00edcaras (ch\u00e1) de leite\n\u2022 2\/3 de x\u00edcara (ch\u00e1) de a\u00e7\u00facar\n\u2022 3\/4 de x\u00edcara (ch\u00e1) de maisena\n\u2022 5 gemas\n\u2022 2 colher (ch\u00e1) de ess\u00eancia de baunilha\n\nPara polvilhar\n\n\u2022 2 colheres (sopa) de a\u00e7\u00facar de confeiteiro",
            "Modo de Preparo": "Rende 8 por\u00e7\u00f5es:\n\nCreme:\n1. Coloque em uma vasilha as gemas e o a\u00e7\u00facar, bata bem at\u00e9 ficar esbranqui\u00e7ado.\n\n\n2. Misture a maisena e mexa bem. Reserve esta mistura.\n\n3. Coloque em uma panela o leite e a baunilha e deixe o leite quase ferver, em fogo baixo.\n\n4. Quando come\u00e7ar a levantar fervura, desligue e misture devagar este leite com a outra mistura, mexa bem. Volte tudo para a panela em fogo baixo e mexa at\u00e9 engrossar. Desligue o fogo e coloque papel filme encostando no creme, leve \u00e0 geladeira at\u00e9 ficar gelado.\n\n6. Depois tire e mexa de novo at\u00e9 voltar a consist\u00eancia de creme se pelotas.\n\nMassa:\n\n1. Corte a massa do tamanho que quiser que fique o bolo, eu fiz do tamanho de uma assadeira retangular grande, coloque na assadeira e leve ao forno para assar. Cuidado que \u00e9 bem r\u00e1pido. Quando estiver douradinha, vire para dourar o outro lado. Fa\u00e7a isso com quantas camadas quiser.\n\nMontagem:\n\n1. Depois da massa assada e do creme gelado e mexido, coloque uma camada de massa e outra de creme, assim sucessivamente. Na \u00faltima camada de massa, polvilhe o a\u00e7\u00facar de confeiteiro por cima.."
        },
        {
            "Nome": "Sufl\u00ea de chocolate",
            "Tipo": "Doce",
            "Dificuldade": "Dif\u00edcil",
            "Ingredientes": "\u2022 200 g de a\u00e7\u00facar\n\u2022 4 ovos\n\u2022 200 g de chocolate meio amargo\n\u2022 200 g de manteiga",
            "Modo de Preparo": "Rende 7 por\u00e7\u00f5es:\n\n1. Derreta o chocolate em banho-maria.\n\n2. Derreta a manteiga.\n\n3. Separada as claras das gemas dos ovos, reserve as gemas\n\n4. Bata as claras at\u00e9 que elas fiquem em ponto de neve, reserve.\n\n5. Bata as gemas com o a\u00e7\u00facar at\u00e9 ficar um creme.\n\n6. Por \u00faltimo, delicadamente adicione as claras em neve.\n\n7. Adicione o chocolate e a manteiga nesse creme.\n\n8. Coloque no forno, que n\u00e3o pode estar preaquecido, por cerca de 10 a 15 minutos.\n\n9. Espere at\u00e9 que ele esteja altinho."
        },
        {
            "Nome": "Omelete de Queijo",
            "Tipo": "Salgada",
            "Dificuldade": "F\u00e1cil",
            "Ingredientes": "\n\n\u2022 2 ovos\n\u2022 1 pitada de sal\n\u2022 1 fatia de presunto\n\u2022 2 fatias de queijo\n\u2022 tempero verde a gosto\n\u2022 caldo de galinha a gosto",
            "Modo de Preparo": "1. Bata os 2 ovos, pode ser na batedeira ou n\u00e3o.\n2. Ap\u00f3s ter batido bem, coloque-o na frigideira j\u00e1 untada com \u00f3leo, acrescente o sal, o presunto picado em quadradinhos e as duas fatias de queijo (n\u00e3o precisa picar o queijo).\n3. Coloque os temperos a gosto, espere ficar firme, e vire o omelete.\n4. Est\u00e1 pronto um omelete delicioso, bom apetite!"
        },
        {
            "Nome": "Arroz de Forno",
            "Tipo": "Salgada",
            "Dificuldade": "F\u00e1cil",
            "Ingredientes": "\n\u2022 3 x\u00edcaras de arroz cozido\n\u2022 1 lata de seleta de legumes (milho, ervilha, batata, cenoura etc)\n\u2022 1 peito de frango cozido e desfiado\n\u2022 2 tomates picados em cubos\n\u2022 1 cebola m\u00e9dia picada em rodelas\n\u2022 1 copo de requeij\u00e3o\n\u2022 1\/2 x\u00edcara de batata palha\n\u2022 1\/2 x\u00edcara de queijo mussarela ralado\n\u2022 2 colheres (sopa) de molho de tomate\n\u2022 1 colher (sopa) de \u00f3leo\n\u2022 sal a gosto\n\u2022 pimenta-do-reino a gosto",
            "Modo de Preparo": "1.Preaque\u00e7a o forno a 180\u00baC\n2.Misture os ingredientes\n3.Disponha o arroz em um refrat\u00e1rio e despeje por cima o queijo ralado\n4.Leve ao forno por 15 a 20 minutos para aquecer e gratinar"
        },
        {
            "Nome": "Sandu\u00edche Natural de Frango",
            "Tipo": "Salgada",
            "Dificuldade": "F\u00e1cil",
            "Ingredientes": "\n\n\u2022 100 g de frango desfiado pr\u00e9-cozido\n\u2022 1\/2 cebola pequena picada\n\u2022 1\/2 tomate picado\n\u2022 1 cenoura pequena ralada\n\u2022 1\/2 lata de milho verde\n\u2022 salsinha e cebolinha a gosto\n\u2022 sal a gosto\n\u2022 maionese light a gosto\n\u2022 p\u00e3o de forma",
            "Modo de Preparo": "\n1. Refogue o frango desfiado com azeite, alho e cebola em uma panela.\n2. Misture a cebola e o tomate picados, a cenoura ralada, o milho, a salsa, a cebolinha e o sal.\n3. Adicione maionese at\u00e9 a obter a consist\u00eancia desejada do recheio.\n4. Cremosa ou mais consistente, como voc\u00ea preferir.\n5.Coloque o recheio entre 2 fatias de p\u00e3o de forma."
        },
        {
            "Nome": "Panqueca Simples",
            "Tipo": "Salgada",
            "Dificuldade": "F\u00e1cil",
            "Ingredientes": "\n\u2022 2 x\u00edcaras (ch\u00e1) de farinha de trigo\n\u2022 2 x\u00edcaras (ch\u00e1) de leite\n\u2022 3 ovos\n\u2022 1 pitada de sal",
            "Modo de Preparo": "1. Bata todos os ingredientes no liquidificador por 2 minutos.\n2. Em seguida desligue e, com uma colher, misture a farinha que grudou no copo do liquidificador.\n3. Bata novamente s\u00f3 para misturar e reserve.\n4. Unte a frigideira com um fio de \u00f3leo e leve ao fogo at\u00e9 aquecer.\n5. Com o aux\u00edlio de uma concha, pegue uma por\u00e7\u00e3o de massa e coloque na frigideira, gire a frigideira para espalhar bem a massa.\n6. Abaixe o fogo e deixe dourar por baixo, em seguida vire do outro lado e deixe dourar, repita o processo com toda a massa."
        },
        {
            "Nome": "Macarr\u00e3o Alho e \u00d3leo",
            "Tipo": "Salgada",
            "Dificuldade": "F\u00e1cil",
            "Ingredientes": "\n\n\u2022 5 dentes de alho amassados\n\u2022 5 colheres de sopa de \u00f3leo\n\u2022 1 colher de sopa de manteiga\n\u2022 Sal a gosto",
            "Modo de Preparo": "1. Amasse bem o alho juntamente com o sal, formando uma pasta.\n2. Em uma frigideira, coloque o alho amassado e o \u00f3leo.\n3. Frite em fogo m\u00e9dio sem deixar o alho queimar, s\u00f3 dourar.\n4. Acrescente a manteiga e deixe ferver um pouco, s\u00f3 para incorporar bem o sabor, mexendo sempre.\n5. Coloque sobre o macarr\u00e3o imediatamente."
        },
        {
            "Nome": "Escondidinho de Carne Seca",
            "Tipo": "Salgada",
            "Dificuldade": "M\u00e9dia",
            "Ingredientes": "\n\u2022 500g carne seca\n\u2022 1kg mandioca\n\u2022 Cebola\n\u2022 Alho\n\u2022 Azeite\n\u2022 1 Caixa de Cr\u00e8me de Leite\n\u2022 Manteiga\n\u2022 Tomate\n\u2022 Queijo Parmes\u00e3o",
            "Modo de Preparo": "\n1. Esprema a mandioca ainda quente e leve em uma panela com a margarina e sal.\n2. Quando estiverem bem misturados acrescente o creme de leite, misture e reserve.\n3. Refogue a cebola e o alho em um fio de azeite.\n4. Acrescente a carne-seca desfiada e deixe fritar um pouco.\n5. Acrescente os tomates e deixe cozinhar at\u00e9 ficarem murchos e acerte o sal se achar necess\u00e1rio.\n6. Em um refrat\u00e1rio untado com azeite, coloque uma camada do pur\u00ea de mandioca, a carne seca e termine com o restante do pur\u00ea.\n7. Polvilhe com queijo parmes\u00e3o ralado e leve ao forno pra gratinar."
        },
        {
            "Nome": "Frango Xadrez",
            "Tipo": "Salgada",
            "Dificuldade": "M\u00e9dia",
            "Ingredientes": "\n\u2022 2 colheres (sopa) de azeite de oliva\n\u2022 2 cebolas m\u00e9dias cortadas em cubos\n\u2022 2 dentes de alho esmagados\n\u2022 500 g de fil\u00e9 de frango sem pele e cortado em cubos\n\u2022 sal a gosto\n\u2022 1 piment\u00e3o verde cortado em cubos\n\u2022 1 piment\u00e3o vermelho cortado em cubos\n\u2022 1 piment\u00e3o amarelo cortado em cubos\n\u2022 1 x\u00edcara (ch\u00e1) de cogumelos em conserva cortados ao meio\n\u2022 1\/4 x\u00edcara de molho shoyu\n\u2022 1 colher (sopa) de maisena\n\u2022 1\/2 x\u00edcara (ch\u00e1) de \u00e1gua\n\u2022 2 colheres (sopa) de amendoim torrado",
            "Modo de Preparo": "1. Em uma frigideira ou panela grande, misture a metade do azeite de oliva, a cebola, o alho e deixe fritar.\n2. Retire e coloque em um prato.\n3. Na mesma panela, coloque o sal, o restante do azeite e frite os piment\u00f5es e os cogumelos por 5 minutos.\n4. Retire e despeje em outro prato.\n5. Ainda na mesma panela, coloque o frango e frite at\u00e9 dourar.\n6. Coloque todos os ingredientes novamente na frigideira, misture bem com uma colher de pau e refogue por mais 2 minutos.\n7. Em uma x\u00edcara, misture o molho shoyu, a maisena e a \u00e1gua.\n8. Mexa bem e junte a mistura de frango.\n9. Cozinhe, mexendo constantemente, at\u00e9 formar um molho espesso.\n10. Coloque em uma travessa, polvilhe com amendoim e sirva quente."
        },
        {
            "Nome": "Risoto de Camar\u00e3o",
            "Tipo": "Salgada",
            "Dificuldade": "Dif\u00edcil",
            "Ingredientes": "\n\u2022 400 g de camar\u00e3o cinza limpo\n\u2022 3 x\u00edcaras (ch\u00e1) de arroz branco\n\u2022 1 cubo de caldo de camar\u00e3o\n\u2022 1\/2 x\u00edcara (ch\u00e1) de piment\u00e3o verde cortado em cubos pequenos\n\u2022 1 tomate sem sementes e cortado em cubos pequenos\n\u2022 cheiro-verde picado\n\u2022 2 colheres de extrato de tomate\n\u2022 2 dentes de alho\n\u2022 1 colher (sopa) de azeite\n\u2022 sal\n\u2022 1\/2 lim\u00e3o",
            "Modo de Preparo": "1. Tempere o camar\u00e3o com lim\u00e3o e sal, reserve por 10 minutos.\n2. Enquanto isso, fa\u00e7a o arroz, fritando-o muito bem.\n3. Em seguida, coloque \u00e1gua em uma panela, o suficiente para cobrir o arroz (sobrando uns 2 cent\u00edmetros a mais do que o arroz no fundo da panela)\n4. Coloque pouco sal, pois o molho do camar\u00e3o levar\u00e1 o cubo de caldo de camar\u00e3o.\n5. Cozinhe em fogo baixo at\u00e9 que toda \u00e1gua seque.\n6. Retire do fogo e deixe a tampa da panela aberta (para o arroz n\u00e3o passar do ponto).\n7. E uma frigideira grande, que caiba todo o camar\u00e3o, doure o alho e coloque todo o camar\u00e3o sem o suco do lim\u00e3o.\n8. Junte o tomate, o piment\u00e3o, o cheiro-verde, o extrato de tomate e o cubo de caldo de camar\u00e3o.\n9. Adicione um pouco de \u00e1gua, para que tenha molho suficiente para encobrir o camar\u00e3o na frigideira. Cozinhe em fogo baixo por 5 minutos.\n10. Enquanto isso, retire o arroz e coloque-o em um recipiente de cer\u00e2mica ou vidro, solte-o bastante com o garfo.\n11. Junte o molho do camar\u00e3o e misture, usando em uma das m\u00e3os um garfo, e em outra m\u00e3o uma colher.\n12. Decore com camar\u00f5es grelhados e coentro, sirva bem quente!"
        },
        {
            "Nome": "Ravioli Recheado",
            "Tipo": "Salgada",
            "Dificuldade": "Dif\u00edcil",
            "Ingredientes": "\n\u2022 280 g de farinha de trigo\n\u2022 120 g de s\u00eamola de grano duro\n\u2022 4 ovos\n\u2022 480 g de ricota de b\u00fafala (escorrida)\n\u2022 50 g de queijo parmes\u00e3o ralado fino\n\u2022 1 pitada de a\u00e7\u00facar\n\u2022 raspas de 1 lim\u00e3o-siciliano\n\u2022 folhas de manjeric\u00e3o picadas a gosto\n\u2022 noz-moscada ralada na hora a gosto\n\u2022 sal a gosto",
            "Modo de Preparo": "1. Numa tigela grande, misture as farinhas e reserve uma por\u00e7\u00e3o (cerca de \u2153 de x\u00edcara) \u2013 a quantidade total de farinha pode variar de acordo com o tamanho dos ovos.\n2. Numa tigela pequena, quebre um ovo de cada vez e transfira para outra tigela. 3. Bata os ovos com um garfo apenas para misturar as claras com as gemas.\n4. Abra um buraco no centro da farinha, como se fosse um \u201cvulc\u00e3o\u201d. Adicione os ovos batidos no centro e comece misturando com um garfo, do centro para as bordas, adicionando a farinha aos poucos. Amasse com as m\u00e3os at\u00e9 a farinha incorporar os ovos. V\u00e1 adicionando a farinha reservada caso necess\u00e1rio. Transfira a massa para a bancada e sove at\u00e9 que fique bem lisa.\n5. Embale a massa com filme e deixe descansar por 20 minutos. Enquanto isso, prepare o recheio.\n6. Numa peneira, escorra a ricota sobre a tigela, para retirar o excesso de soro. Enquanto isso, separe o restante dos ingredientes.\n7. Numa tigela m\u00e9dia, coloque a ricota (sem o soro), adicione o parmes\u00e3o, as raspas de lim\u00e3o e o manjeric\u00e3o picado. Tempere com uma pitada de a\u00e7\u00facar, sal e noz-moscada a gosto. Misture delicadamente e leve \u00e0 geladeira para firmar por 30 minutos \u2013 \u00e9 mais f\u00e1cil rechear os ravi\u00f3lis com o recheio gelado.\n8. Ap\u00f3s o tempo de descanso, corte a massa em quatro partes. Com um rolo de macarr\u00e3o (ou cilindro) abra a massa em folhas na espessura de 2 mm.\n9. Para modelar os ravi\u00f3lis: posicione uma faixa de massa sobre a bancada. \n10. Disponha no centro da massa por\u00e7\u00f5es de cerca de 10g do recheio uma ao lado da outra, deixando cerca de 1 cm de espa\u00e7o entre cada uma. Borrife a massa com \u00e1gua e cubra com outra faixa de massa. Com a lateral das m\u00e3os, retire o ar ao redor do recheio e pressione as bordas de massa para selar \u2013 assim os ravi\u00f3lis n\u00e3o abrem nem criam bolhas ao cozinhar. Com um cortador de ravi\u00f3li ou carretilha dentada, corte os ravi\u00f3lis ao redor de cada por\u00e7\u00e3o de recheio. Voc\u00ea pode deixar os ravi\u00f3lis quadradinhos ou cortar e dobrar as pontas para modelar o plin. Se preferir, utilize formas para ravi\u00f3lis.\n11. Transfira os ravi\u00f3lis para uma travessa levemente enfarinhada e repita com o restante.\n12. Leve uma panela grande com \u00e1gua ao fogo alto para ferver. Adicione sal e mergulhe uma parte dos ravi\u00f3lis \u2013 cozinhe em levas para que n\u00e3o grudem uns nos outros. Diminua o fogo para m\u00e9dio e fique de olho: quando o ravi\u00f3li subir \u00e0 superf\u00edcie da \u00e1gua, est\u00e1 cozido.\n13. Com uma escumadeira, transfira para uma travessa e repita com o restante. Sirva os ravi\u00f3lis de queijo com molho de tomate e folhas de manjeric\u00e3o fresco."
        },
        {
            "Nome": "Cordeiro Assado com Ervas",
            "Tipo": "Salgada",
            "Dificuldade": "Dif\u00edcil",
            "Ingredientes": "\n\u2022 1 pernil de carneiro (1,5 kg a 2 kg em m\u00e9dia)\n\u2022 2 cebolas m\u00e9dias\n\u2022 4 dentes de alho\n\u2022 1 copo americano de vinagre de vinho tinto\n\u2022 1 copo americano de \u00e1gua\n\u2022 2 colher de sopa de sal\n\u2022 1 colher de caf\u00e9 de pimenta do reino (mo\u00edda na hora) ou alternativamente 1 pimenta dedo de mo\u00e7a, sem pele e sementes\n\u2022 3 a 4 folhas de manjeric\u00e3o\n\u2022 2 a 3 folhas de hortel\u00e3\n\u2022 1 ma\u00e7o de salsinha picada",
            "Modo de Preparo": "\n1.Na V\u00e9spera\nLave o pernil e retire as gl\u00e2ndulas e todo excesso de gordura do pernil.\n2. Bata todos os ingredientes no liquidificador.\n3. Injete o tempero na carne com seringa pr\u00f3pria para isso. Se n\u00e3o tiver, fure bastante a carne para penetrar o tempero.\n4. Deixe marinando na geladeira por pelo menos 12 horas, de prefer\u00eancia dentro de um saco, para o tempeiro penetrar por igual\n5. No dia de servir\n6. Coloque o pernil em um refrat\u00e1rio e cubra com papel alum\u00ednio.\n7. Coloque no forno a 180\u00baC e deixe cozinhar por cerca de 1 hora.\n8. Retire o papel alum\u00ednio e asse at\u00e9 dourar (mais ou menos 1 hora).\n9. Durante o tempo em que estiver assando, coloque, aos poucos \u00e1gua na assadeira para n\u00e3o secar.\n10. Sirva com arroz, salada de r\u00facula ou agri\u00e3o."
        }
    ]);
