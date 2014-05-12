class Rules():

    metaSheetName = "meta"
    idColumnName = "_id"
    keyName  = "key"
    dataName = "data"
    
    dataTypes   = {"int":1,"string":1,"float":1,"long":1}
    
    systemColumns = {idColumnName:   {"shortName":"id"   , "type":"int"},
                     "_name":        {"shortName":"nm" ,  "type":"string"},
                     "_sort_order":  {"shortName":"so"  ,  "type":"int"},
                     "_assets":      {"shortName":"asts" ,  "type":"string"},
                     "_is_active":   {"shortName":"ia"  ,  "type":"int"},
                     "_buy_price":   {"shortName":"bp"  ,  "type":"int"}, 
                     "_sell_price":  {"shortName":"sp"  ,  "type":"int"}
                    }    