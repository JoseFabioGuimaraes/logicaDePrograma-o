primeiraPalavra = input("Digite a primeira palavra: ").lower()
segundaPalavra = input("Digite a segunda palavra: ").lower()

if(len(primeiraPalavra) != len(segundaPalavra)):
    print("Não é um anagrama")
else:
    if (sorted(primeiraPalavra) == sorted(segundaPalavra)):
        print("As palavras são anagramas")
    else:
        print("As palavras não são anagramas")