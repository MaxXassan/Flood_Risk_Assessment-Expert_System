from KB import *
from gui import * 
from functions import *

facts = []

## Functional Unit class
class FU:
    def __init__(self):
        self.asset1 = 0
        self.asset2 = 0
        self.asset3 = 0
        self.asset4 = 0
        self.asset5 = 0
        self.vulnerability = 0
        self.risk = 0

if __name__ == "__main__":

    #Update facts with input from gui, in the form "premise"
    asset1Found, asset2Found, asset3Found, asset4Found, asset5Found, vulnerabilityFound, riskFound = 0, 0, 0, 0, 0, 0, 0

    runStartPage()
    values, types = runGUI()
    # Add fact about asset1
    facts = appendAsset1(facts, values, types)
    asset1Found = 1
    
    # The inference engine using forward chaining
    while riskFound == 0:
        for rule in KB:
            if checker(facts[0], rule) == 0 or facts[0] == rule[0]:
                print("current fact:", facts[0])
                temp = rule[-1][1] #conclusion
                print("conclusion of rule in kb:", rule[-1][1])
                facts = []

                if asset1Found == 1 and asset2Found == 0: 
                    FU.asset1 = temp
                    values, type = runGUI2()
                    facts = appendAsset2(facts, values, type)
                    asset2Found = 1
                    
                elif asset2Found == 1 and asset3Found == 0: 
                    FU.asset2 = temp
                    facts = appendAsset3(FU.asset1, FU.asset2, facts)
                    asset3Found = 1

                elif asset3Found == 1 and asset4Found == 0:
                    FU.asset3 = temp
                    values, type = runGUI3()
                    facts = appendAsset4(facts, values, type)
                    asset4Found = 1

                elif asset4Found == 1 and asset5Found == 0:
                    FU.asset4 = temp
                    facts = appendAsset5(FU.asset3, FU.asset4, facts)
                    asset5Found = 1
                        
                elif asset5Found == 1 and vulnerabilityFound == 0:
                    FU.asset5 = temp
                    values, type = runGUI4()
                    floodlevelForVulnerability, exposure = int(type), int(values)
                    facts = appendVulnerability(facts, type, FU.asset5, exposure)
                    vulnerabilityFound = 1

                elif vulnerabilityFound == 1 and riskFound == 0:
                    FU.vulnerability = temp
                    facts = appendRisk(facts, FU.vulnerability, floodlevelForVulnerability)
                    vulnerabilityFound = 2

                elif vulnerabilityFound == 2:
                    FU.risk = temp
                    runGUI5(FU.risk)
                    riskFound = 1
                    exit()

                else:
                    print("Invalid")
                    exit()


