# Lab 1
## Team: 
- Lorenzo Radaele s301165
- Fabio Sofer s301195

## Description
We started from the script of the 8-puzzle removing the unnecessary parts and adapting the data types and the methods in order to fit the problem.

In the priority function we have considered both the cost of the current solution and its coverage; using a multiplier factor to adjust the weight of the latter we can obtain faster but less accurate solutions or slower but more precise ones.

## Results

| N                | Ls       | Visited nodes | k |
|-----------------------|----------|---------------|-------|
| 5               | 5 |     3          | 1 |
| 10 |  10 |       3        | 1 |
| 20 | 23 |      11,901         | 1 |
| 100   | 171 |    562           | 4 |
| 500    | 1240 |   347            | 15 |
| 1000    | 2788 |     1090          | 25 |