# * make a api to recving class to get best players in one week or best agem of a player 
# * make the score on how a player does in one play or a season (avg score of all games )

# switch to a node.js to make the proces fatser 
from mysql.index import get_pff_play_info, get_play_info
from mysql.DB_client import create_connect, create_cursor, execute_query
# filter on cal score max play score

cursor = create_cursor( create_connect() )

def player_best_game(nflid, season):
    return

# filter on cal score min play score
def player_worest_game(nflid, season):
    return

# thse are all needed arrgs to cal_score
# gameid, nflid,
# pff table: pff_role, pff_hurryAllowed, pff_sackAllowed, pff_hitAllowed, pff_beatenByDefender, pff_blockType
# plays table: quarter, yardsToGo, possessionTeam, passResult, offenseFormation, personnelO
# make a 1 for a boolean and scale for numerical veribles like how many penalty yards   total number of score / len(number of veribles) 
def cal_score(gameid, playid, nflid):
    pff_info_query = get_pff_play_info(gameid, playid, nflid)
    play_info_query = get_play_info(gameid, playid, nflid)

    pff_info = execute_query(cursor, pff_info_query)
    play_info = execute_query(cursor, play_info_query)



