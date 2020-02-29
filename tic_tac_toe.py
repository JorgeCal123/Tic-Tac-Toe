import re
import random


_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None


#-----------------------------------------------------------------------------------

  def is_over(self):
    estado=False
    # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    if self.board.count(None) == 0:
      estado=True
    if self.diagonals()==True:
      estado=True
    elif self.columns()==True:
      estado=True
    elif self.rows()==True:
      estado=True
    return estado


  def diagonals(self):
    raya=False
    if self.turn==_PLAYER:
      if self.check_Play(_MACHINE,0,4,8) or self.check_Play(_MACHINE,2,4,6):
        raya=True
        self.winner=_MACHINE

    elif self.turn==_MACHINE:
      if self.check_Play(_PLAYER,0,4,8) or self.check_Play(_PLAYER,2,4,6):
        raya=True
        self.winner=_PLAYER
    return raya

        
  def columns(self):
    raya=False
    if self.turn==_PLAYER:
      if self.check_Play(_MACHINE,0,1,2) or self.check_Play(_MACHINE,3,4,5) or self.check_Play(_MACHINE,6,7,8):
        raya=True
        self.winner=_MACHINE

    elif self.turn==_MACHINE:
      if self.check_Play(_PLAYER,0,1,2) or self.check_Play(_PLAYER,3,4,5) or self.check_Play(_PLAYER,6,7,8):
        raya=True
        self.winner=_PLAYER

    return raya



  def rows(self):
    raya=False
    if self.turn==_PLAYER:
      if self.check_Play(_MACHINE,0,3,6) or self.check_Play(_MACHINE,1,4,7) or self.check_Play(_MACHINE,2,5,8):
        raya=True
        self.winner=_MACHINE
        
    elif self.turn==_MACHINE:
      if self.check_Play(_PLAYER,0,3,6) or self.check_Play(_PLAYER,1,4,7) or self.check_Play(_PLAYER,2,5,8):
        raya=True
        self.winner=_PLAYER
    return raya
  


  def check_Play(self,jugador,x,y,z):
    raya=False
    if jugador==_PLAYER:
      if self.board[x]==_PLAYER_SYMBOL and self.board[y]==_PLAYER_SYMBOL and self.board[z]==_PLAYER_SYMBOL:
        raya=True
    elif jugador==_MACHINE:
      if self.board[x]==_MACHINE_SYMBOL and self.board[y]==_MACHINE_SYMBOL and self.board[z]==_MACHINE_SYMBOL:
        raya=True
    return raya


  
  

  def play(self):
    
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER
 

#-----------------------------------------------------------------------------------

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

#-----------------------------------------------------------------------------------


  def player_turn(self):

    
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

#-----------------------------------------------------------------------------------


  def machine_turn(self): # TODO: Finish this function by making the machine choose a random cell (use random module)
   
    i=int(random.randint(0, 8))
   # print(self.board[i])
   # print(not self.board[i])
    if (not self.board[i]):
      self.board[i] = _MACHINE_SYMBOL
    else:
      self.machine_turn()
    
#-----------------------------------------------------------------------------------

  def format_board(self):
    row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
    row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
    row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

    return "\n".join([row0, row1, row2])




  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self): # TODO: Finish this function in order to print the result based on the *winner*
    print("El Ganador es "+ self.winner)
