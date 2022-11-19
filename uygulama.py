#Gerekli Kütüphanelerin Eklenmesi
from random import choice 
from experta import *

class Işık(Fact):
    """Trafik Işıklarıyla İlgili Genel Bilgiler"""
    pass

class KarşıdanKarşıyaGeçme(KnowledgeEngine):
    @Rule(Işık(renk="yeşil"))
    def yeşil_ışık(self):
        print("Yeşil ışık yandığı için yürüyebliirsiniz.")
    
    @Rule(Işık(renk="kırmızı"))
    def kırmızı_ışık(self):
        print("Kırmızı ışık yandığı için lütfen bekleyiniz.")
        
    @Rule(Işık(renk="sarı"))
    def sarı_ışık(self):    
        print("Sarı ışık yanıyor . Lütfen dikkatli olunuz.")
        
uzman=KarşıdanKarşıyaGeçme()
uzman.reset()
uzman.declare(Işık(renk=choice(["yeşil","sarı","kırmızı"])))
uzman.run()