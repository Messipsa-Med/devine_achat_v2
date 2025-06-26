import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

df_base = pd.read_csv("profils_achat.csv")
df_hist = pd.read_csv("historique_devine_achat.csv")

df_total = pd.concat([df_base, df_hist], ignore_index=True)

sns.scatterplot(x="Age",y="Salaire",hue="Acheté",data = df_total)
plt.show()


def devine_achat_v2():

    while True:
        a = input("\nEntrez l'âge : ")
        if a.isdigit() :
            a = int(a)
            if 18<a<110 :
                b = input("\nEntrez le salaire : ")
                if b.isdigit() :
                    b = int(b)
                    break
                else:
                    print("\nVeuillez entrer un nombre")
            else :
                print("\nVeuillez entrer un âge valide")
        else:
            print("\nVeuillez entrer un nombre")

    new_pred = pd.DataFrame([[a, b]], columns=["Age", "Salaire"])

    if ia.predict(new_pred) == 0:
      print("\nN'achètera pas")
    else:
      print("\nAchètera")

    while True :
        reponse = input("\nCe client a-t-il acheté ?")
        if reponse in ["0","1"]:
            break
        else :
            print ("\nEntrez uniquement 1 ou 0 svp")

    with open("historique_devine_achat.csv","a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow([a,b,int(reponse)])

    while True:
        choix = input("\nVoulez-vous entrer un autre profil ? 1 pour oui, 0 pour non : ")
        if choix != "1":
            break
        else:
            print("\nMerci d'avoir utilisé notre outil\n")
            return 

if __name__ == "__main__":
    devine_achat_v2()