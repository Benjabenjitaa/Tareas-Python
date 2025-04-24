# Benjamin Pizarro Garcia
# 14-04-2025

n_elefantes = int(input("¿Cuántos elefantes quieren que canten?: "))

for elefantes in range(1, n_elefantes + 1):
    if elefantes == 1:
        print("Un elefante se columpiaba sobre la tela de un araña")
        print("Como veía que no se caía, fue a llamar a otro elefante")
    else:
        print(f"{elefantes} elefantes se columpiaban sobre la tela de una araña")
        print("Como veían que no se caían, fueron a llamar a otro elefante")
