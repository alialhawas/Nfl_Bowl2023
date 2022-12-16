


# it takes a game id and retruns a list of all play ids
# the table scan be only pff or plays table 
def get_plays_list (gameId, table):
    return f'SELECT playid FROM nflbowl.{table} WHERE gameid = {gameId}'

def get_player_logs(nflid, gameid, role, table):
    return f'SELECT * FROM nflbowl.{table} WHERE gameid = {gameid} AND nflid = {nflid} AND pff_role = {role}'

def get_player_name(nflid):
    return f'SELECT name FROM nflbowl.players WHERE nflid = {nflid}'

def get_players_games(nflid):
    return f'SELECT displayName FROM nflbowl.players WHERE nflid = {nflid}'

def get_player_pos_game(gameid, playid, nflid):
    return f'SELECT pff_positionLinedUp FROM nflbowl.pff_scouting WHERE gameid = {gameid} AND playid = {playid} AND nflid = {nflid}' 

