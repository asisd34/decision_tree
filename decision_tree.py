import pandas as pd  # Veri işleme ve manipülasyonu için
import numpy as np  # Sayısal işlemler için
import matplotlib.pyplot as plt  # Görselleştirme için
import seaborn as sns  # Veri görselleştirmesi için
from sklearn.model_selection import train_test_split  # Veriyi eğitim ve test setlerine ayırmak için
from sklearn.tree import DecisionTreeClassifier, plot_tree  # Karar ağacı modeli oluşturmak için
from sklearn.metrics import accuracy_score, confusion_matrix  # Model performansını değerlendirmek için
from sklearn.preprocessing import LabelEncoder # Kategorik değişkenleri sayısallaştırmak için





# Veri setini yükleme
data = pd.read_csv("drug200.csv")

# Veri setinin ilk beş gözlemine bakma
print(data.head())

# Kolon başlıklarını Türkçeleştirme
data.columns = ["Yaş", "Cinsiyet", "Kan_Basıncı", "Kolesterol", "Na_K_oranı", "İlaç"]

# Cinsiyet kolonunu sayısallaştırma
le = LabelEncoder()
data["Cinsiyet"] = le.fit_transform(data["Cinsiyet"])

# Kan_Basıncı ve Kolesterol kolonlarını sayısallaştırma
data["Kan_Basıncı"] = le.fit_transform(data["Kan_Basıncı"])
data["Kolesterol"] = le.fit_transform(data["Kolesterol"])
print(data.info())

# Bağımsız değişkenler ve hedef değişken arasında ayırma
X = data.drop("İlaç", axis=1)
y = data["İlaç"]

# Eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Karar ağacı modelini oluşturma
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Karar ağacını görselleştirme
plt.figure(figsize=(15, 10))
plot_tree(clf, feature_names=X.columns, class_names=clf.classes_, filled=True)
plt.show()

# Korelasyon matrisini hesaplama
correlation_matrix = data.corr()

# Korelasyon matrisini görselleştirme
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Değişkenler Arası Korelasyon Haritası")
plt.show()

# İkili değişken grafiklerini çizme
sns.pairplot(data)
plt.show()

# Test seti üzerinde tahmin yapma
y_pred = clf.predict(X_test)

# Doğruluk skorunu hesaplama
accuracy = accuracy_score(y_test, y_pred)
print("Doğruluk Skoru:", accuracy)

# Karmaşıklık matrisini oluşturma
cm = confusion_matrix(y_test, y_pred)
print("Karmaşıklık Matrisi:\n", cm)