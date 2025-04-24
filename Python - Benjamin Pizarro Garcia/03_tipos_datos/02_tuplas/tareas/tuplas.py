# Tuplas

pistas = ("Puerta Roja", 221, "Londres", 3.14, "Watson", 7, "Moriarty")

print("🔎 ¡Bienvenido, detective Holmes!")
print("📜 Se ha encontrado una serie de pistas misteriosas...")
print("🗝️ Pistas encontradas:", pistas)

# Analisis de pistas

print("\n🔍 Analizando pistas...")

print("\n🕵️ Felicitaciones, detective. !Has resuleto el analisis inicial de las pistas¡")
print("🔐 Ahora, sigue con las deducciones para resolver el misterio")

# ¿Cual es la primera pista?
print(pistas[0])

# ¿Cual es la ultima pista?
print(pistas[-1])

# ¿Cuantas pistas hay en total?
print(len(pistas))

# ¿Esta la palabra "londres" en la lista de pistas?
print("Londres" in pistas)

# Desenpaqueta las primeras tres pistas
pista1, pista2, pista3 = pistas[:3]
print(pista1, pista2, pista3)

# Crea una nueva tupla con pistas adicionales

nuevas_pistas = pistas + ("Nueva Pista 1", "Nueva Pista 2")
print(nuevas_pistas)

# Encuentra la posicion de "Watson" en la lista de pistas
print(pistas.index("Watson"))

# ¿Cuantas veces aparece el numero 7 en la lista de pistas?
print(pistas.count(7))