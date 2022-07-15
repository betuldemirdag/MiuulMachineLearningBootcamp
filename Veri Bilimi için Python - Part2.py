####################################################################################
# GÖREV: cat_summary() fonksiyonuna 1 özellik ekleyiniz.
        #Bu özellik argümanla biçimlendirilebilir olsun.
        #Var olan özelliği de argümanla kontrol edilebilir hale getirebilirsiniz.
####################################################################################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")

def cat_summary(dataframe, graph, head = 3, tail = 4, quan = False):
    print("################## SHAPE #########################")
    print(dataframe.shape)
    print("################## TYPES #########################")
    print(dataframe.dtypes)
    print("################## HEAD #########################")
    print(dataframe.head(head))
    print("################## TAIL #########################")
    print(dataframe.tail(tail))
    print("################## NA #########################")
    print(dataframe.isnull().sum())
    if quan:
        print("################## QUANTİLES #########################")
        print(dataframe.quantile(0, 0.05, 0.50, 0.95, 0.99, 1).T)

    print("################## PLOT #########################")
    dataframe.plot(x = graph,  kind = "bar")
    plt.show()

cat_summary(df, "survived")

    # çıktı =>
# ################## SHAPE #########################
# (891, 15)
# ################## TYPES #########################
# survived          int64
# pclass            int64
# sex              object
# age             float64
# sibsp             int64
# parch             int64
# fare            float64
# embarked         object
# class          category
# who              object
# adult_male         bool
# deck           category
# embark_town      object
# alive            object
# alone              bool
# dtype: object
# ################## HEAD #########################
#    survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
# 0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
# 1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
# 2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
# ################## TAIL #########################
#      survived  pclass     sex   age  sibsp  parch   fare embarked  class    who  adult_male deck  embark_town alive  alone
# 887         1       1  female  19.0      0      0  30.00        S  First  woman       False    B  Southampton   yes   True
# 888         0       3  female   NaN      1      2  23.45        S  Third  woman       False  NaN  Southampton    no  False
# 889         1       1    male  26.0      0      0  30.00        C  First    man        True    C    Cherbourg   yes   True
# 890         0       3    male  32.0      0      0   7.75        Q  Third    man        True  NaN   Queenstown    no   True
# ################## NA #########################
# survived         0
# pclass           0
# sex              0
# age            177
# sibsp            0
# parch            0
# fare             0
# embarked         2
# class            0
# who              0
# adult_male       0
# deck           688
# embark_town      2
# alive            0
# alone            0
# dtype: int64
# ################## PLOT #########################
