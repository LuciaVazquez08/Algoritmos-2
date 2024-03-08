def contarLetra(lista: list[str], letra: str) -> list[str]:
    return list(map(lambda x: x.count(letra), lista))

print(contarLetra(['casa', 'hogar', 'espacio', 'cuento'], "c"))