times = ("Palmeiras", "Internacional","Fluminense","Corinthians","Flamengo","Athletico-PR","Atlético-MG","Fortaleza","São Paulo","América-MG",
"Botafogo","Santos","Goiás","Bragantino","Coritiba","Cuiabá","Ceará","Atletico-GO", "Avaí","Chapecoense")
print(f"Os primeiros 5 times são {times[:5]}")
print(f"Os últimos colocados foram {times[-4:]}")
print(f"Os times são {sorted(times)}")
print(f'Chapecoense está na {times.index("Chapecoense")+1} posição')
