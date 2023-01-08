


# it takes a game id and retruns a list of all play ids
# the table scan be only pff or plays table 
def get_plays_list (gameId, table):
    return f'SELECT playid FROM nflbowl.{table} WHERE gameid = {gameId}'

def get_player_logs(nflid, gameid, role, table):
    return f'SELECT * FROM nflbowl.{table} WHERE gameid = {gameid} AND nflid = {nflid} AND pff_role = {role}'

def get_player_name(nflid):
    return f'SELECT name FROM nflbowl.players WHERE nflid = {nflid}'

def get_players_games(nflid, season):
    return f'SELECT gameId FROM nflbowl.game WHERE nflid = {nflid} AND season = {season}'

def get_player_pos_game(gameid, playid, nflid):
    return f'SELECT pff_positionLinedUp FROM nflbowl.pff_scouting WHERE gameid = {gameid} AND playid = {playid} AND nflid = {nflid}' 

def get_pff_play_info(gameid, playid, nflid):
    return f'SELECT pff_role, pff_hit, pff_hurry, pff_sack, pff_beatenByDefender, pff_hitAllowed, pff_blockType FROM pffscoutingdata WHERE gameId = {gameid} AND playId = {playid} AND nflId = {nflid}'

def get_play_info(gameid, playid ):
    return f'SELECT quarter, yardsToGo, possessionTeam, passResult, offenseFormation, personnelO FROM nflbowl.plays WHERE gameId = {gameid} AND playId = {playid}'

def test (gameid):
    return f'SELECT * FROM pffscoutingdata WHERE gameId = {gameid}'    