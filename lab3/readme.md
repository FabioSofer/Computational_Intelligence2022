# Lab 3
## Team: 
- Lorenzo Radaele s301165
- Fabio Sofer s301195

This is our work for the Policy search laboratory,
### Expert System
Based on the professor's implementation showed in class and on github, it is the matematically optimal way to play the game.

### Evolved-rules Strategy
After a lot of experimentation with different techniques and rules we have landed on a very simple genome as the best for our purposes <code>genome[p]</code> chooses the likelyhood of our two rules:

- Take all from the shortest row
- Take all but one from a random row

In addition to this we have a hard-coded rule of always taking the entire row if there is only 1 row left.