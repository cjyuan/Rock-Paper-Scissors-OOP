

  player1 = ...
  player2 = ...
  competition1 = ...
  competition2 = ...

  composite_competion = CompositeCompetition([competition1, competition2])

  run_competition(player1, player2, CompositeCompetition)

class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Need to make this class modifiable only in Competition
class History:
  n: int
  scores: list[int] # scores[i] is the score of player i
  moves: list[list[Move]] # moves[i][j] is the j-th move of player i

  def getScore(playerIndex: int, turn: int) -> int:
      pass  
  def getMoves(playerIndex: int, turn: int) -> Move:
      pass


class Player:
    name: str
    description: str

    def beforeStart(history: History)
    def afterEnd()
    
    def move(playerIndex: int, turn: int) -> Move:
       pass

class Competition:
    turns: int
    points: list[int]
    players: list[Player]
    # moves by all players 
    history: History
    
    def start():
        # Notify every player a competition is starting
        for (player in self.players):
            player.beforeStart(self.history)
        pass  

    def end():
        # Notify every player a competition has ended
        for (player in self.players):
            player.afterEnd()
        pass  
    
    def score():
        # collect moves from each player and calculate the score accordingly
        # scoring mechanism depending on competition type
        pass

    def compare(move1:Move, move2: Move) -> int:
        # return 1 if first move wins, -1 if second move wins, 0 if tie
        if (move1 == Move.ROCK and move2 == Move.SCISSORS) or \
           (move1 == Move.PAPER and move2 == Move.ROCK) or \
           (move1 == Move.SCISSORS and move2 == Move.PAPER):
            return 1  
        if (move1 == move2):
            return 0
            
        return -1


# Normal game, 10 turns
class MyCompetition(Competition):
    def score():
        # custom scoring mechanism
        for (turn in range(self.turns)):
          for (player in self.players):
            move = player.move(playerIndex, turn)
            self.history.moves[playerIndex][turn] = move

          # calculate scores based on moves
            ...
            # if player1 wins: self.history.scores[player1Index] += 1
            

class PlayerRandom(Player):
    history: History
    def beforeStart(history: History):
        pass

    def move(playerIndex: int, turn: int) -> Move:
        ... # access history if needed
        return random.choice([Move.ROCK, Move.PAPER, Move.SCISSORS])




class CompositeCompetition(Competition):
    competitions: list[Competition]

    def start():
        for (competition in self.competitions):
            competition.start()

    def end():
        for (competition in self.competitions):
            competition.end()

    def score():
        for (competition in self.competitions):
            competition.score()


---------------------------

class CompetitionInterface:

    def start():
        pass  

    def end():
        pass  
    
    def score():
        pass

    def compare(move1:Move, move2: Move) -> int:
        # return 1 if first move wins, -1 if second move wins, 0 if tie
        if (move1 == Move.ROCK and move2 == Move.SCISSORS) or \
           (move1 == Move.PAPER and move2 == Move.ROCK) or \
           (move1 == Move.SCISSORS and move2 == Move.PAPER):
            return 1  
        if (move1 == move2):
            return 0
            
        return -1

class BasicCompetition(CompetitionInterface):
   turns: int
    points: list[int]
    players: list[Player]
    # moves by all players 
    history: History
    
    def start():
        # Notify every player a competition is starting
        for (player in self.players):
            player.beforeStart(self.history)
        pass  

    def end():
        # Notify every player a competition has ended
        for (player in self.players):
            player.afterEnd()
        pass  
    
    def score():
        # collect moves from each player and calculate the score accordingly
        # scoring mechanism depending on competition type
        pass

    def compare(move1:Move, move2: Move) -> int:
        # return 1 if first move wins, -1 if second move wins, 0 if tie
        if (move1 == Move.ROCK and move2 == Move.SCISSORS) or \
           (move1 == Move.PAPER and move2 == Move.ROCK) or \
           (move1 == Move.SCISSORS and move2 == Move.PAPER):
            return 1  
        if (move1 == move2):
            return 0
            
        return -1


class CompositeCompetition(CompetitionInterface):

    competitions: list[Competition]

    def start():
        for (competition in self.competitions):
            competition.start()

    def end():
        for (competition in self.competitions):
            competition.end()

    def score():
        for (competition in self.competitions):
            competition.score()





class BaseClass:
  properties
  methods

class SubClass(BaseClass):
  additional_properties
  additional_methods

----

class Interface:
  methods

class BaseClass(Interface):
  properties
  methods # with implementation

class SubClass(BaseClass):
  additional_properties
  additional_methods

class AnotherClass(Interface, OtherBaseClass):
  properties
  methods
