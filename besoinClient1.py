#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import joblib
import numpy as np
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description='Prends en entrée des caractéristiques d\'un arbre et renvoie le cluster de taille d\'arbre associé')
    parser.add_argument('-n', '--clusters', type=str, help='Nombre de clusters', required=True)
    parser.add_argument('-d', '--diam_tronc', type=str, help='Diametre du tronc', required=True)
    parser.add_argument('-t', '--haut_tot', type=str, help='Hauteur totale de l\'arbre', required=True)

    args = parser.parse_args()

    filename = ""

    if(args.clusters == "2"):
        filename = "kmeans_haut_tot_from_diam_tronc_2_clusters.pkl"
    elif(args.clusters == "3"):
        filename = "kmeans_haut_tot_from_diam_tronc_3_clusters.pkl"
    else:
        return # error

    kmeans_loaded = joblib.load(filename)

    new_data = pd.DataFrame(np.array([[float(args.haut_tot),float(args.diam_tronc)]]), columns=['haut_tot', 'tronc_diam'])

    predicted_cluster = kmeans_loaded.predict(new_data)

    print(f"Le modèle KMeans prédit que cet arbre est dans le cluster numéro {predicted_cluster[0]}")

if __name__ == "__main__":
    main()
