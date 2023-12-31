# Rules for appending asset3 facts
# The two numbers represent the lower and upper boundaries of asset3
# The last number represents a placeholder value used for appending the facts
mappingAsset3 = {
    (0, 0): "b",
    (0, 1): "b",
    (1, 1): "b",
    (1, 2): "c",
    (1, 3): "c",
    (2, 2): "c",
    (2, 3): "c",
    (3, 3): 3,
    (3, 4): 3,
    (4, 4): 3,
    (4, 5): 3,
    (5, 5): 3,
    (5, 6): 3,
    (6, 6): 3,
    }

# Rules for appending asset5 facts
# The two numbers represent the lower and upper boundaries of asset5
# The last number represents a placeholder value used for appending the facts
mappingAsset5 = {
    (0, 0): "b",
    (0, 1): "b",
    (1, 1): "b",
    (1, 2): "c",
    (1, 3): "c",
    (2, 2): "c",
    (2, 3): "c",
    (3, 3): 3,
    (3, 4): 3,
    (4, 4): 3,
    (4, 5): 3,
    (5, 5): 3,
    (5, 6): 3,
    (6, 6): 3,
    }

# Rules for appending vulnerability facts
# The two numbers represent the lower and upper boundaries of the vulnerability score
# The last number represents a placeholder value used for appending the facts
mappingVulnerability = {
    (0, 1): "b",
    (1, 2): "c",
    (0, 0): "b",
    (2, 2): "c",
    (1, 1): "b",
    (3, 3): 3,
    (1, 3): "c",
    (2, 3): "c",
    (3, 4): 3,
    (4, 4): 3,
    (4, 5): 3,
    (5, 5): 3,
    (5, 6): 3,
    (6, 6): 3,
    }

from functions import (
    calculateAsset1Residential,
    calculateAsset1Industrial,
    calculateAsset1Recreational,
    calculateAsset2Residential,
    calculateAsset2Industrial,
    calculateAsset2Recreational,
    calculateNonVegetatedSurface,
    calculateVegetatedSurface,
    calculateWaterSurface,
)

#Fill in with [premise, conclusion] for all cases
KB = [
    
    # Rules for asset1 residential
    # Index 0 = 1 represents that it is residential (asset1) and the following 3 indices represent the values of the different variables 
    [1, 1, 1, 1, ["asset1", calculateAsset1Residential(1,1,1)]],
    [1, 1, 1, 2, ["asset1", calculateAsset1Residential(1,1,2)]],
    [1, 1, 1, 3, ["asset1", calculateAsset1Residential(1,1,3)]],
    [1, 1, 2, 1, ["asset1", calculateAsset1Residential(1,2,1)]],
    [1, 1, 2, 2, ["asset1", calculateAsset1Residential(1,2,2)]],
    [1, 1, 2, 3, ["asset1", calculateAsset1Residential(1,2,3)]],
    [1, 1, 3, 1, ["asset1", calculateAsset1Residential(1,3,1)]],
    [1, 1, 3, 2, ["asset1", calculateAsset1Residential(1,3,2)]],
    [1, 1, 3, 3, ["asset1", calculateAsset1Residential(1,3,3)]],
    [1, 2, 1, 1, ["asset1", calculateAsset1Residential(2,1,1)]],
    [1, 2, 1, 2, ["asset1", calculateAsset1Residential(2,1,2)]],
    [1, 2, 1, 3, ["asset1", calculateAsset1Residential(2,1,3)]],
    [1, 2, 2, 1, ["asset1", calculateAsset1Residential(2,2,1)]],
    [1, 2, 2, 2, ["asset1", calculateAsset1Residential(2,2,2)]],
    [1, 2, 2, 3, ["asset1", calculateAsset1Residential(2,2,3)]],
    [1, 2, 3, 1, ["asset1", calculateAsset1Residential(2,3,1)]],
    [1, 2, 3, 2, ["asset1", calculateAsset1Residential(2,3,2)]],
    [1, 2, 3, 3, ["asset1", calculateAsset1Residential(2,3,3)]],
    [1, 3, 1, 1, ["asset1", calculateAsset1Residential(3,1,1)]],
    [1, 3, 1, 2, ["asset1", calculateAsset1Residential(3,1,2)]],
    [1, 3, 1, 3, ["asset1", calculateAsset1Residential(3,1,3)]],
    [1, 3, 2, 1, ["asset1", calculateAsset1Residential(3,2,1)]],
    [1, 3, 2, 2, ["asset1", calculateAsset1Residential(3,2,2)]],
    [1, 3, 2, 3, ["asset1", calculateAsset1Residential(3,2,3)]],
    [1, 3, 3, 1, ["asset1", calculateAsset1Residential(3,3,1)]],
    [1, 3, 3, 2, ["asset1", calculateAsset1Residential(3,3,2)]],
    [1, 3, 3, 3, ["asset1", calculateAsset1Residential(3,3,3)]],

    # Rules for asset1 industrial
    # Index 0 = 2 represents that it is industrial (asset1) and the following 3 indices represent the values of the different variables
    [2, 1, 1, 1, ["asset1", calculateAsset1Industrial(1,1,1)]],
    [2, 1, 1, 2, ["asset1", calculateAsset1Industrial(1,1,2)]],
    [2, 1, 1, 3, ["asset1", calculateAsset1Industrial(1,1,3)]],
    [2, 1, 2, 1, ["asset1", calculateAsset1Industrial(1,2,1)]],
    [2, 1, 2, 2, ["asset1", calculateAsset1Industrial(1,2,2)]],
    [2, 1, 2, 3, ["asset1", calculateAsset1Industrial(1,2,3)]],
    [2, 1, 3, 1, ["asset1", calculateAsset1Industrial(1,3,1)]],
    [2, 1, 3, 2, ["asset1", calculateAsset1Industrial(1,3,2)]],
    [2, 1, 3, 3, ["asset1", calculateAsset1Industrial(1,3,3)]],
    [2, 2, 1, 1, ["asset1", calculateAsset1Industrial(2,1,1)]],
    [2, 2, 1, 2, ["asset1", calculateAsset1Industrial(2,1,2)]],
    [2, 2, 1, 3, ["asset1", calculateAsset1Industrial(2,1,3)]],
    [2, 2, 2, 1, ["asset1", calculateAsset1Industrial(2,2,1)]],
    [2, 2, 2, 2, ["asset1", calculateAsset1Industrial(2,2,2)]],
    [2, 2, 2, 3, ["asset1", calculateAsset1Industrial(2,2,3)]],
    [2, 2, 3, 1, ["asset1", calculateAsset1Industrial(2,3,1)]],
    [2, 2, 3, 2, ["asset1", calculateAsset1Industrial(2,3,2)]],
    [2, 2, 3, 3, ["asset1", calculateAsset1Industrial(2,3,3)]],
    [2, 3, 1, 1, ["asset1", calculateAsset1Industrial(3,1,1)]],
    [2, 3, 1, 2, ["asset1", calculateAsset1Industrial(3,1,2)]],
    [2, 3, 1, 3, ["asset1", calculateAsset1Industrial(3,1,3)]],
    [2, 3, 2, 1, ["asset1", calculateAsset1Industrial(3,2,1)]],
    [2, 3, 2, 2, ["asset1", calculateAsset1Industrial(3,2,2)]],
    [2, 3, 2, 3, ["asset1", calculateAsset1Industrial(3,2,3)]],
    [2, 3, 3, 1, ["asset1", calculateAsset1Industrial(3,3,1)]],
    [2, 3, 3, 2, ["asset1", calculateAsset1Industrial(3,3,2)]],
    [2, 3, 3, 3, ["asset1", calculateAsset1Industrial(3,3,3)]],
 
    # Rules for asset1 recreational
    # Index 0 = 3 represents that it is recreational (asset1) and the following 3 indices represent the values of the different variables
    [3, 1, 1, 1, ["asset1", calculateAsset1Recreational(1,1,1)]],
    [3, 1, 1, 2, ["asset1", calculateAsset1Recreational(1,1,2)]],
    [3, 1, 1, 3, ["asset1", calculateAsset1Recreational(1,1,3)]],
    [3, 1, 2, 1, ["asset1", calculateAsset1Recreational(1,2,1)]],
    [3, 1, 2, 2, ["asset1", calculateAsset1Recreational(1,2,2)]],
    [3, 1, 2, 3, ["asset1", calculateAsset1Recreational(1,2,3)]],
    [3, 1, 3, 1, ["asset1", calculateAsset1Recreational(1,3,1)]],
    [3, 1, 3, 2, ["asset1", calculateAsset1Recreational(1,3,2)]],
    [3, 1, 3, 3, ["asset1", calculateAsset1Recreational(1,3,3)]],
    [3, 2, 1, 1, ["asset1", calculateAsset1Recreational(2,1,1)]],
    [3, 2, 1, 2, ["asset1", calculateAsset1Recreational(2,1,2)]],
    [3, 2, 1, 3, ["asset1", calculateAsset1Recreational(2,1,3)]],
    [3, 2, 2, 1, ["asset1", calculateAsset1Recreational(2,2,1)]],
    [3, 2, 2, 2, ["asset1", calculateAsset1Recreational(2,2,2)]],
    [3, 2, 2, 3, ["asset1", calculateAsset1Recreational(2,2,3)]],
    [3, 2, 3, 1, ["asset1", calculateAsset1Recreational(2,3,1)]],
    [3, 2, 3, 2, ["asset1", calculateAsset1Recreational(2,3,2)]],
    [3, 2, 3, 3, ["asset1", calculateAsset1Recreational(2,3,3)]],
    [3, 3, 1, 1, ["asset1", calculateAsset1Recreational(3,1,1)]],
    [3, 3, 1, 2, ["asset1", calculateAsset1Recreational(3,1,2)]],
    [3, 3, 1, 3, ["asset1", calculateAsset1Recreational(3,1,3)]],
    [3, 3, 2, 1, ["asset1", calculateAsset1Recreational(3,2,1)]],
    [3, 3, 2, 2, ["asset1", calculateAsset1Recreational(3,2,2)]],
    [3, 3, 2, 3, ["asset1", calculateAsset1Recreational(3,2,3)]],
    [3, 3, 3, 1, ["asset1", calculateAsset1Recreational(3,3,1)]],
    [3, 3, 3, 2, ["asset1", calculateAsset1Recreational(3,3,2)]],
    [3, 3, 3, 3, ["asset1", calculateAsset1Recreational(3,3,3)]],
 
    #asset2
    # Rules for asset2 residential
    # Index 0 = 4 represents that it is residential (asset2) and the following 3 indices represent the values of the different variables
    [4, 1, 1, 1, ["asset2", calculateAsset2Residential(1,1,1)]],
    [4, 1, 1, 2, ["asset2", calculateAsset2Residential(1,1,2)]],
    [4, 1, 1, 3, ["asset2", calculateAsset2Residential(1,1,3)]],
    [4, 1, 2, 1, ["asset2", calculateAsset2Residential(1,2,1)]],
    [4, 1, 2, 2, ["asset2", calculateAsset2Residential(1,2,2)]],
    [4, 1, 2, 3, ["asset2", calculateAsset2Residential(1,2,3)]],
    [4, 1, 3, 1, ["asset2", calculateAsset2Residential(1,3,1)]],
    [4, 1, 3, 2, ["asset2", calculateAsset2Residential(1,3,2)]],
    [4, 1, 3, 3, ["asset2", calculateAsset2Residential(1,3,3)]],
    [4, 2, 1, 1, ["asset2", calculateAsset2Residential(2,1,1)]],
    [4, 2, 1, 2, ["asset2", calculateAsset2Residential(2,1,2)]],
    [4, 2, 1, 3, ["asset2", calculateAsset2Residential(2,1,3)]],
    [4, 2, 2, 1, ["asset2", calculateAsset2Residential(2,2,1)]],
    [4, 2, 2, 2, ["asset2", calculateAsset2Residential(2,2,2)]],
    [4, 2, 2, 3, ["asset2", calculateAsset2Residential(2,2,3)]],
    [4, 2, 3, 1, ["asset2", calculateAsset2Residential(2,3,1)]],
    [4, 2, 3, 2, ["asset2", calculateAsset2Residential(2,3,2)]],
    [4, 2, 3, 3, ["asset2", calculateAsset2Residential(2,3,3)]],
    [4, 3, 1, 1, ["asset2", calculateAsset2Residential(3,1,1)]],
    [4, 3, 1, 2, ["asset2", calculateAsset2Residential(3,1,2)]],
    [4, 3, 1, 3, ["asset2", calculateAsset2Residential(3,1,3)]],
    [4, 3, 2, 1, ["asset2", calculateAsset2Residential(3,2,1)]],
    [4, 3, 2, 2, ["asset2", calculateAsset2Residential(3,2,2)]],
    [4, 3, 2, 3, ["asset2", calculateAsset2Residential(3,2,3)]],
    [4, 3, 3, 1, ["asset2", calculateAsset2Residential(3,3,1)]],
    [4, 3, 3, 2, ["asset2", calculateAsset2Residential(3,3,2)]],
    [4, 3, 3, 3, ["asset2", calculateAsset2Residential(3,3,3)]],

    # Rules for asset2 industrial
    # Index 0 = 5 represents that it is industrial (asset2) and the following 3 indices represent the values of the different variables
    [5, 1, 1, 1, ["asset2", calculateAsset2Industrial(1,1,1)]],
    [5, 1, 1, 2, ["asset2", calculateAsset2Industrial(1,1,2)]],
    [5, 1, 1, 3, ["asset2", calculateAsset2Industrial(1,1,3)]],
    [5, 1, 2, 1, ["asset2", calculateAsset2Industrial(1,2,1)]],
    [5, 1, 2, 2, ["asset2", calculateAsset2Industrial(1,2,2)]],
    [5, 1, 2, 3, ["asset2", calculateAsset2Industrial(1,2,3)]],
    [5, 1, 3, 1, ["asset2", calculateAsset2Industrial(1,3,1)]],
    [5, 1, 3, 2, ["asset2", calculateAsset2Industrial(1,3,2)]],
    [5, 1, 3, 3, ["asset2", calculateAsset2Industrial(1,3,3)]],
    [5, 2, 1, 1, ["asset2", calculateAsset2Industrial(2,1,1)]],
    [5, 2, 1, 2, ["asset2", calculateAsset2Industrial(2,1,2)]],
    [5, 2, 1, 3, ["asset2", calculateAsset2Industrial(2,1,3)]],
    [5, 2, 2, 1, ["asset2", calculateAsset2Industrial(2,2,1)]],
    [5, 2, 2, 2, ["asset2", calculateAsset2Industrial(2,2,2)]],
    [5, 2, 2, 3, ["asset2", calculateAsset2Industrial(2,2,3)]],
    [5, 2, 3, 1, ["asset2", calculateAsset2Industrial(2,3,1)]],
    [5, 2, 3, 2, ["asset2", calculateAsset2Industrial(2,3,2)]],
    [5, 2, 3, 3, ["asset2", calculateAsset2Industrial(2,3,3)]],
    [5, 3, 1, 1, ["asset2", calculateAsset2Industrial(3,1,1)]],
    [5, 3, 1, 2, ["asset2", calculateAsset2Industrial(3,1,2)]],
    [5, 3, 1, 3, ["asset2", calculateAsset2Industrial(3,1,3)]],
    [5, 3, 2, 1, ["asset2", calculateAsset2Industrial(3,2,1)]],
    [5, 3, 2, 2, ["asset2", calculateAsset2Industrial(3,2,2)]],
    [5, 3, 2, 3, ["asset2", calculateAsset2Industrial(3,2,3)]],
    [5, 3, 3, 1, ["asset2", calculateAsset2Industrial(3,3,1)]],
    [5, 3, 3, 2, ["asset2", calculateAsset2Industrial(3,3,2)]],
    [5, 3, 3, 3, ["asset2", calculateAsset2Industrial(3,3,3)]],

    # Rules for asset2 recreational
    # Index 0 = 6 represents that it is recreational (asset2) and the following 3 indices represent the values of the different variables
    [6, 1, 1, 1, ["asset2", calculateAsset2Recreational(1,1,1)]],
    [6, 1, 1, 2, ["asset2", calculateAsset2Recreational(1,1,2)]],
    [6, 1, 1, 3, ["asset2", calculateAsset2Recreational(1,1,3)]],
    [6, 1, 2, 1, ["asset2", calculateAsset2Recreational(1,2,1)]],
    [6, 1, 2, 2, ["asset2", calculateAsset2Recreational(1,2,2)]],
    [6, 1, 2, 3, ["asset2", calculateAsset2Recreational(1,2,3)]],
    [6, 1, 3, 1, ["asset2", calculateAsset2Recreational(1,3,1)]],
    [6, 1, 3, 2, ["asset2", calculateAsset2Recreational(1,3,2)]],
    [6, 1, 3, 3, ["asset2", calculateAsset2Recreational(1,3,3)]],
    [6, 2, 1, 1, ["asset2", calculateAsset2Recreational(2,1,1)]],
    [6, 2, 1, 2, ["asset2", calculateAsset2Recreational(2,1,2)]],
    [6, 2, 1, 3, ["asset2", calculateAsset2Recreational(2,1,3)]],
    [6, 2, 2, 1, ["asset2", calculateAsset2Recreational(2,2,1)]],
    [6, 2, 2, 2, ["asset2", calculateAsset2Recreational(2,2,2)]],
    [6, 2, 2, 3, ["asset2", calculateAsset2Recreational(2,2,3)]],
    [6, 2, 3, 1, ["asset2", calculateAsset2Recreational(2,3,1)]],
    [6, 2, 3, 2, ["asset2", calculateAsset2Recreational(2,3,2)]],
    [6, 2, 3, 3, ["asset2", calculateAsset2Recreational(2,3,3)]],
    [6, 3, 1, 1, ["asset2", calculateAsset2Recreational(3,1,1)]],
    [6, 3, 1, 2, ["asset2", calculateAsset2Recreational(3,1,2)]],
    [6, 3, 1, 3, ["asset2", calculateAsset2Recreational(3,1,3)]],
    [6, 3, 2, 1, ["asset2", calculateAsset2Recreational(3,2,1)]],
    [6, 3, 2, 2, ["asset2", calculateAsset2Recreational(3,2,2)]],
    [6, 3, 2, 3, ["asset2", calculateAsset2Recreational(3,2,3)]],
    [6, 3, 3, 1, ["asset2", calculateAsset2Recreational(3,3,1)]],
    [6, 3, 3, 2, ["asset2", calculateAsset2Recreational(3,3,2)]],
    [6, 3, 3, 3, ["asset2", calculateAsset2Recreational(3,3,3)]],

    # Rules for asset3
    # Index 0 = 13 represents that it is asset3 and the following 2 indices represent the values of the different variables
    [13, 3, 3, ["asset3", 3]],
    [13, 3, "c", ["asset3", 3]],
    [13, 3, "b", ["asset3", 2]],

    [13, "c", 3, ["asset3", 3]],
    [13, "c", "c", ["asset3", 3]],
    [13, "c", "b", ["asset3", 2]],

    [13, "b", 3, ["asset3", 2]],
    [13, "b", "c", ["asset3", 2]],
    [13, "b", "b", ["asset3", 1]],

    # Rules for asset4 nonvegetatedsurface
    # Index 0 = 7 represents that it is asset4 (non-vegetated) and the following 2 indices represent the values of the different variables
    [7, 1, 1, ["asset4", calculateNonVegetatedSurface(1, 1)]],
    [7, 1, 2, ["asset4", calculateNonVegetatedSurface(1, 2)]],
    [7, 1, 3, ["asset4", calculateNonVegetatedSurface(1, 3)]],
    [7, 2, 1, ["asset4", calculateNonVegetatedSurface(2, 1)]],
    [7, 2, 2, ["asset4", calculateNonVegetatedSurface(2, 2)]],
    [7, 2, 3, ["asset4", calculateNonVegetatedSurface(2, 3)]],
    [7, 3, 1, ["asset4", calculateNonVegetatedSurface(3, 1)]],
    [7, 3, 2, ["asset4", calculateNonVegetatedSurface(3, 2)]],
    [7, 3, 3, ["asset4", calculateNonVegetatedSurface(3, 3)]],

    # Rules for asset4 vegetatedsurface
    # Index 0 = 8 represents that it is asset4 (vegetated) and the following 2 indices represent the values of the different variables
    [8, 1, 1, ["asset4", calculateVegetatedSurface(1, 1)]],
    [8, 1, 2, ["asset4", calculateVegetatedSurface(1, 2)]],
    [8, 1, 3, ["asset4", calculateVegetatedSurface(1, 3)]],
    [8, 2, 1, ["asset4", calculateVegetatedSurface(2, 1)]],
    [8, 2, 2, ["asset4", calculateVegetatedSurface(2, 2)]],
    [8, 2, 3, ["asset4", calculateVegetatedSurface(2, 3)]],
    [8, 3, 1, ["asset4", calculateVegetatedSurface(3, 1)]],
    [8, 3, 2, ["asset4", calculateVegetatedSurface(3, 2)]],
    [8, 3, 3, ["asset4", calculateVegetatedSurface(3, 3)]],

    # Rules for asset4 watersurface
    # Index 0 = 9 represents that it is asset4 (water) and the following 2 indices represent the values of the different variables
    [9, 1, 1, ["asset4", calculateWaterSurface(1, 1)]],
    [9, 1, 2, ["asset4", calculateWaterSurface(1, 2)]],
    [9, 1, 3, ["asset4", calculateWaterSurface(1, 3)]],
    [9, 2, 1, ["asset4", calculateWaterSurface(2, 1)]],
    [9, 2, 2, ["asset4", calculateWaterSurface(2, 2)]],
    [9, 2, 3, ["asset4", calculateWaterSurface(2, 3)]],
    [9, 3, 1, ["asset4", calculateWaterSurface(3, 1)]],
    [9, 3, 2, ["asset4", calculateWaterSurface(3, 2)]],
    [9, 3, 3, ["asset4", calculateWaterSurface(3, 3)]],

    # Rules for asset5
    # Index 0 = 12 represents that it is asset5 and the following 2 indices represent the values of the different variables
    [12, 3, 3, ["asset5", 3]],
    [12, 3, "c", ["asset5", 2]],
    [12, 3, "b", ["asset5", 2]],

    [12, "c", 3, ["asset5", 3]],
    [12, "c", "c", ["asset5", 2]],
    [12, "c", "b", ["asset5", 1]],

    [12, "b", 3, ["asset5", 2]],
    [12, "b", "c", ["asset5", 1]],
    [12, "b", "b", ["asset5", 1]],

    # Rules for vulnerability
    # Index 0 = 10 represents that it is vulnerability and the following 3 indices represent the values of the different variables
    [10, 1, 3, 3, ["vulnerability", 5]],
    [10, 1, 3, "a", ["vulnerability", 4]],
    [10, 1, 3, 0, ["vulnerability", 2]],

    [10, 1, "c", 3, ["vulnerability", 4]],
    [10, 1, "c", "a", ["vulnerability", 3]],
    [10, 1, "c", 0, ["vulnerability", 2]],

    [10, 1, "b", 3, ["vulnerability", 2]],
    [10, 1, "b", "a", ["vulnerability", 3]],
    [10, 1, "b", 0, ["vulnerability", 1]],
    
    [10 , 3, 3, 3, ["vulnerability", 5]],
    [10 , 3, 3, "a", ["vulnerability", 5]],
    [10 , 3, 3, 0, ["vulnerability", 3]],

    [10, 3, "c", 3, ["vulnerability", 4]],
    [10, 3, "c", "a", ["vulnerability", 4]],
    [10, 3, "c", 0, ["vulnerability", 3]],

    [10, 3, "b", 3, ["vulnerability", 4]],
    [10, 3, "b", "a", ["vulnerability", 4]],
    [10, 3, "b", 0, ["vulnerability", 2]],

    [10, 5, 3, 3, ["vulnerability", 5]],
    [10, 5, 3, "a", ["vulnerability", 5]],
    [10, 5, 3, 0, ["vulnerability", 4]],

    [10, 5, "c", 3, ["vulnerability", 5]],
    [10, 5, "c", "a", ["vulnerability", 4]],
    [10, 5, "c", 0, ["vulnerability", 3]],

    [10, 5, "b", 3, ["vulnerability", 4]],
    [10, 5, "b", "a", ["vulnerability", 4]],
    [10, 5, "b", 0, ["vulnerability", 3]], 

    # Rules for risk
    # Index 0 = 11 represents that it is risk and the following 2 indices represent the values of the different variables
    [11, 5, 1, ["risk", "VH"]],
    [11, 5, 3, ["risk", "VH"]],
    [11, 5, 5, ["risk", "H"]],

    [11, 4, 1, ["risk", "VH"]],
    [11, 4, 3, ["risk", "H"]],
    [11, 4, 5, ["risk", "M"]],

    [11, 3, 1, ["risk", "VH"]],
    [11, 3, 3, ["risk", "M"]],
    [11, 3, 5, ["risk", "L"]],

    [11, 2, 1, ["risk", "H"]],
    [11, 2, 3, ["risk", "L"]],
    [11, 2, 5, ["risk", "VL"]],

    [11, 1, 1, ["risk", "M"]],
    [11, 1, 3, ["risk", "L"]],
    [11, 1, 5, ["risk", "VL"]],
]


