def normalizar_nombre_propio(name):
    """
    str -> str
    Función que transforma un texto a las normas
    del español de forma correcta para un nombre propio.
    >>>>normalizar_nombre_propio(" rigoberto   villalta   ")
    'Rigoberto Vilalta'
    >>>>normalizar_nombre_propio("Rigoberto  villalta   ")
    'Rigoberto Vilalta'
    >>>>normalizar_nombre_propio(" rigoberto Villalta.")
    'Rigoberto Vilalta'
    >>>>normalizar_nombre_propio(" María De Los   Ángeles ")
    'María de los Ángeles'
    >>>>normalizar_nombre_propio("Rosa Del Carmen")
    'Rosa del Carmen'
    >>>>normalizar_nombre_propio(" ernesto de la cruz.")
    'Ernesto de la Cruz'
    """
    nombre_normalizado = ' '.join(name.strip().title().split())
    while " De " in nombre_normalizado:
        nombre_normalizado = nombre_normalizado.replace(' De ', ' de ')
    while " Del " in nombre_normalizado:
        nombre_normalizado = nombre_normalizado.replace(' Del ', ' del ')
    while " La " in nombre_normalizado:
        nombre_normalizado = nombre_normalizado.replace(' La ', ' la ')
    while " Los " in nombre_normalizado:
        nombre_normalizado = nombre_normalizado.replace(' Los ', ' los ')
    while "." in nombre_normalizado:
        nombre_normalizado = nombre_normalizado.replace('.', '')
    return nombre_normalizado