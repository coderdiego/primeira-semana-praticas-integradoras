# Ao criar um arquivo.txt no shell script do ubuntu voce insere algumas palavras

ajudaria
animalesco
pescaria
pipocando
comemorando

# Executa o comando cat arquivo.txt mostrará o arquivo com as palavras
# Proximo passo é executar o comando SED para alterar as palavras 

sed -i "s/ajuda/descomplica/g" arquivo.txt
sed -i "s/animal/descomplica/g" arquivo.txt
sed -i "s/pesca/descomplica/g" arquivo.txt
sed -i "s/pipoca/descomplica/g" arquivo.txt
sed -i "s/comemora/descomplica/g" arquivo.txt

# Esse comando irá inserir a palavra descomplica sobre a parte da palavra que foi determinada
# Por exemplo a palavra ajudaria sera cortada a parte ajuda
# Então a descomplica sobrescreve essa parte tornando descomplica+RIA restante da palavra

descomplicaria
descomplicaesco
descomplicaria
descomplicando
descomplicando

# Uma dessas palavras geradas pela junção da palavra 'normal' + descomplica gera a palavra chave 
# Essa palavra chave foi utilizada para abrir um arquivo com senha 