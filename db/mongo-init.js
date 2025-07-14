// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

// The current database to use.
db = db.getSiblingDB('RecipeService');

db.createCollection('recipes')

// Create a new document in the collection.
db.getCollection('recipes').insertMany(
    [
        {
            "Name": "Brigadeiro",
            "Tipo": "Doce",
            "Difficulty": "INICIANTE",
            "Preparation": "Rende 30 porções:\n1. Em uma panela funda, acrescente o leite condensado, a margarina e o chocolate em pó.\n\n2. Cozinhe em fogo médio e mexa até que o brigadeiro comece a desgrudar da panela.\n\n3. Deixe esfriar e faça pequenas bolas com a mão passando a massa no chocolate granulado.",
            "Ingredients": [
                {
                    "quantity": "1 caixa",
                    "ingredient": "leite condensado"
                },
                {
                    "quantity": "1 colher (sopa)",
                    "ingredient": "margarina sem sal"
                },
                {
                    "quantity": "7 colheres (sopa)",
                    "ingredient": "achocolatado ou 4 colheres (sopa) de chocolate em pó"
                },
                {
                    "quantity": "",
                    "ingredient": "chocolate granulado"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/brigadeiro.png"
        },
        {
            "Name": "Bolo de Caneca",
            "Tipo": "Doce",
            "Difficulty": "INICIANTE",
            "Preparation": "Rende 1 porção:\n1. Coloque todos os Ingredients dentro de uma caneca de aproximadamente 300 ml ou mais.\n\n2. Mexa até obter uma massa homogênea e leve ao micro-ondas por 3 minutos.\n\nCalda:\n\n1. Coloque todos os Ingredients em uma panela, leve ao fogo médio e misture até obter uma consistência grossa.\n\n2. Despeje a calda sobre o bolo assim que retirará-lo do microondas.",
            "Ingredients": [
                {
                    "quantity": "1",
                    "ingredient": "ovo"
                },
                {
                    "quantity": "2 colheres (sopa)",
                    "ingredient": "achocolatado em pó"
                },
                {
                    "quantity": "3 colheres (sopa) rasas",
                    "ingredient": "açúcar"
                },
                {
                    "quantity": "4 colheres (sopa) rasas",
                    "ingredient": "farinha de trigo"
                },
                {
                    "quantity": "1 colher (sopa)",
                    "ingredient": "óleo"
                },
                {
                    "quantity": "",
                    "ingredient": "fermento em pó químico"
                },
                {
                    "quantity": "1 colher (café) rasa",
                    "ingredient": "fermento em pó"
                },
                {
                    "quantity": "4 colheres (sopa)",
                    "ingredient": "leite"
                },
                {
                    "quantity": "2 colheres (sopa)",
                    "ingredient": "achocolatado em pó"
                },
                {
                    "quantity": "1 colher (sopa)",
                    "ingredient": "margarina"
                },
                {
                    "quantity": "1/2 xícara",
                    "ingredient": "leite"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/bolo-de-caneca.png"
        },
        {
            "Name": "Mousse de Maracujá",
            "Tipo": "Doce",
            "Difficulty": "INICIANTE",
            "Preparation": "Rende 6 porções:\n1. Em um liquidificador, bata o creme de leite, o leite condensado e o suco concentrado de maracujá.\n\n2. Em uma tigela, despeje a mistura e leve à geladeira por, no mínimo, 4 horas.",
            "Ingredients": [
                {
                    "quantity": "1 lata",
                    "ingredient": "leite condensado"
                },
                {
                    "quantity": "1 lata",
                    "ingredient": "suco de maracujá (medida pela lata de leite condensado)"
                },
                {
                    "quantity": "1 lata",
                    "ingredient": "creme de leite sem soro"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/Mousse-de-Maracuj%C3%A1.png"
        },
        {
            "Name": "Banana Caramelada",
            "Tipo": "Doce",
            "Difficulty": "INICIANTE",
            "Preparation": "Rende 4 porções:\n1. Corte as bananas do tamanho que desejar.\n\n2. Despeje o açúcar em uma panela média junto com as bananas.\n\n3. Mexa vagarosamente em fogo médio com uma colher para não desmanchar as banana.\n\n4. Espere o açúcar chegar no ponto de caramelo(quando estiver derretendo) e desligue o fogo.\n\n5. Coloque as lascas de canela ao gosto.\n\n6. Sirva em uma bandeja de vidro e espere a banana esfriar.",
            "Ingredients": [
                {
                    "quantity": "6",
                    "ingredient": "bananas maduras (de preferência banana nanica/prata)"
                },
                {
                    "quantity": "1 xícara (café)",
                    "ingredient": "açúcar mascavo ou cristal"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "canela em lasca"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/Banana-Caramelada.png"
        },
        {
            "Name": "Pavê de Bolacha",
            "Tipo": "Doce",
            "Difficulty": "INICIANTE",
            "Preparation": "Rende 25 porções\n1. Leve ao fogo o leite condensado, o leite, as gemas e o amido já dissolvido (pode ser em um pouquinho de água).\n\n2. Mexa até engrossar, o segredo é não deixar ficar muito grosso, pois as bolachas não precisarão ser molhadas.\n\n3. Quando estiver meio grosso, coloque o coco ralado e deixe mais 5 minutos, desligue.\n\nCobertura:\n1. Bata as claras, junte o creme de leite, o açúcar e mexa, reserve.\n\n2. Em um refratário, coloque uma camada de recheio, outra de biscoito e quando as camadas completarem o refratário, adicione a cobertura.\n\n3.Leve à geladeira até ficar gelado..",
            "Ingredients": [
                {
                    "quantity": "3 pacotes",
                    "ingredient": "bolacha maizena"
                },
                {
                    "quantity": "1 lata",
                    "ingredient": "leite condensado"
                },
                {
                    "quantity": "2 latas",
                    "ingredient": "leite (medida da lata de leite condensado)"
                },
                {
                    "quantity": "2 colheres",
                    "ingredient": "amido de milho"
                },
                {
                    "quantity": "200 g",
                    "ingredient": "coco ralado"
                },
                {
                    "quantity": "2",
                    "ingredient": "gemas"
                },
                {
                    "quantity": "1 lata",
                    "ingredient": "creme de leite"
                },
                {
                    "quantity": "2",
                    "ingredient": "claras"
                },
                {
                    "quantity": "1 xícara",
                    "ingredient": "açúcar"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/Pav%C3%AA-de-Bolacha.png"
        },
        {
            "Name": "Torta de Limão",
            "Tipo": "Doce",
            "Difficulty": "INTERMEDIÁRIO",
            "Preparation": "Rende 15 porções:\n\nMassa:\n\n1 .Triture o biscoito de maisena em um liquidificador ou processador.\n\n2. Junte a margarina e bata mais um pouco.\n\n3. Despeje a massa em uma forma de fundo removível (27 cm de diâmetro).\n\n4. Com as mãos, espalhe os biscoitos triturados no fundo e nas laterais da forma, cobrindo toda área de maneira uniforme.\n\n5. Leve ao forno médio (180° C), preaquecido, por aproximadamente 10 minutos.\n\nRecheio:\n\n6. Bata todos os Ingredients no liquidificador até obter um creme liso e firme.\n\n7. Recheie a massa já assada e leve à geladeira por 30 minutos.\n\nCobertura:\n\n1. Bata as claras em neve e acrescente o açúcar.\n\n2. Misture até obter um ponto de suspiro e leve ao forno até dourar.\n\n3. Desenforme a torta (sem retirar o fundo falso).",
            "Ingredients": [
                {
                    "quantity": "200 g",
                    "ingredient": "biscoito de maisena"
                },
                {
                    "quantity": "150 g",
                    "ingredient": "margarina"
                },
                {
                    "quantity": "1 lata",
                    "ingredient": "leite condensado (395 g)"
                },
                {
                    "quantity": "1 caixa",
                    "ingredient": "creme de leite (200 g)"
                },
                {
                    "quantity": "",
                    "ingredient": "suco de 4 limões"
                },
                {
                    "quantity": "",
                    "ingredient": "raspas de 2 limões"
                },
                {
                    "quantity": "3",
                    "ingredient": "ou 4 claras de ovo"
                },
                {
                    "quantity": "3 colheres (sopa)",
                    "ingredient": "açúcar"
                },
                {
                    "quantity": "",
                    "ingredient": "raspas de 2 limões para decorar"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/Torta-de-Lim%C3%A3o.png"
        },
        {
            "Name": "Churros Caseiros",
            "Tipo": "Doce",
            "Difficulty": "INTERMEDIÁRIO",
            "Preparation": "Rende 20 porções\n1.Em uma panela, adicione o leite, a água, a manteiga e o sal.\n\n2. Quando o leite ferver, adicione a farinha de trigo e mexa rápido até a massa soltar do fundo da panela.\n\n3. Coloque a massa em um saco de confeiteiro com o bico pitanga, depois faça tirinhas com a massa e frite.\n\n4. Misture a canela e o açúcar, depois passe nos churros fritos.",
            "Ingredients": [
                {
                    "quantity": "1 e 1/2 xícara (chá)",
                    "ingredient": "leite"
                },
                {
                    "quantity": "1/2 xícara (chá)",
                    "ingredient": "água"
                },
                {
                    "quantity": "2 colheres (sopa)",
                    "ingredient": "margarina ou manteiga"
                },
                {
                    "quantity": "2 xícaras (chá)",
                    "ingredient": "farinha de trigo"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "sal"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "açúcar"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "canela"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/Churros-Caseiros.png"
        },
        {
            "Name": "Bolo Red Velvet",
            "Tipo": "Doce",
            "Difficulty": "INTERMEDIÁRIO",
            "Preparation": "Rende 8 porções:\n\nMassa:\n\n1. Misture 200 ml de leite com 1 colher (sopa) de suco de limão e reserve por 10 minutos.\n\n2. Em uma tigela, misture a farinha de trigo, açúcar refinado, cacau em pó, sal, bicarbonato de sódio, fermento em pó até ficar homogêneo e reserve.\n\n3. Na batedeira em velocidade média, bata por 10 minutos a manteiga, ovos, vinagre branco, essência de baunilha, corante alimentício vermelho, 05 colheres de suco de limão.\n\n4. Ainda na batedeira, intercale a mistura seca e o leite, adicionando-os à massa formada e bata por mais 5 minutos até formar uma massa bem cremosa.\n\n5. Em forno preaquecido a 180ºC, unte 2 tabuleiros redondos de 20 cm de diâmetro, divida a massa entre os 2 tabuleiros e asse por aproximadamente 20 a 40 minutos. Após 20 minutos, verifique se a massa está assada, perfurando o bolo com uma faca, se a mesma sair limpa, a massa estará pronta. Quando a massa estiver pronta, retire do forno e deixe esfriar antes de desenformar.\n\nRecheio e cobertura:\n\n1. Na batedeira em velocidade média, bata por 10 minutos a manteiga sem sal amolecida, cream cheese, chocolate branco derretido, açúcar de confeiteiro, essência de baunilha e nozes triturada.\n\n2. Quando formar uma mistura bem fofa e cremosa, reserve.\n\nMontagem:\n\n1. Desenforme os bolos e corte-os ao meio formando 4 camadas. Para cada camada, adicione o recheio até chegar a última camada. Após, utilize uma espátula de confeiteiro e decore todo o bolo com o restante da cobertura, adicionando e confeitando com nozes não trituradas.\n\n\n2. Você pode servir gelado ou não. Se for gelado, depois de pronto, deixe na geladeira por 10 minutos.",
            "Ingredients": [
                {
                    "quantity": "2",
                    "ingredient": "ovos"
                },
                {
                    "quantity": "100 g",
                    "ingredient": "manteiga sem sal amolecida"
                },
                {
                    "quantity": "1 colher (sopa)",
                    "ingredient": "vinagre branco"
                },
                {
                    "quantity": "1 colher (chá)",
                    "ingredient": "essência de baunilha"
                },
                {
                    "quantity": "4 colheres",
                    "ingredient": "corante alimentício líquido cor vermelha"
                },
                {
                    "quantity": "5 colheres (sopa)",
                    "ingredient": "suco de limão"
                },
                {
                    "quantity": "3 xícaras (chá)",
                    "ingredient": "farinha de trigo"
                },
                {
                    "quantity": "2 xícaras (chá)",
                    "ingredient": "açúcar refinado"
                },
                {
                    "quantity": "1 colher (sopa)",
                    "ingredient": "cacau em pó (Não pode ser achocolatado)"
                },
                {
                    "quantity": "1 colher (chá)",
                    "ingredient": "sal"
                },
                {
                    "quantity": "1 colher (sopa)",
                    "ingredient": "bicarbonato de sódio"
                },
                {
                    "quantity": "1 colher (sopa)",
                    "ingredient": "fermento em pó"
                },
                {
                    "quantity": "200 ml",
                    "ingredient": "leite integral"
                },
                {
                    "quantity": "1 colher (sopa)",
                    "ingredient": "suco de limão"
                },
                {
                    "quantity": "100 g",
                    "ingredient": "manteiga sem sal amolecida"
                },
                {
                    "quantity": "300 g",
                    "ingredient": "cream cheese"
                },
                {
                    "quantity": "200 g",
                    "ingredient": "chocolate branco derretido"
                },
                {
                    "quantity": "300 g",
                    "ingredient": "açúcar de confeiteiro"
                },
                {
                    "quantity": "1 colher (sopa)",
                    "ingredient": "essência de baunilha"
                },
                {
                    "quantity": "100 g",
                    "ingredient": "nozes triturada"
                },
                {
                    "quantity": "50 g",
                    "ingredient": "nozes não triturada"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/Bolo-Red-Velvet.png"
        },
        {
            "Name": "Bolo Mil-folhas",
            "Tipo": "Doce",
            "Difficulty": "AVANÇADO",
            "Preparation": "Rende 8 porções:\n\nCreme:\n1. Coloque em uma vasilha as gemas e o açúcar, bata bem até ficar esbranquiçado.\n\n\n2. Misture a maisena e mexa bem. Reserve esta mistura.\n\n3. Coloque em uma panela o leite e a baunilha e deixe o leite quase ferver, em fogo baixo.\n\n4. Quando começar a levantar fervura, desligue e misture devagar este leite com a outra mistura, mexa bem. Volte tudo para a panela em fogo baixo e mexa até engrossar. Desligue o fogo e coloque papel filme encostando no creme, leve à geladeira até ficar gelado.\n\n6. Depois tire e mexa de novo até voltar a consistência de creme se pelotas.\n\nMassa:\n\n1. Corte a massa do tamanho que quiser que fique o bolo, eu fiz do tamanho de uma assadeira retangular grande, coloque na assadeira e leve ao forno para assar. Cuidado que é bem rápido. Quando estiver douradinha, vire para dourar o outro lado. Faça isso com quantas camadas quiser.\n\nMontagem:\n\n1. Depois da massa assada e do creme gelado e mexido, coloque uma camada de massa e outra de creme, assim sucessivamente. Na última camada de massa, polvilhe o açúcar de confeiteiro por cima..",
            "Ingredients": [
                {
                    "quantity": "1 rolo",
                    "ingredient": "massa folhada congelada"
                },
                {
                    "quantity": "4 xícaras (chá)",
                    "ingredient": "leite"
                },
                {
                    "quantity": "2/3 xícara (chá)",
                    "ingredient": "açúcar"
                },
                {
                    "quantity": "3/4 xícara (chá)",
                    "ingredient": "maisena"
                },
                {
                    "quantity": "5",
                    "ingredient": "gemas"
                },
                {
                    "quantity": "2 colher (chá)",
                    "ingredient": "essência de baunilha"
                },
                {
                    "quantity": "2 colheres (sopa)",
                    "ingredient": "açúcar de confeiteiro"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/Bolo-Mil-folhas.png"
        },
        {
            "Name": "Suflê de chocolate",
            "Tipo": "Doce",
            "Difficulty": "AVANÇADO",
            "Preparation": "Rende 7 porções:\n\n1. Derreta o chocolate em banho-maria.\n\n2. Derreta a manteiga.\n\n3. Separada as claras das gemas dos ovos, reserve as gemas\n\n4. Bata as claras até que elas fiquem em ponto de neve, reserve.\n\n5. Bata as gemas com o açúcar até ficar um creme.\n\n6. Por último, delicadamente adicione as claras em neve.\n\n7. Adicione o chocolate e a manteiga nesse creme.\n\n8. Coloque no forno, que não pode estar preaquecido, por cerca de 10 a 15 minutos.\n\n9. Espere até que ele esteja altinho.",
            "Ingredients": [
                {
                    "quantity": "200 g",
                    "ingredient": "açúcar"
                },
                {
                    "quantity": "4",
                    "ingredient": "ovos"
                },
                {
                    "quantity": "200 g",
                    "ingredient": "chocolate meio amargo"
                },
                {
                    "quantity": "200 g",
                    "ingredient": "manteiga"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/sufle_chocolate.png"
        },
        {
            "Name": "Omelete de Queijo",
            "Tipo": "Salgada",
            "Difficulty": "INICIANTE",
            "Preparation": "1. Bata os 2 ovos, pode ser na batedeira ou não.\n2. Após ter batido bem, coloque-o na frigideira já untada com óleo, acrescente o sal, o presunto picado em quadradinhos e as duas fatias de queijo (não precisa picar o queijo).\n3. Coloque os temperos a gosto, espere ficar firme, e vire o omelete.\n4. Está pronto um omelete delicioso, bom apetite!",
            "Ingredients": [
                {
                    "quantity": "2",
                    "ingredient": "ovos"
                },
                {
                    "quantity": "1 pitada",
                    "ingredient": "sal"
                },
                {
                    "quantity": "1 fatia",
                    "ingredient": "presunto"
                },
                {
                    "quantity": "2 fatias",
                    "ingredient": "queijo"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "tempero verde"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "caldo de galinha"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/sufle_chocolate.png"
        },
        {
            "Name": "Arroz de Forno",
            "Tipo": "Salgada",
            "Difficulty": "INICIANTE",
            "Preparation": "1.Preaqueça o forno a 180ºC\n2.Misture os Ingredients\n3.Disponha o arroz em um refratário e despeje por cima o queijo ralado\n4.Leve ao forno por 15 a 20 minutos para aquecer e gratinar",
            "Ingredients": [
                {
                    "quantity": "3 xícaras",
                    "ingredient": "arroz cozido"
                },
                {
                    "quantity": "1 lata",
                    "ingredient": "seleta de legumes (milho, ervilha, batata, cenoura etc)"
                },
                {
                    "quantity": "1",
                    "ingredient": "peito de frango cozido e desfiado"
                },
                {
                    "quantity": "2",
                    "ingredient": "tomates picados em cubos"
                },
                {
                    "quantity": "1",
                    "ingredient": "cebola média picada em rodelas"
                },
                {
                    "quantity": "1 copo",
                    "ingredient": "requeijão"
                },
                {
                    "quantity": "1/2 xícara",
                    "ingredient": "batata palha"
                },
                {
                    "quantity": "1/2 xícara",
                    "ingredient": "queijo mussarela ralado"
                },
                {
                    "quantity": "2 colheres (sopa)",
                    "ingredient": "molho de tomate"
                },
                {
                    "quantity": "1 colher (sopa)",
                    "ingredient": "óleo"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "sal"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "pimenta-do-reino"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/arroz_forno.png"
        },
        {
            "Name": "Sanduíche Natural de Frango",
            "Tipo": "Salgada",
            "Difficulty": "INICIANTE",
            "Preparation": "\n1. Refogue o frango desfiado com azeite, alho e cebola em uma panela.\n2. Misture a cebola e o tomate picados, a cenoura ralada, o milho, a salsa, a cebolinha e o sal.\n3. Adicione maionese até a obter a consistência desejada do recheio.\n4. Cremosa ou mais consistente, como você preferir.\n5.Coloque o recheio entre 2 fatias de pão de forma.",
            "Ingredients": [
                {
                    "quantity": "100 g",
                    "ingredient": "frango desfiado pré-cozido"
                },
                {
                    "quantity": "1/2",
                    "ingredient": "cebola pequena picada"
                },
                {
                    "quantity": "1/2",
                    "ingredient": "tomate picado"
                },
                {
                    "quantity": "1",
                    "ingredient": "cenoura pequena ralada"
                },
                {
                    "quantity": "1/2 lata",
                    "ingredient": "milho verde"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "salsinha e cebolinha"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "sal"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "maionese light"
                },
                {
                    "quantity": "",
                    "ingredient": "pão de forma"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/sanduiche-natural-de-frango.png"
        },
        {
            "Name": "Panqueca Simples",
            "Tipo": "Salgada",
            "Difficulty": "INICIANTE",
            "Preparation": "1. Bata todos os Ingredients no liquidificador por 2 minutos.\n2. Em seguida desligue e, com uma colher, misture a farinha que grudou no copo do liquidificador.\n3. Bata novamente só para misturar e reserve.\n4. Unte a frigideira com um fio de óleo e leve ao fogo até aquecer.\n5. Com o auxílio de uma concha, pegue uma porção de massa e coloque na frigideira, gire a frigideira para espalhar bem a massa.\n6. Abaixe o fogo e deixe dourar por baixo, em seguida vire do outro lado e deixe dourar, repita o processo com toda a massa.",
            "Ingredients": [
                {
                    "quantity": "2 xícaras (chá)",
                    "ingredient": "farinha de trigo"
                },
                {
                    "quantity": "2 xícaras (chá)",
                    "ingredient": "leite"
                },
                {
                    "quantity": "3",
                    "ingredient": "ovos"
                },
                {
                    "quantity": "1 pitada",
                    "ingredient": "sal"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/panqueca-simples.png"
        },
        {
            "Name": "Macarrão Alho e Óleo",
            "Tipo": "Salgada",
            "Difficulty": "INICIANTE",
            "Preparation": "1. Amasse bem o alho juntamente com o sal, formando uma pasta.\n2. Em uma frigideira, coloque o alho amassado e o óleo.\n3. Frite em fogo médio sem deixar o alho queimar, só dourar.\n4. Acrescente a manteiga e deixe ferver um pouco, só para incorporar bem o sabor, mexendo sempre.\n5. Coloque sobre o macarrão imediatamente.",
            "Ingredients": [
                {
                    "quantity": "5 dentes",
                    "ingredient": "alho amassados"
                },
                {
                    "quantity": "5 colheres de sopa",
                    "ingredient": "óleo"
                },
                {
                    "quantity": "1 colher de sopa",
                    "ingredient": "manteiga"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "Sal"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/macarrao_alho_oleo.png"
        },
        {
            "Name": "Escondidinho de Carne Seca",
            "Tipo": "Salgada",
            "Difficulty": "INTERMEDIÁRIO",
            "Preparation": "\n1. Esprema a mandioca ainda quente e leve em uma panela com a margarina e sal.\n2. Quando estiverem bem misturados acrescente o creme de leite, misture e reserve.\n3. Refogue a cebola e o alho em um fio de azeite.\n4. Acrescente a carne-seca desfiada e deixe fritar um pouco.\n5. Acrescente os tomates e deixe cozinhar até ficarem murchos e acerte o sal se achar necessário.\n6. Em um refratário untado com azeite, coloque uma camada do purê de mandioca, a carne seca e termine com o restante do purê.\n7. Polvilhe com queijo parmesão ralado e leve ao forno pra gratinar.",
            "Ingredients": [
                {
                    "quantity": "500g",
                    "ingredient": "carne seca"
                },
                {
                    "quantity": "1kg",
                    "ingredient": "mandioca"
                },
                {
                    "quantity": "",
                    "ingredient": "Cebola"
                },
                {
                    "quantity": "",
                    "ingredient": "Alho"
                },
                {
                    "quantity": "",
                    "ingredient": "Azeite"
                },
                {
                    "quantity": "1 Caixa",
                    "ingredient": "Crème de Leite"
                },
                {
                    "quantity": "",
                    "ingredient": "Manteiga"
                },
                {
                    "quantity": "",
                    "ingredient": "Tomate"
                },
                {
                    "quantity": "",
                    "ingredient": "Queijo Parmesão"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/escondidinho-carne-seca.png"
        },
        {
            "Name": "Frango Xadrez",
            "Tipo": "Salgada",
            "Difficulty": "INTERMEDIÁRIO",
            "Preparation": "1. Em uma frigideira ou panela grande, misture a metade do azeite de oliva, a cebola, o alho e deixe fritar.\n2. Retire e coloque em um prato.\n3. Na mesma panela, coloque o sal, o restante do azeite e frite os pimentões e os cogumelos por 5 minutos.\n4. Retire e despeje em outro prato.\n5. Ainda na mesma panela, coloque o frango e frite até dourar.\n6. Coloque todos os Ingredients novamente na frigideira, misture bem com uma colher de pau e refogue por mais 2 minutos.\n7. Em uma xícara, misture o molho shoyu, a maisena e a água.\n8. Mexa bem e junte a mistura de frango.\n9. Cozinhe, mexendo constantemente, até formar um molho espesso.\n10. Coloque em uma travessa, polvilhe com amendoim e sirva quente.",
            "Ingredients": [
                {
                    "quantity": "2 colheres (sopa)",
                    "ingredient": "azeite de oliva"
                },
                {
                    "quantity": "2",
                    "ingredient": "cebolas médias cortadas em cubos"
                },
                {
                    "quantity": "2 dentes",
                    "ingredient": "alho esmagados"
                },
                {
                    "quantity": "500 g",
                    "ingredient": "filé de frango sem pele e cortado em cubos"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "sal"
                },
                {
                    "quantity": "1",
                    "ingredient": "pimentão verde cortado em cubos"
                },
                {
                    "quantity": "1",
                    "ingredient": "pimentão vermelho cortado em cubos"
                },
                {
                    "quantity": "1",
                    "ingredient": "pimentão amarelo cortado em cubos"
                },
                {
                    "quantity": "1 xícara (chá)",
                    "ingredient": "cogumelos em conserva cortados ao meio"
                },
                {
                    "quantity": "1/4 xícara",
                    "ingredient": "molho shoyu"
                },
                {
                    "quantity": "1 colher (sopa)",
                    "ingredient": "maisena"
                },
                {
                    "quantity": "1/2 xícara (chá)",
                    "ingredient": "água"
                },
                {
                    "quantity": "2 colheres (sopa)",
                    "ingredient": "amendoim torrado"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/frango-xadrez.png"
        },
        {
            "Name": "Risoto de Camarão",
            "Tipo": "Salgada",
            "Difficulty": "AVANÇADO",
            "Preparation": "1. Tempere o camarão com limão e sal, reserve por 10 minutos.\n2. Enquanto isso, faça o arroz, fritando-o muito bem.\n3. Em seguida, coloque água em uma panela, o suficiente para cobrir o arroz (sobrando uns 2 centímetros a mais do que o arroz no fundo da panela)\n4. Coloque pouco sal, pois o molho do camarão levará o cubo de caldo de camarão.\n5. Cozinhe em fogo baixo até que toda água seque.\n6. Retire do fogo e deixe a tampa da panela aberta (para o arroz não passar do ponto).\n7. E uma frigideira grande, que caiba todo o camarão, doure o alho e coloque todo o camarão sem o suco do limão.\n8. Junte o tomate, o pimentão, o cheiro-verde, o extrato de tomate e o cubo de caldo de camarão.\n9. Adicione um pouco de água, para que tenha molho suficiente para encobrir o camarão na frigideira. Cozinhe em fogo baixo por 5 minutos.\n10. Enquanto isso, retire o arroz e coloque-o em um recipiente de cerâmica ou vidro, solte-o bastante com o garfo.\n11. Junte o molho do camarão e misture, usando em uma das mãos um garfo, e em outra mão uma colher.\n12. Decore com camarões grelhados e coentro, sirva bem quente!",
            "Ingredients": [
                {
                    "quantity": "400 g",
                    "ingredient": "camarão cinza limpo"
                },
                {
                    "quantity": "3 xícaras (chá)",
                    "ingredient": "arroz branco"
                },
                {
                    "quantity": "1 cubo",
                    "ingredient": "caldo de camarão"
                },
                {
                    "quantity": "1/2 xícara (chá)",
                    "ingredient": "pimentão verde cortado em cubos pequenos"
                },
                {
                    "quantity": "1",
                    "ingredient": "tomate sem sementes e cortado em cubos pequenos"
                },
                {
                    "quantity": "",
                    "ingredient": "cheiro-verde picado"
                },
                {
                    "quantity": "2 colheres",
                    "ingredient": "extrato de tomate"
                },
                {
                    "quantity": "2 dentes",
                    "ingredient": "alho"
                },
                {
                    "quantity": "1 colher (sopa)",
                    "ingredient": "azeite"
                },
                {
                    "quantity": "",
                    "ingredient": "sal"
                },
                {
                    "quantity": "1/2",
                    "ingredient": "limão"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/risoto-camarao.png"
        },
        {
            "Name": "Ravioli Recheado",
            "Tipo": "Salgada",
            "Difficulty": "AVANÇADO",
            "Preparation": "1. Numa tigela grande, misture as farinhas e reserve uma porção (cerca de ⅓ de xícara) - a quantity total de farinha pode variar de acordo com o tamanho dos ovos.\n2. Numa tigela pequena, quebre um ovo de cada vez e transfira para outra tigela. 3. Bata os ovos com um garfo apenas para misturar as claras com as gemas.\n4. Abra um buraco no centro da farinha, como se fosse um “vulcão”. Adicione os ovos batidos no centro e comece misturando com um garfo, do centro para as bordas, adicionando a farinha aos poucos. Amasse com as mãos até a farinha incorporar os ovos. Vá adicionando a farinha reservada caso necessário. Transfira a massa para a bancada e sove até que fique bem lisa.\n5. Embale a massa com filme e deixe descansar por 20 minutos. Enquanto isso, prepare o recheio.\n6. Numa peneira, escorra a ricota sobre a tigela, para retirar o excesso de soro. Enquanto isso, separe o restante dos Ingredients.\n7. Numa tigela média, coloque a ricota (sem o soro), adicione o parmesão, as raspas de limão e o manjericão picado. Tempere com uma pitada de açúcar, sal e noz-moscada a gosto. Misture delicadamente e leve à geladeira para firmar por 30 minutos - é mais fácil rechear os raviólis com o recheio gelado.\n8. Após o tempo de descanso, corte a massa em quatro partes. Com um rolo de macarrão (ou cilindro) abra a massa em folhas na espessura de 2 mm.\n9. Para modelar os raviólis: posicione uma faixa de massa sobre a bancada. \n10. Disponha no centro da massa porções de cerca de 10g do recheio uma ao lado da outra, deixando cerca de 1 cm de espaço entre cada uma. Borrife a massa com água e cubra com outra faixa de massa. Com a lateral das mãos, retire o ar ao redor do recheio e pressione as bordas de massa para selar - assim os raviólis não abrem nem criam bolhas ao cozinhar. Com um cortador de ravióli ou carretilha dentada, corte os raviólis ao redor de cada porção de recheio. Você pode deixar os raviólis quadradinhos ou cortar e dobrar as pontas para modelar o plin. Se preferir, utilize formas para raviólis.\n11. Transfira os raviólis para uma travessa levemente enfarinhada e repita com o restante.\n12. Leve uma panela grande com água ao fogo alto para ferver. Adicione sal e mergulhe uma parte dos raviólis - cozinhe em levas para que não grudem uns nos outros. Diminua o fogo para médio e fique de olho: quando o ravióli subir à superfície da água, está cozido.\n13. Com uma escumadeira, transfira para uma travessa e repita com o restante. Sirva os raviólis de queijo com molho de tomate e folhas de manjericão fresco.",
            "Ingredients": [
                {
                    "quantity": "280 g",
                    "ingredient": "farinha de trigo"
                },
                {
                    "quantity": "120 g",
                    "ingredient": "sêmola de grano duro"
                },
                {
                    "quantity": "4",
                    "ingredient": "ovos"
                },
                {
                    "quantity": "480 g",
                    "ingredient": "ricota de búfala (escorrida)"
                },
                {
                    "quantity": "50 g",
                    "ingredient": "queijo parmesão ralado fino"
                },
                {
                    "quantity": "1 pitada",
                    "ingredient": "açúcar"
                },
                {
                    "quantity": "",
                    "ingredient": "raspas de 1 limão-siciliano"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "folhas de manjericão picadas"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "noz-moscada ralada na hora"
                },
                {
                    "quantity": "a gosto",
                    "ingredient": "sal"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/ravioli_recheado.png"
        },
        {
            "Name": "Cordeiro Assado com Ervas",
            "Tipo": "Salgada",
            "Difficulty": "AVANÇADO",
            "Preparation": "\n1.Na Véspera\nLave o pernil e retire as glândulas e todo excesso de gordura do pernil.\n2. Bata todos os Ingredients no liquidificador.\n3. Injete o tempero na carne com seringa própria para isso. Se não tiver, fure bastante a carne para penetrar o tempero.\n4. Deixe marinando na geladeira por pelo menos 12 horas, de preferência dentro de um saco, para o tempeiro penetrar por igual\n5. No dia de servir\n6. Coloque o pernil em um refratário e cubra com papel alumínio.\n7. Coloque no forno a 180ºC e deixe cozinhar por cerca de 1 hora.\n8. Retire o papel alumínio e asse até dourar (mais ou menos 1 hora).\n9. Durante o tempo em que estiver assando, coloque, aos poucos água na assadeira para não secar.\n10. Sirva com arroz, salada de rúcula ou agrião.",
            "Ingredients": [
                {
                    "quantity": "1",
                    "ingredient": "pernil de carneiro (1,5 kg a 2 kg em média)"
                },
                {
                    "quantity": "2",
                    "ingredient": "cebolas médias"
                },
                {
                    "quantity": "4 dentes",
                    "ingredient": "alho"
                },
                {
                    "quantity": "1 copo americano",
                    "ingredient": "vinagre de vinho tinto"
                },
                {
                    "quantity": "1 copo americano",
                    "ingredient": "água"
                },
                {
                    "quantity": "2 colher de sopa",
                    "ingredient": "sal"
                },
                {
                    "quantity": "1 colher de café",
                    "ingredient": "pimenta do reino (moída na hora) ou alternativamente 1 pimenta dedo de moça, sem pele e sementes"
                },
                {
                    "quantity": "3 a 4 folhas",
                    "ingredient": "manjericão"
                },
                {
                    "quantity": "2 a 3 folhas",
                    "ingredient": "hortelã"
                },
                {
                    "quantity": "1 maço",
                    "ingredient": "salsinha picada"
                }
            ],
            "image_url": "https://sidechef-recipe-images.s3.sa-east-1.amazonaws.com/cordeiro-assado-em-ervas.png"
        }
    ]
)