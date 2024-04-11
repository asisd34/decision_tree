# decision_tree
Bu uygulamamızda yine www.kaggle.com'dan indirdiğimiz ve aşağıda açıklaması verilen veri setini kullanacağız.
Bu veri seti, bir tıp araştırması için toplanan verileri içeriyor. Araştırmacılar, aynı hastalığa sahip bir grup hastadan veri toplamıştır. Tedavi süreci boyunca, her hasta beş farklı ilaçtan birine yanıt vermiştir: İlaç A, İlaç B, İlaç C, İlaç X ve İlaç Y.

Bu veri setiyle amaç, aynı hastalığa sahip gelecekteki bir hastaya hangi ilacın uygun olabileceğini belirlemek için bir model oluşturmaktır. Veri setinin özellikleri hastaların yaşları, cinsiyetleri, kan basınçları ve kolesterol düzeyleridir. Hedef değişken, her hastanın yanıt verdiği ilaçtır.

Bu veri seti, çok sınıflı bir sınıflandırma probleminin örneğidir. Veri setinin eğitim bölümünü kullanarak bir karar ağacı oluşturabilir ve daha sonra bilinmeyen bir hastanın sınıfını tahmin etmek veya yeni bir hastaya bir ilaç reçete etmek için kullanabilirsiniz.

Veri setinin kolonları hakkında daha detaylı bilgi verelim:

Yaş (Age): Hastaların yaşlarını temsil eder. Sayısal bir değerdir.

Cinsiyet (Sex): Hastaların cinsiyetini temsil eder. Kategorik bir değişkendir ve genellikle "M" (erkek) veya "F" (kadın) olarak kodlanır.

Kan Basıncı (Blood Pressure): Hastaların kan basıncını temsil eder. Kategorik olarak "DÜŞÜK", "NORMAL" ve "YÜKSEK" gibi gruplara ayrılmıştır.

Kolesterol (Cholesterol): Hastaların kolesterol seviyelerini temsil eder. Kategorik olarak "DÜŞÜK", "NORMAL" ve "YÜKSEK" gibi gruplara ayrılmıştır.

Na/K Oranı (Na_to_K): Hastaların sodyum (Na) ve potasyum (K) oranını temsil eder. Bu sayısal bir değerdir.

İlaç (Drug): Hastaların yanıt verdiği ilacı temsil eder. Bu, modelimizin tahmin etmeye çalışacağı hedef değişkendir ve genellikle "İlaç A", "İlaç B", "İlaç C", "İlaç X" ve "İlaç Y" gibi kategorik değerler alır.
Dataset: https://www.kaggle.com/datasets/pablomgomez21/drugs-a-b-c-x-y-for-decision-trees
