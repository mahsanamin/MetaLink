class Rules():
    dataTypes   = ("int","string","float","long","arr")
    
    systemColumns = {"_id":          {"shortName":"i"   ,  "type":"int"},
                     "_name":        {"shortName":"nm"  ,  "type":"string"},
                     "_sort_order":  {"shortName":"so"  ,  "type":"int"},
                     "_resources":   {"shortName":"res" ,  "type":"string"},
                     "_is_active":   {"shortName":"ia"  ,  "type":"int"},
                     "_buy_price":   {"shortName":"bp"  ,  "type":"int"}, 
                     "_sell_price":  {"shortName":"sp"  ,  "type":"int"}
                    }
    
