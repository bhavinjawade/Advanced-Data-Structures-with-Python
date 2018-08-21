def pour(jug1, jug2):
    
    capacityA = 5
    capacityB = 7
    Measure = 4  
    print("%d \t %d" % (jug1, jug2))

    if jug2 is Measure: # jug2 has "measure" amount of water stop
        return
    
    elif jug2 is capacityB:
        pour(0, jug1) 
    
    elif jug1 != 0 and jug2 is 0:
        pour(0, jug1)
    
    elif jug1 is Measure: # jug1 has "measure" amount of water, pour that to jug2
        pour(jug1, 0)
    
    elif jug1 < capacityA: 
        pour(capacityA, jug2)
    
    elif jug1 < (capacityB-jug2):
        pour(0, (jug1+jug2))
    
    else:
        pour(jug1-(capacityB-jug2), (capacityB-jug2)+jug2)
 
print("Jug 1 \t Jug 2")
pour(0, 0)