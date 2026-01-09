import os

print("--- RECHERCHE DU COUPABLE ---")
print("Je cherche les fichiers qui contiennent 'pygame.quit()' ou 'pygame.init()'")
print("-----------------------------")

# On parcours tous les dossiers
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py") and file != "debug_search.py":
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        # On cherche quit() ou init()
                        if "pygame.quit()" in line or "pygame.init()" in line:
                            # On ignore les commentaires
                            if line.strip().startswith("#"):
                                continue
                            
                            print(f"FICHIER : {path}")
                            print(f"  -> Ligne {i+1} : {line.strip()}")
                            print("-----------------------------")
            except:
                pass

print("--- FIN DE LA RECHERCHE ---")