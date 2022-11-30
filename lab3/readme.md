# Lab 2
## Team: 
- Lorenzo Radaele s301165
- Fabio Sofer s301195

## Lab3 Algorithms choice

### Expert System
Based on the professor's implementation showed in class and on github.

### Fitness definition
Similarly to the first lab we have considered both the lenght of the current solution and its coverage to compute its fitness, in practice we have a multiplicative costant <code>K</code> which is used to make the weighting of the coverage bigger than the negative score of the lenght, otherwise we would stop as soon as the addition of one already present element is required. Furthermore, we have added a penalty to the fitness score of invalid solutions, as this helps us find the best valid solutions without discarding possible paths that pass through non-valid solutions.

### Genetic function changes
The changes we have made in indivual generation are:
- A higher probability(80%) of mutating 5 times(as opposed to only once)
- A cross-over generation with lower probability(20%) and that still causes small mutations inside the genome of the offspring (single gene after the crosss over is done).
- Tournament, after experimentation with tournament sizes, is left unchanged from the one-max example.