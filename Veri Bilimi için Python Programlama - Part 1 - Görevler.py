###########################################################################################

# Görev 1: Verile n değerlerin veri yapılarını inceleyiniz. Type() metodunu kullanınız.

############################################################################################

x = 8
type(x)

  # çıktı => int

y = 3.2
type(y)

  # çıktı => float

z = 8j + 18
type(z)

  # çıktı => complex

a = "Hello World"
type(a)

  # çıktı => str

b = True
type(b)

  # çıktı => bool

c = 23 < 22
type(c)

  # çıktı => bool

l = [1, 2, 3, 4]
type(l)

  # çıktı => list

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d)

  # çıktı => dict

t = {"Machine Learning", "Data Science"}
type(t)

  # çıktı => set

s = {"Python", "Machine Learning", "Data Science"}
type(s)

  # çıktı => set


###########################################################################################

# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

############################################################################################

text = "The goal is to turn data into information, and information into insight."
a = text.replace(".", " ").replace(",", " ")
ntext = a.upper().split(" ")
print(ntext)

  # çıktı => ['THE', 'GOAL', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'INFORMATION', '', 'AND', 'INFORMATION', 'INTO', 'INSIGHT', '']

###########################################################################################

# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.

############################################################################################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# ADIM 1: Verilen listenin eleman sayısına bakınız.

print(len(lst))

  # çıktı => 11

# ADIM 2: Sıfırıncı ve onuncu indexteki elemanları çağırınız.

print(lst[0])
print(lst[10])

  # çıktı => D, E

# ADIM 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesini oluşturunuz.

liste1 = []
liste1.append(lst[0:4])
print(liste1)

  # çıktı => [['D', 'A', 'T', 'A']]

# ADIM 4: Sekizinci indeksteki elemanı siliniz.

lst.remove(lst[8])
print(lst)

  # çıktı => ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'C', 'E']

# ADIM 5: Yeni bir eleman ekleyiniz.

lst.append(2)
print(lst)

  # çıktı => ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'C', 'E', 2]

# ADIM 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert(8, "N")
print(lst)

  # çıktı => ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E', 2]

###########################################################################################

# Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

############################################################################################

dict = {
     "Christian": ["America", 18],
     "Daisy": ["England", 12],
     "Antonio": ["Spain", 22],
     "Dante": ["Italy", 25]}

# ADIM 1: Key değerlerine erişiniz.

print(dict.keys())
  # çıktı => dict_keys(['Christian', 'Daisy', 'Antonio', 'Dante'])

# ADIM 2: Value'lara erişiniz.

print(dict.values())
  # çıktı => dict_values([['America', 18], ['England', 12], ['Spain', 22], ['Italy', 25]])

# ADIM 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict["Daisy"][1] = 13
print(dict)
  # çıktı => {'Christian': ['America', 18], 'Daisy': ['England', 13], 'Antonio': ['Spain', 22], 'Dante': ['Italy', 25]}

# ADIM 4: Key değeri Ahmet, value değeri [Turkey, 24] olan yeni bir değer ekleyiniz.

dict.update({"Ahmet": ["Turkey", 24]})
print(dict)
  # çıktı => {'Christian': ['America', 18], 'Daisy': ['England', 13], 'Antonio': ['Spain', 22], 'Dante': ['Italy', 25], 'Ahmet': ['Turkey', 24]}

# ADIM 5: Antonio'yu dictionary'den siliniz.

dict.pop("Antonio")
print(dict)
  # çıktı => {'Christian': ['America', 18], 'Daisy': ['England', 13], 'Dante': ['Italy', 25], 'Ahmet': ['Turkey', 24]}

###########################################################################################

# Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyonu yazınız.

############################################################################################

l = [2, 13, 18, 93, 22]
def func():
     even_list = []
     odd_list = []
     for i in l:
          if i % 2 == 0:
               even_list.append(i)
          else:
               odd_list.append(i)
     return even_list, odd_list

func()

  # çıktı => ([2, 18, 22], [13, 93])

###########################################################################################

# Görev 6: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz

############################################################################################

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

  # çıktı => ['NUM_TOTAL',
     #  'NUM_SPEEDING',
     #  'NUM_ALCOHOL',
     #  'NUM_NOT_DISTRACTED',
     #  'NUM_NO_PREVIOUS',
     #  'NUM_INS_PREMIUM',
     #  'NUM_INS_LOSSES',
     #  'ABBREV']

###########################################################################################

# Görev 7: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.

############################################################################################

[col.upper() + "_FLAG" if col[0:2] != "no" else col.upper() for col in df.columns]

 # çıktı => ['TOTAL_FLAG',
     #  'SPEEDING_FLAG',
     #  'ALCOHOL_FLAG',
     #  'NOT_DISTRACTED',
     #  'NO_PREVIOUS',
     #  'INS_PREMIUM_FLAG',
     #  'INS_LOSSES_FLAG',
     #  'ABBREV_FLAG']

###########################################################################################

# Görev 8: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

############################################################################################

import pandas as pd

og_list = ["abbrev", "no_previous"]

yeni = [col for col in df.columns if col not in og_list]
yeni = df[yeni]
yeni.head()

 # çıktı =>    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
          # 0   18.8     7.332    5.640          18.048       784.55      145.08
          # 1   18.1     7.421    4.525          16.290      1053.48      133.93
          # 2   18.6     6.510    5.208          15.624       899.47      110.35
          # 3   22.4     4.032    5.824          21.056       827.34      142.39
          # 4   12.0     4.200    3.360          10.920       878.41      165.63