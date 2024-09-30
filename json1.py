import json 
import os
os.system("cls")

odam = {
    "ism" : "KImdir",
    "yosh" : 123,
    "adres" : "Urganch"
}

o = json.dumps(odam, indent=4)        #! dumps - malumotni json file qilib oladi
                                    #! indent qator tushurib beradi

f  = open("odam.json","w+")
f.write(o)

f.close()