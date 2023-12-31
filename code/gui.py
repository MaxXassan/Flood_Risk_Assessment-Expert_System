import PySimpleGUI as sg

# Reading input for the "current FU type". FU is Functional Unit
def runGUI():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.

    layoutFUType = [ 
        [sg.Text("CURRENT FUNCTIONAL UNIT", font = "bold")],
        [sg.Text('(What is the current function of the area?)')],
        [sg.Text('(Input either "Residential", "Industrial" or "Recreational")')],
        [sg.Button('Residential'), sg.Button('Industrial'), sg.Button('Recreational')],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    layoutResidential = [
        [sg.Text("CURRENT FUNCTIONAL UNIT", font = "bold")],
        [sg.Text('What is the built-up density of the functional unit?')],
        [sg.Text("(How covered by buildings the land is, given as a percentage)")],
        [sg.Text("(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('What is the building height?')], 
        [sg.Text("(Average height of the present buildings. As per industry standards, rated as either <15m or >15m.)")], 
        [sg.Text("(< 15m? input: 1, >15m? input: 2")], 
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('What is the minimum green area?')],
        [sg.Text('(Minimum required space for green areas, given as a percentage)')],
        [sg.Text('(< 20%? input: 3, between 40% and 60% input 2, > 60% input 1)')],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    layoutIndustrial= [
        [sg.Text("CURRENT FUNCTIONAL UNIT", font = "bold")], 
        [sg.Text('What is the built-up density of the area of the functional unit?')],
        [sg.Text("(How covered by buildings the land is, given as a percentage)")],
        [sg.Text("(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('What is the max allowed residential area?')], 
        [sg.Text('(Maximum allowed space for things like apartments/other communal buildings in the industrial zone on the land. Given as a percentage.)')], 
        [sg.Text("(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('How present is critical infrastructure in the area?')], 
        [sg.Text('(Infrastructure integral to public transport & general societal function roads, tunnels, bridges etc).')],
        [sg.Text("(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Button('Ok'), sg.Button('Cancel')] 
    ]

    layoutRecreational= [ 
        [sg.Text("CURRENT FUNCTIONAL UNIT", font = "bold")],
        [sg.Text('What is the built-up density of the area?')],
        [sg.Text('The maximum allowed space for buildings within the green areas. Given as a percentage.')], 
        [sg.Text("(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('What is the minimum area of recreational space needed?')], 
        [sg.Text('(Minimum required recreational area on the land. Given as a percentage)')], 
        [sg.Text("(< 20%? input: 3, between 40% and 60%? input: 2, >60%? input: 1)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('What is the mininum density of high woody vegetation?')],
        [sg.Text('(Minimum density needed of trees and forested areas on the land. Given as a percentage.)')],
        [sg.Text("(< 20%? input: 3, between 40% and 60%? input: 2, >60%? input: 1)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Button('Ok'), sg.Button('Cancel')] 
    ]

    # Create the Windows
    windowFUType = sg.Window('window', layoutFUType)
    windowResidential= sg.Window('window',layoutResidential)
    windowIndustrial= sg.Window('window', layoutIndustrial)
    windowRecreational = sg.Window('window', layoutRecreational)

    open1 = 0
    open2 = 0
    
    # Event Loop to process "events" and get the "values" of the inputs
    while open1 == 0:
        event, values = windowFUType.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
            break
        # Type = event
        type = event
        open1 = 1
    windowFUType.close()

    while open2 == 0:
        if type == "Residential":
            event, values = windowResidential.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
        elif type == "Industrial":
            event, values = windowIndustrial.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
        elif type == "Recreational":
            event, values = windowRecreational.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
            
    # Closing the windows
    if type == "Residential":
        windowResidential.close()
    elif type == "Industrial":
        windowIndustrial.close()
    elif type == "Recreational":
        windowRecreational.close()

    values = list(values.values())

    # Convert to int
    for i in range(len(values)):
        values[i] = int(values[i])
    
    return values, type

# Reading input for the "planned FU type"
def runGUI2():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.

    layoutFUType = [ 
        [sg.Text("PLANNED FUNCTIONAL UNIT", font = "bold")],
        [sg.Text('(What is the planned function of the area?)')],
        [sg.Text('(Input either "Residential", "Industrial" or "Recreational")')],
        [sg.Button('Residential'), sg.Button('Industrial'), sg.Button('Recreational')],

        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    layoutResidential = [
        [sg.Text("PLANNED FUNCTIONAL UNIT", font = "bold")],
        [sg.Text('What is the built-up density of the functional unit?')],
        [sg.Text("(How covered by buildings the land is, given as a percentage)")],
        [sg.Text("(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('What is the building height?')], 
        [sg.Text("(Average height of the present buildings. As per industry standards, rated as either <15m or >15m.)")], 
        [sg.Text("(< 15m? input: 1, >15m? input: 2")], 
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('What is the minimum green area?')],
        [sg.Text('(Minimum required space for green areas, given as a percentage)')],
        [sg.Text('(< 20%? input: 3, between 40% and 60% input 2, > 60% input 1)')],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    layoutIndustrial= [
        [sg.Text("PLANNED FUNCTIONAL UNIT", font = "bold")], 
        [sg.Text('What is the built-up density of the area of the functional unit?')],
        [sg.Text("(How covered by buildings the land is, given as a percentage)")],
        [sg.Text("(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('What is the max allowed residential area?')], 
        [sg.Text('(Maximum allowed space for things like apartments/other communal buildings in the industrial zone on the land. Given as a percentage.)')], 
        [sg.Text("(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('How present is critical infrastructure in the area?')], 
        [sg.Text('(Infrastructure integral to public transport & general societal function roads, tunnels, bridges etc).')],
        [sg.Text("(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Button('Ok'), sg.Button('Cancel')] 
    ]

    layoutRecreational= [ 
        [sg.Text("PLANNED FUNCTIONAL UNIT", font = "bold")],
        [sg.Text('What is the built-up density of the area?')],
        [sg.Text('The maximum allowed space for buildings within the green areas. Given as a percentage.')], 
        [sg.Text("(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('What is the minimum area of recreational space needed?')], 
        [sg.Text('(Minimum required recreational area on the land. Given as a percentage)')], 
        [sg.Text("(< 20%? input: 3, between 40% and 60%? input: 2, >60%? input: 1)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('What is the mininum density of high woody vegetation?')],
        [sg.Text('(Minimum density needed of trees and forested areas on the land. Given as a percentage.)')],
        [sg.Text("(< 20%? input: 3, between 40% and 60%? input: 2, >60%? input: 1)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Button('Ok'), sg.Button('Cancel')] 
    ]

    # Create the Windows
    windowFUType = sg.Window('window', layoutFUType)
    windowResidential= sg.Window('window',layoutResidential)
    windowIndustrial= sg.Window('window', layoutIndustrial)
    windowRecreational = sg.Window('window', layoutRecreational)
    
    open1 = 0
    open2 = 0
    
    # Event Loop to process "events" and get the "values" of the inputs
    while open1 == 0:
        event, values = windowFUType.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
            break
        # Type = values[0]
        type = event
        open1 = 1
    windowFUType.close()

    while open2 == 0:
        if type == "Residential":
            event, values = windowResidential.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
        elif type == "Industrial":
            event, values = windowIndustrial.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
        elif type == "Recreational":
            event, values = windowRecreational.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1

    # Closing the windows      
    if type == "Residential":
        windowResidential.close()
    elif type == "Industrial":
        windowIndustrial.close()
    elif type == "Recreational":
        windowRecreational.close()

    values = list(values.values())

    # Convert to int
    for i in range(len(values)):
        values[i] = int(values[i])

    return values, type

# Reading input for the land cover of the FU
def runGUI3():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.

    layoutLandCover = [ 
        [sg.Text('What does the surface of the area consist of?')], 
        [sg.Text('(Input either "Non-Vegetated Surface", "Vegetated Surface" or "Water")')], 
        [sg.Button('Non-Vegetated Surface'), sg.Button('Vegetated Surface'), sg.Button('Water')],

        [sg.Button('Ok'), sg.Button('Cancel')]
    ]
    layoutNonVegetatedSurface = [
        [sg.Text('What is the area of the artificially sealed surface?')],
        [sg.Text('(Land covered by artifical constructions; buildings, carparks, roads etc)')],
        [sg.Text("(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)")],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('What is the area of the buildings?')], 
        [sg.Text('(Area of the buildings, given as a percentage)')], 
        [sg.Text("(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)")], 
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Button('Ok'), sg.Button('Cancel')] 
    ]

    layoutVegetatedSurface = [ 
        [sg.Text('What is the area of woody vegetation?')], 
        [sg.Text('(Land covered by forest areas, tall trees, parks etc)')], 
        [sg.Text('20%? input: 3, between 40% and 60%? input: 2, >60%? input: 1).')], 
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('What is the area of cultivated land?')],
        [sg.Text('(Area of land set aside for agricultural purposes necessary to provide food to the public. Given as a percentage.)')],
        [sg.Text('(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)')], 
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Button('Ok'), sg.Button('Cancel')] 
    ]

    layoutWater= [ 
        [sg.Text('What is the area of permanent water?')], 
        [sg.Text('(How much of the land is taken up by something like a lake or quarry etc. Given as a percentage.)')], 
        [sg.Text('(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)')], 
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Text('What is the area of temporary water?')], 
        [sg.Text('(Area of the land covered in water that can be removed, such as fountain installments or temporary reservoirs)')], 
        [sg.Text('(< 20%? input: 3, between 40% and 60%? input: 2, >60%? input: 1)')],
        [sg.Slider(range=(1, 3), default_value=1, orientation='h', size=(15, 20), key='slider')],

        [sg.Button('Ok'), sg.Button('Cancel')] 
    ]

    # Create the Windows
    windowLandCover = sg.Window('window', layoutLandCover)
    windowNonVegetatedSurface= sg.Window('window',layoutNonVegetatedSurface)
    windowVegetatedSurface= sg.Window('window', layoutVegetatedSurface)
    windowWater = sg.Window('window', layoutWater)
    
    open1 = 0
    open2 = 0
    
    # Event Loop to process "events" and get the "values" of the inputs
    while open1 == 0:
        event, values = windowLandCover.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
            break
        #type = values[0]
        type = event
        open1 = 1
    windowLandCover.close()

    while open2 == 0:
        if type == "Non-Vegetated Surface":
            event, values = windowNonVegetatedSurface.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
        elif type == "Vegetated Surface":
            event, values = windowVegetatedSurface.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
        elif type == "Water":
            event, values = windowWater.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1

    # Closing the windows  
    if type == "Non-Vegetated Surface":
        windowNonVegetatedSurface.close()
    elif type == "Vegetated Surface":
        windowVegetatedSurface.close()
    elif type == "Water":
        windowWater.close()

    values = list(values.values())

    # Convert to int
    for i in range(len(values)):
        values[i] = int(values[i])
    
    return values, type

# Reading the input for the flooding levels in the FU
def runGUI4():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.

    layoutFloodLevel = [ 
        [sg.Text('What is the flooding level?')],
        [sg.Text('(Amount of expected flooding due to rainfall averages and general weather patterns.)')],
        [sg.Text('(Input either 1 for 1 meter, 3 for 3 meters, 5 for 5 meters)')], 
        [sg.Button('1'), sg.Button('3'), sg.Button('5')],

        [sg.Button('Ok'), sg.Button('Cancel')]
    ]

    layoutOneM = [
        [sg.Text('What is the percentage of land affected by the flooding?')], 
        [sg.Text('(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)')], 
        [sg.Button('1'), sg.Button('2'), sg.Button('3')],

        [sg.Button('Ok'), sg.Button('Cancel')] 
    ]

    layoutThreeM = [ 
        [sg.Text('What is the percentage of land affected by the flooding?')], 
        [sg.Text('(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)')], 
        [sg.Button('1'), sg.Button('2'), sg.Button('3')],

        [sg.Button('Ok'), sg.Button('Cancel')] 
    ]

    layoutFiveM = [ 
        [sg.Text('What is the percentage of land affected by the flooding?')], 
        [sg.Text('(< 20%? input: 1, between 40% and 60%? input: 2, >60%? input: 3)')], 
        [sg.Button('1'), sg.Button('2'), sg.Button('3')],

        [sg.Button('Ok'), sg.Button('Cancel')] 
    ]
    
    # Create the Windows
    windowFloodLevel = sg.Window('window', layoutFloodLevel)
    windowOneM = sg.Window('window',layoutOneM)
    windowThreeM = sg.Window('window', layoutThreeM)
    windowFiveM = sg.Window('window', layoutFiveM)
    open1 = 0
    open2 = 0
    
    # Event Loop to process "events" and get the "values" of the inputs
    while open1 == 0:
        event, values = windowFloodLevel.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        #type = values[0]
        type = event
        open1 = 1
    windowFloodLevel.close()

    while open2 == 0:
        if type == "1":
            event, values = windowOneM.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
        elif type == "3":
            event, values = windowThreeM.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
        elif type == "5":
            event, values = windowFiveM.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
        
    # Closing the windows     
    if type == "1":
        windowOneM.close()
    elif type == "3":
        windowThreeM.close()
    elif type == "5":
        windowFiveM.close()
    return event, type

# Generating a window that produces the final output
def runGUI5(risk):
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.

    layoutOutputAcceptable = [ 
        [sg.Text('The planned type of the functional unit/zone (FU) is acceptable.' )],
        [sg.Text('For the administrator/end-user this means that there is no need of additional indicators of risk impact monitoring, nor additional measures for strengthening resilience (administrative, technical, financial, infrastructure, etc.)')],
        [sg.Button('Close')]
    ]

    layoutOutputAcceptableModerateRestrictions = [ 
        [sg.Text('The planned type of the functional unit/zone (FU) is acceptable with additional soft measures as moderate restrictions and additional risk assessment parameters for the total area of the FU or for a part of the area.')],
        [sg.Text('These moderate restrictions refer to:')],
        [sg.Text('regular monitoring of territorial management of the FU territory with respect to the applied restrictions;')],
        [sg.Text('application of certain limitation with respect to the build-up density, the type of constructions applied and application of potential risk warning system.')],
        [sg.Button('Close')]
    ]

    layoutOutputAcceptableMajorRestrictions = [ 
        [sg.Text('The planned type of the functional unit/zone is acceptable for clearly defined part of the FU with low or medium risk level with additional soft measures as defined under risk level 2.')],
        [sg.Text('For the other part of the FU area major restrictions must be applied; in cases of uncertainty, such major restrictions must be applied for the whole FU area.')],
        [sg.Text('These restrictions refer to:')], 
        [sg.Text('certain limitation in territorial planning/management parameters, with respect to the build-up density, the type of constructions applied, and the establishment of buffer zones where construction will be limited;')],
        [sg.Text('regular monitoring of changes; application of potential risk warning system; construction of elements protective infrastructure on vulnerable areas; adoption of a real-time emergency response and prevention plan.')],
        [sg.Button('Close')]
    ]

    layoutOutputAcceptableModifications= [ 
        [sg.Text('The planned type of the functional unit/zone is acceptable with strong modifications.')],
        [sg.Text('In addition to the presented above measures, this implies modification of the parameters of the built-up density and building height, establishment of buffer zones,')],
        [sg.Text('restriction rules and construction of the protection infrastructure (ditches, walls/dykes, drainage channels, prevention - network of sensors and additional emergency infrastructure).')],
        [sg.Button('Close')]
    ]

    layoutOutputNotAcceptable= [ 
        [sg.Text('The planned type of the functional zone is not acceptable.')],
        [sg.Text('Other functional type having lower risk score should be proposed or the area may be used as a emergency sector, bearing the pressure of the flood.')],
        [sg.Text('Any significant elements of the urban infrastructure should not be allowed.')],
        [sg.Button('Close')]
    ]

    # Creating the windows
    windowOutputAcceptable = sg.Window('window', layoutOutputAcceptable)
    windowOutputAcceptableModerateRestrictions = sg.Window('window', layoutOutputAcceptableModerateRestrictions)
    windowOutputAcceptableMajorRestrictions = sg.Window('window', layoutOutputAcceptableMajorRestrictions)
    windowOutputAcceptableModifications = sg.Window('window', layoutOutputAcceptableModifications)
    windowOutputNotAcceptable = sg.Window('window', layoutOutputNotAcceptable)
    
    # Event Loop to process "events" and deliver the final message
    open2 = 0
    while open2 == 0:
        if risk == "VH":
            event = windowOutputNotAcceptable.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
        elif risk== "H":
            event = windowOutputAcceptableModifications.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
        elif risk == "M":
            event = windowOutputAcceptableMajorRestrictions.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
        elif risk == "L":
            event = windowOutputAcceptableModerateRestrictions.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
        elif risk == "VL":
            event = windowOutputAcceptable.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # If user closes window or clicks cancel
                break
            open2 = 1
            
    # Closing the windows
    if risk == "VH":
        windowOutputNotAcceptable.close()
    elif risk == "H":
        windowOutputAcceptableModifications.close()
    elif risk == "M":
        windowOutputAcceptableMajorRestrictions.close()
    elif risk == "L":
        windowOutputAcceptableModerateRestrictions.close()
    elif risk == "VL":
        windowOutputAcceptable.close()


def runStartPage():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layoutStartPage = [ 
        [sg.Text('Welcome to the Flood Risk Assessment Tool!')],
        [sg.Text('This tool is designed to help you assess the flood risk in your area.')],
        [sg.Text('Please click on the button below to start the assessment.')],
        [sg.Button('Start')],
        [sg.Button('Cancel')]
    ]
    # Create the window
    windowStartPage = sg.Window('window', layoutStartPage)
    # Event Loop to process "events"
    while True:
        event, values = windowStartPage.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            exit()
            break
        if event == 'Start':
            windowStartPage.close()
            break
    windowStartPage.close()
