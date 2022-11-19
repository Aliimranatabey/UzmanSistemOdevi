#Gerekli Kütüphanelerin Eklenmesi
from random import choice 
from experta import *

class dis(Fact):
    """Diş Rahatsızlıkları ile İlgili Genel Bilgiler"""
    pass

class disRahatsizliklari(KnowledgeEngine):
    @Rule(dis(rahatsızlık="dişEtiKanaması"))
    def rahatsızlık1(self):
        print("Diş hastalığı vardır ve diş hekimine başvur .")
    
    @Rule(dis(rahatsızlık="uzunSüreliDişEtiKanaması"))
    def rahatsızlık2(self):
        print("Diş eti çekilmesi vardır ve diş hekimine başvur .")
        
    @Rule(dis(rahatsızlık="dişEtiÇekilmesiVarVeDişKöküGörünüyorsa"))
    def rahatsızlık3(self):    
        print("Dolgu yaptır.")
        
    @Rule(dis(rahatsızlık="dişteYiyecekVeİçeceklerdenOluşanRenkDeğişimiVarsa"))
    def rahatsızlık4(self):    
        print("Dişleri Temizle.")
    
    @Rule(dis(rahatsızlık="yeniDişÇıkarkenMorarmaGözüküyorsa"))
    def rahatsızlık5(self):    
        print("Diş Hekimine Başvur.")
        
    @Rule(dis(rahatsızlık="dişteAğrıYapmayanÇürükseVarsa"))
    def rahatsızlık6(self):    
        print("Dolgu Yaptır.")
        
    @Rule(dis(rahatsızlık="diştekiÇürükİleriDerecedeyse"))
    def rahatsızlık7(self):    
        print("Kanal Tedavisi ve Dolgu Yaptır.")
        
uzman=disRahatsizliklari()
uzman.reset()
uzman.declare(dis(rahatsızlık=choice(["dişEtiKanaması","uzunSüreliDişEtiKanaması","dişEtiÇekilmesiVarVeDişKöküGörünüyorsa",
                                "dişteYiyecekVeİçeceklerdenOluşanRenkDeğişimiVarsa","yeniDişÇıkarkenMorarmaGözüküyorsa",
                                "dişteAğrıYapmayanÇürükseVarsa","diştekiÇürükİleriDerecedeyse"])))
uzman.run()