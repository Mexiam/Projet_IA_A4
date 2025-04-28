#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import joblib
import numpy as np
import pandas as pd

"haut_tot", "haut_tronc", "tronc_diam"


def main():
    parser = argparse.ArgumentParser(description='Prends en entrée des caractéristiques d\'un arbre et renvoie le cluster de taille d\'arbre associé')
    parser.add_argument('-d', '--diam_tronc', type=str, help='Diametre du tronc', required=True)
    parser.add_argument('-t', '--haut_tot', type=str, help='Hauteur totale de l\'arbre', required=True)
    parser.add_argument('-r', '--haut_tronc', type=str, help='Hauteur du tronc', required=True)

    args = parser.parse_args()

    filename = "decisiontree_regressor.pkl"

    decision_tree_loaded = joblib.load(filename)

    new_data = pd.DataFrame(np.array([[float(args.haut_tot),float(args.haut_tronc),float(args.diam_tronc)]]),
                             columns=["haut_tot", "haut_tronc", "tronc_diam"])

    predicted_age = decision_tree_loaded.predict(new_data)

    print(f"Le modèle Decision Tree prédit que cet arbre a un age de {predicted_age[0]}")

if __name__ == "__main__":
    main()
