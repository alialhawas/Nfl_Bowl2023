import re

# By crateing a posions as dic with a defult values
pos_dic = {
    'QB':0,
    'RB':0,
    'WR':0,
    'TE':0,
    'DT':0,
    'S':0,
    'LB':0,
}

string_of_positions = "QB RB WR TE FB "

test_data=  '1 RB, 1 TE, 3 WR'

def conut_position_personnel(formation ):
    formation.replace(" ", "")
    # To separate the positions
    formation_arr = formation.split(',')

    try :
        for entry in formation_arr:
            latters = re.findall('[A-Z]', entry)
            pos = re.findall("".join(latters), string_of_positions)[0]
            number_of_players = int(re.findall('[0-9]', entry)[0])
            pos_dic [pos] = number_of_players
    except TypeError:
        print("can't find the position in the personnel ")
    

    return pos_dic

# print(re.search(, string_of_positions)[0])
# conut_position_personnel(test_data)
  










    
