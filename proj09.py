##############################################################################################################################################
#
#   CSE 231
#   Project 09
#
#   Algorithm
#
#      def open_file():
#
#           prompt for a file_name
#        while loop to repeatedly prompt for a file_name:
#           use try-except method to prevent the program from running errors
#           try :
#               break from the loop if a file is successfully opened
#           except:
#               print Invalid filename  and prompt for a file name
#               go back to the while loop to start from the beginning
#
#
#       def read_file(fp)
#
#           skip the header row of the cvs file
#
#           for loop through the cvs file:
#               assign the value for generation, name and type
#               If type 2 is empty:
#                   then assign it as None
#               # initialize set for each effectiveness
#
#               for loop through line[1: 19]:
#           
#                       if the value of the columns == key of EFFECTIVENESSS dictionary
#                               assign the value to the value of that key
#
#
#                       if val == ability:
#                           add the ability to specific set
#
#               create  a dictionary  add the ability set to the dictionary
#
#               add the dictionary to a list 
#               add other ability values to list based on index given by the project
#
#               
#           if gen not in pokedex:
#    
#               pokedex[gen] = {}
#
#           if typ  not in  pokedex[gen]:
#    
#               pokedex [gen][typ] = {}
#  
#
#           if name not in pokedex[gen][typ]:
#
#               pokedex[gen][typ][name]  = name_list
#
#
#           return Dictionary pokedex
#
#
#       def find_pokemon(pokedex, names):
#  
#           create name_list
#           for loop through the name set
#           name = i
#       
#           for k,v through pokedex.items:
#               for k1, v1 in v.items():
#                   
#                   for k2 in v1.keys():
#                    
#                    append name to name_list
#           d_dic = dict()           
#           for loop through name_list:
#                   add it to set
#
#           for loop again through the nested dictionaries:
#               if name == k2 
#                   then add to d_dic dictionary
#
#           for loop through dictionary:
#               after index add the value to D_list
#               update the dictionary by adding list 
#               return Dictionary
#
#
#
#       def display_pokemon(name, info):
#
#           assign all the appropriate index to string variables
#           such as m3 = info[6] use format statements
#           Add all the variables creating a string Name
#           return Name
#
#
#
#       def find_pokemon_from_abilities(pokedex, abilities):
#
#           for k,v through pokedex.items:
#               for k1, v1 in v.items():
#                
#                   for k2 in v1.keys():
#                     Assign n as the unique elements between abilities set and v2[1]
#                    if abilities set == n
#                       append k2(names) to poke_names set
#           return poke_names
#
#
#
#       def find_matchups(pokedex, name, matchup_type):
#
#           for k,v through pokedex.items:
#            for k1, v1 in v.items():
#                
#                for k2 in v1.keys():
#                    if name == k2:
#                      if k2 == type then assign that specifc value to typ_set
#                       
#
#
#           for loop through the nested dictioa\naries once again:
#               for loop through the type_set:
#                   if type in k1:
#                       if none in type 2 remove None
#                           add name and type to a list of tuples
#           sort the list_tup
#           return list_tup
#
#
#       def main()
#           calls the open_file() and read_file()
#           prompts for user input by printing prompt
#   
#           while prompt is not digit or not "q":
#           print ("Invalid") and prompt till valid input is recieved
#    
#           while prompt is not equalt to "q" or "Q":
#   
#               while check == False:
#                   keep asking for valid input if the user is entering invalid option
#       
#               if user entered option == 1:
#                   prompt for a list of pokemon names 
#                   strip and split the names with comma
#                   for loop through the list:
#                   strip whitespaces and add it to a set
#                   call find_pokemon_from_abilities(pokedex, ability_set) function
#                   for loop through the dictionary returned from the function
#                   print key and values
#    
#               if user entered option == 2:
#                   prompt for a list of pokemon ability names 
#                   strip and split the names with comma
#                   for loop through the list:
#                   strip whitespaces and add it to a set
#                   call find_pokemon_from_abilities(pokedex, ability_set) function
#                   print the set by joining the values of the set
#       
#               if user entered option == 3:
#                   prompt for pokemon name and matchup type
#                   call find_matchups(pokedex, poke_name, match)
#                   if the returned list is empty print "Invalid name"
#                   for for loop through the list of tuple:
#                       print each tuple
#######################################################################################################################################
        



import csv,copy


EFFECTIVENESS = {0.25: "super effective", 0.5: "effective", 1:"normal", 2:"weak", 4:"super weak", 0:"resistant"}
MATCHUP_TYPES = {"resistant", "super effective", "effective", "normal",
                 "weak", "super weak"}
header_list = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fight', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal','poison', 'psychic', 'rock', 'steel', 'water']
PROMPT = '''
\nTo make a selection, please enter an option 1-3:\n
\tOPTION 1: Find Pokemon
\tOPTION 2: Find Pokemon From Abilities
\tOPTION 3: Find Matchups
\nEnter an option: '''

def open_file(s):
    """
    

    Parameters
    ----------
    s : string
        string called pokemon.

    Returns
    -------
    filepointer : valid cvs file
        cvs file with data of pokemon.

    """
   
    
    
    file_name = input("Please enter a pokemon filename: ")
    check = True
    
    while check == True:
        try:
            filepointer = open(file_name,encoding = "utf-8")
            break
        except FileNotFoundError:
            print("This pokemon file does not exist. Please try again.")
            file_name = input("Please enter a pokemon filename: ")
            continue
    
    return filepointer
    
    


def read_file(fp):
    """
    

    Parameters
    ----------
    fp : cvs file
        file with all the data of pokemon.

    Returns
    -------
    nested dictionaries containing data of generation, type of pokemon,
        name of pokemon, list of abilities of pokemon

    """
   
    
    reader = csv.reader(fp) 
    header = next(reader,None)
    
    D = dict()
    m = 0
    typ_dic = dict()
    
    pokedex = dict()
    
    
    name_dic = dict()
    
    

    v = 0 
    
   
    
    for line in reader:
        name_list = []
        pow_dict = dict()
        
        super_effective = set()
        effective = set()
        normal = set()
        weak = set()
        super_weak = set()
        resistance = set()
        
        gen = int(line[39])
        name = line [30]
        
        
        
        type_1 = line[36]
        type_2 = line[37]
        if type_1 == "":
            type_1 = None
        if type_2 == "":
            type_2 = None
        
        typ = (type_1,type_2)
      
        
        
      
        count = 0        
        for i in line [1:19]:
            
            
            
            i = float(i)
        
            if i in EFFECTIVENESS.keys():
                
                val = EFFECTIVENESS[i]
              
                
            if val == "super effective":
                
                super_effective.add(header_list[count])
               
            
            if val == "effective":
                
                effective.add(header_list[count])
              
                
                
            if val == "normal":
                
                normal.add(header_list[count])
                
                
                
            if val == "weak":
                
                weak.add(header_list[count])
                
                
            if val == "super weak":
                
                super_weak.add(header_list[count])
               
                
                
            if val == "resistant":
                
                resistance.add(header_list[count])
               
            
            count += 1
            
        
    
        pow_dict["super effective"] = super_effective
        pow_dict["effective"] = effective
        pow_dict["normal"] = normal
        pow_dict["weak"] = weak
        pow_dict["super weak"] = super_weak
        pow_dict["resistant"] = resistance
        
        name_list.append(pow_dict)
        
        # del pow_dict
       
        
        abilities = line[0]
        abilities = abilities.rstrip("]")
        abilities = abilities.lstrip("[")
        ab_l = abilities.split(", ")
        
        ability_set = set()
        
        q = 0
        for i in ab_l:
            
            i = i.strip("'")
            
            ability_set.add(i)
                
           
                
        name_list.append(ability_set)
        
        name_list.append(int(line[28]))
        name_list.append(int(line[23]))
        name_list.append(float(line[38]))
        name_list.append(int(line[35]))
        
        legend = False
        
        if line [40] == "0":
            
            name_list.append(legend)
        else:
            legend = True
            name_list.append(legend)
        
        
       
        
        
        if gen not in pokedex:
    
    
            pokedex[gen] = {}
            
    
        if typ  not in  pokedex[gen]:
            
           pokedex [gen][typ] = {}
           
        
       
            
        
        if name not in pokedex[gen][typ]:
            
            
            
            pokedex[gen][typ][name]  = name_list
           
            
        
        m += 1
        v += 1  
        
    return(pokedex)
            
            
   
       
        
        
        
       
        
        
           
    
    
    
  


def find_pokemon(pokedex, names):
    """
    

    Parameters
    ----------
    pokedex : dictionary returned from read_file function
        nested dictionries containing data of generation, type of pokemon,
        name of pokemon, list of abilities of pokemon .
    names : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    #pokemon_small.csv
    #pokemon.csv
    
    
    
    
    names_list = []
    
    name_set = set()
    D = dict()
    D_dic = dict()
    
    for i in names:
        
        name = i
        
        for k,v in pokedex.items():
            for k1, v1 in v.items():
                
                for k2 in v1.keys():
                    
                    names_list.append(k2)
                   
                
            
        
    
    for i in names:
        
       
        if i in names_list:
            name_set.add(i)
    
   
        
        
    # print(name_set)
    for i in name_set:
        name = i
        D_list = []
        
        
        for k,v in pokedex.items():
            
            for k1, v1 in v.items():
                
               
                
                for k2, v2 in v1.items():
                   
                    
                    if name == k2:
                        D_dic = v2
                    
                        
                        gen = k
                        typ = k1
                        break
                
                   
                   
    
                    
        
        for i in D_dic[1:]:
            
            D_list.append(i)
            
        D_list.append(gen)  
        D_list.append(typ)
        
        if name not in D:
            
            D[name] = D_list
    
    return(D)
        
        

    
def display_pokemon(name, info):
    """
    

    Parameters
    ----------
    name : string
        name of the pokemon.
    info : list 
        list contains a dictionary of abilities and outside of that dictionary it contains
        other abilities.

    Returns
    -------
    string Name.

    """
   
    # pokemon.csv
    m1 = ("\n")
    m2 = ( "{:<s}".format(name))
    q6 = ""
    
    
        
    m3 =  "{}{}".format("\n\tGen: " , info[6])
    
    if None in info[7]:
        
        m4 =  "{}{}".format("\n\tTypes: " , info[7][0])
          
    else:
        m4 =  "{}{}{}{}".format("\n\tTypes: " , info[7][0],", ", info[7][1])
    
    # m5 = "{}".format("\n\tAbilities:") 
    # m6 = "{}{}".format(" " ,i)
    # print(m1 +m2 + m3 + m4)
    
    length = len(info[0])
    
    count = 0
    for i in sorted(info[0]):
        
        if count == 0:
            m5 = "{}".format("\n\tAbilities:")
        count += 1
        if count == length :
            
            m7 =  "{}{}".format(" " , i )
        
        else:
            m6 =  "{}{}{}".format(" " ,i, ",")
            q6 += m6
    
    m8 = "{}{}".format("\n\tHP: " , info[1])
    m9 =  "{}{}".format("\n\tCapture Rate: ", info[2])
    
    m10 =  "{}{}".format("\n\tWeight: ", info[3])
    
    m11 =  "{}{}".format("\n\tSpeed: ", info[4])
    
    if info[5] == True:
        
        m12 =  "{}".format("\n\tLegendary")
     
    else:
        
        m12 =  "{}{}".format("\n","\tNot Legendary")
    m13 = "\n"
  
            
        
    Name = m1 +m2 +m3 +m4 +m5 +q6 + m7 + m8 + m9 +m10 +m11 + m12
   
    return(Name)
      
    
    
 
    
    

def find_pokemon_from_abilities(pokedex, abilities):
    """
    

    Parameters
    ----------
    pokedex : nested dictionaries returned from read file function
        nested dictionries containing data of generation, type of pokemon,
        name of pokemon, list of abilities of pokemon .
    abilities : TYPE
        DESCRIPTION.

    Returns
    -------
    poke_names : set
        finds the names of pokemons that has the same abilities from that set

    """
   
    
   
    
    poke_names = set()
    
    len_ab = len(abilities) 
    
    count = 0
    
    
        
    
        
    for k,v in pokedex.items():
        
        
            
        for k1, v1 in v.items():
                
               
                
            for k2, v2 in v1.items():
                
                n = abilities & v2[1]
                
                if abilities  == n:
                    poke_names.add(k2)
                
             
                    
    return (poke_names)

                    
def find_matchups(pokedex, name, matchup_type):
    """
    

    Parameters
    ----------
    pokedex : nested dictionaries returned from read file function
        nested dictionries containing data of generation, type of pokemon,
        name of pokemon, list of abilities of pokemon.
        .
    name : string
        name of the pokemon.
    matchup_type : string
        string that contains type effectiveness of the pokemon.

    Returns
    -------
    List of tuples
       List with names and its type of effectivenss in tuple.

    """
   
     
    
    typ_set = set ()
    
    if matchup_type not in EFFECTIVENESS.values():
        
        return (None)
    for k,v in pokedex.items():
        
        
            
        for k1, v1 in v.items():
                
        
               
                
            for k2, v2 in v1.items():
                
                
                
                for key,val in v2[0].items():
                    
                    if name == k2:
                        if matchup_type == key:
                            typ_set = val
                          
    
                        
   
     
    tup = tuple()
    
   
    list_tup = []
    for k,v in pokedex.items():
        
        
            
        for k1, v1 in v.items():
                
            
                
            for k2, v2 in v1.items():
                
                for i in typ_set:
                
                    if i in k1:
                        
                        if None in k1:
                            t = k1[0:-1]
                            tup = (t)
                            
                            
                            list_tup.append((k2,tuple(tup)))
                        else:
                            list_tup.append((k2,tuple(k1)))
                
            
                        
  
                        
    list_tup = sorted(list_tup)
    
    if not list_tup:
        return(None)
    else:
        
        return(list_tup)
                
                
                    
    
   

def main():
    """
    calls the open_file() and read_file()
    prompts for user input by printing prompt
    
    while prompt is not digit or not "q":
        print ("Invalid") and prompt till valid input is recieved
        
    while prompt is not equalt to "q" or "Q":
        
        while check == False:
            keep asking for valid input if the user is entering invalid option
            
        if user entered option == 1:
            prompt for a list of pokemon names 
            strip and split the names with comma
            for loop through the list:
                strip whitespaces and add it to a set
            call find_pokemon_from_abilities(pokedex, ability_set) function
            for loop through the dictionary returned from the function
            print key and values
        
        if user entered option == 2:
            prompt for a list of pokemon ability names 
            strip and split the names with comma
            for loop through the list:
                strip whitespaces and add it to a set
            call find_pokemon_from_abilities(pokedex, ability_set) function
            print the set by joining the values of the set
            
        if user entered option == 3:
            prompt for pokemon name and matchup type
            call find_matchups(pokedex, poke_name, match)
            if the returned list is empty print "Invalid name"
            or for loop through the list of tuple:
                    print each tuple
            
    

    """
    print("Welcome to your personal Pokedex!\n")
    fp = open_file("pokemon")
    pokedex = read_file(fp)
    prompt = input(PROMPT)
    
    while prompt.isdigit() == False and prompt != "q":
        print("Invalid option ", {prompt})
        prompt = input(PROMPT)
    while prompt != "q" and prompt != "Q":
        
        check = False
        while check == False:
            
            if prompt.isdigit():
                
                prompt = int(prompt)
                if prompt > 3 or prompt < 1 :
    
                    print("Invalid option", prompt)
                    prompt = input(PROMPT)
                    check = False
                    continue
                else:
                    check = True 
                    break
            else:
                if prompt == "q" or prompt == "Q":
                    break
                else:
                    print("Invalid option", prompt)
                    prompt = input(PROMPT)
                    check = False
                    continue
            
       
                    
                
            
            
                
        
        
        if prompt == "q" or prompt == "Q":
            break
        prompt = int(prompt)
        if prompt == 1:
            names = input("\nEnter a list of pokemon names, separated by commas: ")
            names = names.strip().split(",")
            name_set = set()
           
            for i in names:
                
                i = i.strip(" ")
                name_set.add(i)
            
            find_poke = find_pokemon(pokedex, sorted(name_set))
            
            
            for key in sorted(find_poke.keys()):
                
                display = display_pokemon(key, find_poke[key])
                print(display)
          
          
        if prompt == 2:
            
            abilities = input("Enter a list of abilities, separated by commas: ")
            
            abilities = abilities.strip().split(",")
            ability_set = set()
           
            for i in abilities:
                
                i = i.strip(" ")
                ability_set.add(i)
                
            find_ability = find_pokemon_from_abilities(pokedex, ability_set)
            
            # find_ability = sorted(find_ability)
            
            print("Pokemon: " , ", ".join(sorted(find_ability)))
            
                
        if prompt == 3:
            
            poke_name = input("Enter a pokemon name: ")
    
                
            match = input("Enter a matchup type: ")
            matchups = find_matchups(pokedex, poke_name, match)
            
            if matchups == None:
                print("Invalid input")
                prompt = input(PROMPT)
                continue
            for i in matchups:
                
                print(i[0] +":", ", ".join(i[1]))
                
               
            
                    
            
            
            
          
            
        prompt = input(PROMPT)
                
    

if __name__ == "__main__":
    main()