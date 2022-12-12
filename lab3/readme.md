# Lab 3
## Team: 
- Lorenzo Radaele s301165
- Fabio Sofer s301195

This is our work for the Policy search laboratory,
### P1: Expert System
Based on the professor's implementation showed in class and on github, it is the matematically optimal way to play the game.

### P2: Evolved-rules Strategy
After a lot of experimentation with different techniques and rules we have landed on a very simple genome as the best for our purposes:

 <code>genome[p]</code> is our only evolving parameter and defines the likelyhood of our two possible outcomes:

- Take all from the shortest row
- Take all but one from a random row

These simple rules have perfomed best when evolved even when compared to more complex multi-rule systems.

In addition to this we have a hard-coded rule of always taking the entire row if there is only 1 row left, as it is a basic check that just ensures we don't miss an easy win.

### P3: MinMax Approach
We started from the professor solution of the previous year for TicTacToe, using it as a skeleton for our code and adapting it to our problem.
We used a simple but powerful strategy, leveraging the fact that we only need to find one good solution as there are not middleground states in Nim.

We are using a state cache 
```python 
boardCache=dict()
```
to optimize future tree searches but the key aspect of our program is the small 
```python 
if(val==-1):
    break
```
at the end of each move check, this makes speeds up the code drastically while providing no downside in the case of Nim.

Our code wins 100% of the time against the expert opponent up to Nim size 8 (it will ideally win with any size), choosing whether to start or not depending if the board starts off with nimSum=0 or not.

### P4: RL Approach
Starting from the code provided by assistant professor, we have used out Nim class as the "maze" in the sense that it is the state our agent is currently in and it handles the rewards, while the agent just chooses an action that will be performed on his next step and learns from his previous paths.
Key things that we do differently are the creation of the possible boardstates G at the beginning of the game (using the hash and eq functions we already implemented to use the cache in the minmax approach): 
```python 
for i in range(num_rows):
    tmp.append(range(0, i * 2 + 2))
for i in list(product(*tmp)):
    n = Nim(num_rows)
    self.G[n.assign_rows(i)] = random.random()
```

and a push for the program not to get stuck in a bad situation we restart the Agent, removing all previous values in the states and starting the exploration with new G-values.
```python 
if win_ratio < 0.1 :
    jack = Agent(NUM_ROWS, alpha=0.3, random_factor=0.1)
```