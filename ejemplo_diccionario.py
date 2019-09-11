def localidad():
    
    localidades = {
    'manacor': 29054,
    'calvia':234234,
    'inca':345345,
    'sineu':5453534,
    'palma':2,
    }
    localidad = input('INGRESA UNA LOCALIDAD\n')
    for localidad1 in localidades:
        if localidad1 == localidad:
            print(localidad1 , 'tiene' , localidades[localidad] , 'habitantes')