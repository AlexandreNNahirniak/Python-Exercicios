larg=float(input('Largura da parede: '))
alt=float(input('Altura da parede: '))
área=larg*alt
print(f'Sua parede tem a medida de {larg} x {alt} e a área é de {área}m²')
quantia_tinta=área/2
print(f'Para pintar a parede vai ser necessário {quantia_tinta}L de tinta')