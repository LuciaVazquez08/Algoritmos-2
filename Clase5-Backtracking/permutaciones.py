def permutar(lista_og: list[int]) -> list[list[int]]:    
    permutaciones = []

    def permutar_interna(perm, resto):
        if not resto:
            permutaciones.append(perm)
        else: 
            for i in range(len(resto)):
                permutar_interna(perm + [resto[i]], resto[:i] + resto[i+1:])


    permutar_interna([], lista_og)
    return permutaciones
