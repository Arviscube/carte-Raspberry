import os
import re


def nettoyer_contenu_kicad(contenu: str) -> str:
    contenu = re.sub(r'\(kicad_symbol_lib.*?\(symbol', '(symbol', contenu, flags=re.DOTALL)

    contenu = contenu.rstrip()
    if contenu.endswith(')'):
        contenu = contenu[:-1].rstrip()

    print(contenu)

    return contenu

def fusionner_kicad_sym(fichiers, fichier_sortie):
    en_tete = '(kicad_symbol_lib (version 20211014) (generator "custom-script")\n'
    symboles_total = []

    for fichier in fichiers:
        with open(fichier, 'r', encoding='utf-8') as f:
            contenu = f.read()
            symboles = nettoyer_contenu_kicad(contenu)
            symboles_total.append(symboles)

    contenu_final = en_tete + "\n\n".join(symboles_total) + "\n)"

    with open(fichier_sortie, 'w', encoding='utf-8') as f_out:
        f_out.write(contenu_final)

    print(f"✅ Fusion terminé. Fichier créé : {fichier_sortie}")

# 🔧 Utilisation :
# Dossier contenant les .kicad_sym
dossier_source = "symbols"
# Fichier de sortie
fichier_fusionne = "symbols.kicad_sym"

# Récupérer tous les .kicad_sym du dossier
fichiers_sym = [os.path.join(dossier_source, f) for f in os.listdir(dossier_source) if f.endswith(".kicad_sym")]

# Lancer la fusion
fusionner_kicad_sym(fichiers_sym, fichier_fusionne)
