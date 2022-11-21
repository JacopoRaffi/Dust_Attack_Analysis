import pandas as pd

#viene caricato un file .csv.xz in un dataframe
df = pd.read_csv("animali_zoo.csv.xz", compression='xz')
# Il dataframe ha la seguente forma:
#   Animale         Nome   Peso(Kg)
#   Panda           Icaro    1100
#   Orso_Bruno      Dedalo   500   
#   Panda           Apollo   1055
#   Panda           Zeus     1165
#   Orso_Polare     Cupido   450
#   Orso_Bruno      Ermes    600

df.groupby("Animale").count()
#Risultato:
#  Panda: 3
#  Orso_Bruno: 2
#  Orso_Polare: 1

df[df.Animale == 'Panda']
#Risultato:
# Animale   Nome    Peso(Kg)
# Panda     Icaro   1100
# Panda     Zeus    1165
# Panda     Apollo  1055

#la ~(tilde) corrisponde ad una negazione
df[~df.Animale == 'Pandas']
#Risultato:
#   Animale         Nome    Peso(Kg)
#   Orso_Bruno      Dedalo   500 
#   Orso_Bruno      Ermes    600
#   Orso_Polare     Cupido   450