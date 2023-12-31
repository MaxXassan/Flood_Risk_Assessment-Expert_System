import math
from KB import mappingAsset3, mappingAsset5, mappingVulnerability

## functions to calculate value of Asset1 (basically the same for Asset2
def calculateAsset1Residential(bd, bh, mg):
    result = (1.2*float(bd) + 1.4*float(bh) + 1.1*float(mg))/3
    return result

def calculateAsset1Industrial(bd, ra, ci):
    result = (1.2*float(bd) + 1.4*float(ra) + 2*float(ci))/3
    return result

def calculateAsset1Recreational(bd, mr, wv):
    result = (1.2*float(bd) + float(mr) + 0.5*float(wv))/3
    return result

## functions to calculate value of Asset2
def calculateAsset2Residential(bd, bh, mg):
    result = (1.2*float(bd) + 1.4*float(bh) + 1.1*float(mg))/3
    return result

def calculateAsset2Industrial(bd, ra, ci):
    result = (1.2*float(bd) + 1.4*float(ra) + 2*float(ci))/3
    return result

def calculateAsset2Recreational(bd, mr, wv):
    result = (1.2*float(bd) + float(mr) + 0.5*float(wv))/3
    return result

## functions to calculate value of Asset4
def calculateNonVegetatedSurface(ass, ab):
    result = (1.2*float(ass) + 1.4*float(ab))/3
    return result

def calculateVegetatedSurface(wv, cl):
    result = (0.2*float(wv) + 1.1*float(cl))/3
    return result    

def calculateWaterSurface(pw, tw):
    result = (1.5*float(pw) + 0.9*float(tw))/3
    return result

def checker(l1, l2):
    ## check if all elements in l1 are the same in l2
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return 1  
    return 0

def appendAsset1(facts, values, type):
    if type == "Recreational":
        facts.append(f"{3}, {values[0]}, {values[1]}, {values[2]}")
    elif type == "Industrial":
        facts.append(f"{2}, {values[0]}, {values[1]}, {values[2]}")
    elif type == "Residential":
        facts.append(f"{1}, {values[0]}, {values[1]}, {values[2]}")

    facts = stringToInt(facts)
    
    return facts

def appendAsset2(facts, values, type):
    if type == "Recreational":
        facts.append(f"{6}, {values[0]}, {values[1]}, {values[2]}")
    elif type == "Industrial":
        facts.append(f"{5}, {values[0]}, {values[1]}, {values[2]}")
    elif type == "Residential":
        facts.append(f"{4}, {values[0]}, {values[1]}, {values[2]}")

    facts = stringToInt(facts)

    return facts

def appendAsset3(asset1, asset2, facts):
    listt = [None]*3

    listt[0] = 13

    print("asset1", asset1)
    print("asset2", asset2)

    lower_asset1 = math.floor(asset1)
    upper_asset1 = math.ceil(asset1)

    lower_asset2 = math.floor(asset2)
    upper_asset2 = math.ceil(asset2)

    print("lower_asset1", lower_asset1)
    print("upper_asset1", upper_asset1)
    print("lower_asset2", lower_asset2)
    print("upper_asset2", upper_asset2)
    
    listt[1] = mappingAsset3.get((lower_asset1, upper_asset1), listt[1])
    listt[2] = mappingAsset3.get((lower_asset2, upper_asset2), listt[2])

    facts.append(f"{listt[0]}, {listt[1]}, {listt[2]}")
    facts = stringToInt(facts)
    print("facts", facts)

    return facts

def appendAsset4(facts, values, type):
    facts.append({
        "Non-Vegetated Surface": f"{7}, {values[0]}, {values[1]}",
        "Vegetated Surface": f"{8}, {values[0]}, {values[1]}",
        "Water": f"{9}, {values[0]}, {values[1]}"
        }[type])
    
    facts = stringToInt(facts)
    
    return facts

def appendAsset5(asset3, asset4, facts):
    listt = [None]*3

    listt[0] = 12
    print(asset3)
    lower_asset3 = math.floor(asset3)
    upper_asset3 = math.ceil(asset3)

    lower_asset4 = math.floor(asset4)
    upper_asset4 = math.ceil(asset4)

    print("lower_asset3", lower_asset3)
    print("upper_asset3", upper_asset3)
    print("lower_asset4", lower_asset4)
    print("upper_asset4", upper_asset4)
   
    listt[1] = mappingAsset5.get((lower_asset3, upper_asset3), listt[1])
    listt[2] = mappingAsset5.get((lower_asset4, upper_asset4), listt[2])

    facts.append(f"{listt[0]}, {listt[1]}, {listt[2]}")
    facts = stringToInt(facts)
    print("facts", facts)

    return facts

def appendVulnerability(facts, type, asset5, exposure):
    listt = [None]*4

    listt[0] = 10
    listt[1] = type
    listt[3] = math.floor(exposure)
    print("asset5", asset5)

    upper = math.ceil(asset5)
    lower = math.floor (asset5)
   
    listt[2] = mappingVulnerability.get((lower, upper), listt[2])

    ## for exposure
    if listt[3] == 1 or listt[3] == 2:
        listt[3] = "a"

    facts.append(f"{listt[0]}, {listt[1]}, {listt[2]}, {listt[3]}")
    facts = stringToInt(facts)

    return facts

def appendRisk(facts, vulnerability, floodLevel):
    facts.append(f"{11}, {vulnerability}, {floodLevel}")
    facts = stringToInt(facts)

    return facts

def stringToInt(facts):
    # split the string into integers
    for i in range(len(facts)):
        facts[i] = facts[i].split(", ")
        for j in range(len(facts[i])):
            ## ignore chracaters
            if facts[i][j].isalpha():
                continue
            else:
                facts[i][j] = int(facts[i][j])
        
    return facts