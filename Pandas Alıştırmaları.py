####################################################################
                         PANDAS ALIŞTIRMALARI
####################################################################

# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.

import seaborn as sns
df = sns.load_dataset("titanic")
df.head()


# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.

df["sex"].value_counts()

    # çıktı =>
            # male      577
            # female    314
            # Name: sex, dtype: int64

# Görev 3: Her bir sütuna ait unique değerlerin sayısını bulunuz.

df.nunique()

    # çıktı =>
# survived         2
# pclass           3
# sex              2
# age             88
# sibsp            7
# parch            7
# fare           248
# embarked         3
# class            3
# who              3
# adult_male       2
# deck             7
# embark_town      3
# alive            2
# alone            2
# dtype: int64


# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.

df["pclass"].nunique()

    # çıktı => 3


# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.

df[["pclass", "parch"]].nunique()

    # çıktı =>

# pclass    3
# parch     7
# dtype: int64

# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.

str(df["embarked"].dtype)

    # çıktı => 'object'

df["embarked"] = df["embarked"].astype("category")
str(df["embarked"].dtype)

    # çıktı => 'category'

# Görev 7: embarked değeri C olanların tüm bilgilerini gösteriniz.

df[(df["embarked"] == "C")]

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.

df[(df["embarked"] != "S")]

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df[(df["age"] < 30) & (df["sex"] == "female")]

# Görev 10: Fare'i 500'den büyük veya yaşı 70’den büyük yolcuların bilgilerini gösteriniz.

df[(df["fare"] > 500) | (df["age"] > 70)]

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.

df.isnull().sum()

    # çıktı =>

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

# Görev 12: who değişkenini dataframe’den çıkarınız.

df.drop("who", axis=1, inplace=True)

# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.

df['deck'].fillna(df['deck'].mode()[0], inplace=True)
df['deck'].isnull().sum()

# Görev 14: age değişkenindeki boş değerleri age değişkenin medyanı ile doldurunuz.

df['age'].fillna(df['age'].median(), inplace=True)
df['age'].isnull().sum()

# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})

    # çıktı =>          survived
#                    sum count      mean
# pclass sex
# 1      female       91    94  0.968085
#        male         45   122  0.368852
# 2      female       70    76  0.921053
#        male         17   108  0.157407
# 3      female       72   144  0.500000
#        male         47   347  0.135447

# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 verecek bir fonksiyon yazın.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz (apply ve lambda yapılarını kullanınız).

df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)
df.head()

    # çıktı =>

#       survived  pclass   sex   age  ...  embark_town  alive  alone   age_flag
# 0         0       3    male  22.0  ...  Southampton     no  False        1
# 1         1       1  female  38.0  ...    Cherbourg    yes  False        0
# 2         1       3  female  26.0  ...  Southampton    yes   True        1
# 3         1       1  female  35.0  ...  Southampton    yes  False        0
# 4         0       3    male  35.0  ...  Southampton     no   True        0


# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.

import seaborn as sns
df = sns.load_dataset("tips")
df.head()

    # çıktı =>
#   total_bill   tip     sex  smoker  day    time  size
# 0       16.99  1.01  Female     No  Sun  Dinner     2
# 1       10.34  1.66    Male     No  Sun  Dinner     3
# 2       21.01  3.50    Male     No  Sun  Dinner     3
# 3       23.68  3.31    Male     No  Sun  Dinner     2
# 4       24.59  3.61  Female     No  Sun  Dinner     4

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerinin sum, min, max ve mean değerlerini bulunuz.

df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})

    # çıktı =>
#                     total_bill
#               sum   min    max       mean
# time
# Lunch     1167.47  7.51  43.11  17.168676
# Dinner    3660.30  3.07  50.81  20.797159


# Görev 19: Day ve time’a göre total_bill değerlerinin sum, min, max ve mean değerlerini bulunuz.

df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

    # çıktı =>
#                           total_bill
#                    sum    min    max       mean
# day  time
# Thur Lunch     1077.55   7.51  43.11  17.664754
#      Dinner      18.78  18.78  18.78  18.780000
# Fri  Lunch       89.92   8.58  16.27  12.845714
#      Dinner     235.96   5.75  40.17  19.663333
# Sat  Lunch        0.00    NaN    NaN        NaN
#      Dinner    1778.40   3.07  50.81  20.441379
# Sun  Lunch        0.00    NaN    NaN        NaN
#      Dinner    1627.16   7.25  48.17  21.410000

# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre sum, min, max ve mean değerlerini bulunuz.

df[["total_bill", "tip", "day"]].loc[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day"). \
agg({"total_bill": ["sum", "min", "max", "mean"], "tip": ["sum", "min", "max", "mean"]})

    # çıktı =>          total_bill                   tip
#             sum    min    max      mean    sum   min   max      mean
# day
# Thur     516.11   8.35  43.11  16.64871  79.42  1.25  5.17  2.561935
# Fri       55.76  10.09  16.27  13.94000  10.98  2.00  3.48  2.745000
# Sat        0.00    NaN    NaN       NaN   0.00   NaN   NaN       NaN
# Sun        0.00    NaN    NaN       NaN   0.00   NaN   NaN       NaN


# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)

df.loc[(df["size"] < 3) & (df["total_bill"] > 10)]["total_bill"].mean()

    # çıktı => 17.18496503496505

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği total bill ve tip in toplamını versin.

df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

    # çıktı =>
#    total_bill   tip     sex  smoker  day  time   size  total_bill_tip_sum
# 0       16.99  1.01  Female     No  Sun  Dinner     2               18.00
# 1       10.34  1.66    Male     No  Sun  Dinner     3               12.00
# 2       21.01  3.50    Male     No  Sun  Dinner     3               24.51
# 3       23.68  3.31    Male     No  Sun  Dinner     2               26.99
# 4       24.59  3.61  Female     No  Sun  Dinner     4               28.20


# Görev 23: Total_bill değişkeninin kadın ve erkek için ayrı ayrı ortalamasını bulunuz. Bulduğunuz ortalamaların altında olanlara 0, üstünde ve eşit olanlara 1 verildiği yeni bir total_bill_flag değişkeni oluşturunuz.
# Kadınlar için Female olanlarının ortalamaları, erkekler için ise Male olanların ortalamaları dikkate alınacaktır. Parametre olarak cinsiyet ve total_bill alan bir fonksiyon yazarak başlayınız. (If-else koşulları içerecek)

f_avg = df[df["sex"] == "Female"]["total_bill"].mean()
m_avg = df[df["sex"] == "Male"]["total_bill"].mean()


def function(sex, total_bill):
    if sex == "Female":
        if total_bill >= f_avg:
            return 1
        else:
            return 0
    else:
        if total_bill >= m_avg:
            return 1
        else:
            return 0

df["total_bill_flag"] = df.apply(lambda x: function(x["sex"], x["total_bill"]), axis=1)
df.head()

    # çıktı =>
# total_bill   tip     sex  ... size total_bill_tip_sum total_bill_flag
# 0       16.99  1.01  Female  ...    2              18.00               0
# 1       10.34  1.66    Male  ...    3              12.00               0
# 2       21.01  3.50    Male  ...    3              24.51               1
# 3       23.68  3.31    Male  ...    2              26.99               1
# 4       24.59  3.61  Female  ...    4              28.20               1


# Görev 24: total_bill_flag değişkenini kullanarak cinsiyetlere göre ortalamanın altında ve üstünde olanların sayısını gözlemleyiniz.

df.groupby(["sex", "total_bill_flag"]).total_bill_flag.count()

    # çıktı =>

# sex     total_bill_flag
# Male    0                  95
#         1                  62
# Female  0                  54
#         1                  33
# Name: total_bill_flag, dtype: int64


# Görev 25: Veriyi total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.

first_30_df = df.sort_values('total_bill_tip_sum', ascending=False).head(30)
first_30_df

    # çıktı =>

#       total_bill  tip     sex  ...  size total_bill_tip_sum total_bill_flag
# 170       50.81  10.00    Male  ...    3              60.81               1
# 212       48.33   9.00    Male  ...    4              57.33               1
# 59        48.27   6.73    Male  ...    4              55.00               1
# 156       48.17   5.00    Male  ...    6              53.17               1
# 182       45.35   3.50    Male  ...    3              48.85               1
# 197       43.11   5.00  Female  ...    4              48.11               1
# 23        39.42   7.58    Male  ...    4              47.00               1
# 102       44.30   2.50  Female  ...    3              46.80               1
# 142       41.19   5.00    Male  ...    5              46.19               1
# 95        40.17   4.73    Male  ...    4              44.90               1
# 184       40.55   3.00    Male  ...    2              43.55               1
# 112       38.07   4.00    Male  ...    3              42.07               1
# 207       38.73   3.00    Male  ...    4              41.73               1
# 56        38.01   3.00    Male  ...    4              41.01               1
# 141       34.30   6.70    Male  ...    6              41.00               1
# 238       35.83   4.67  Female  ...    3              40.50               1
# 11        35.26   5.00  Female  ...    4              40.26               1
# 52        34.81   5.20  Female  ...    4              40.01               1
# 85        34.83   5.17  Female  ...    4              40.00               1
# 47        32.40   6.00    Male  ...    4              38.40               1
# 180       34.65   3.68    Male  ...    4              38.33               1
# 179       34.63   3.55    Male  ...    2              38.18               1
# 83        32.68   5.00    Male  ...    2              37.68               1
# 39        31.27   5.00    Male  ...    3              36.27               1
# 167       31.71   4.50    Male  ...    4              36.21               1
# 175       32.90   3.11    Male  ...    2              36.01               1
# 44        30.40   5.60    Male  ...    4              36.00               1
# 173       31.85   3.18    Male  ...    2              35.03               1
# 116       29.93   5.07    Male  ...    4              35.00               1
# 155       29.85   5.14  Female  ...    5              34.99               1
# [30 rows x 9 columns]

