# machine_learning_assignment_six

### Assignment 6, Due on November 7

You are given the following rating data in which 12 movies are rated by 10 users.  Blank entry indicates that the user has not seen the movie.  The last 4 rows describe the content of each movie.


|          | M1   | M2  | M3  |  M4 |  M5 |  M6 |  M7 |  M8 |  M9 | M10 | M11 | M12 |
| -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| U1       | 1    | 5   | 2   |     | 4   | 4   | 2   | 2   |     | 3   | 2   |     |
| U2       | 5    | 3   |     | 2   | 4   | 2   | 1   |     |     | 4   | 3   | 2   |
| U3       |      |     |     | 5   | 2   |     | 4   |     |     | 1   |     | 1   |
| U4       |      | 3   |     |     |     | 1   | 2   | 3   | 4   |     |     | 4   |
| U5       | 4    | 3   | 4   | 1   | 4   | 1   |     | 4   |     | 1   | 5   | 1   |
| U6       | 2    | 4   | 4   | 4   |     |     | 3   | 1   | 4   |	4   | 5   |	1   |
| U7       |      |     | 3   | 1   | 1   |	4   |     | 5   | 2   | 1   |     |     |
| U8       | 4    |     |     |     | 3   |	2   | 2   |     | 3   |     |     | 2   |
| U9       | 5    | 1   |     | 4   | 2   | 4   | 4   | 4   |     | 1   | 2   | 3   |
| U10      | 4    | 2   |     | 5   | 3	  |     | 4   | 3   | 4   |     |     |     |
| Action   | 0.8  | 0.3 | 0.2 |	0.2 | 0.6 | 0.1 | 0.1 | 0.2 | 0.7 | 0.6 | 0.2 |	0.2 |
| Comedy   | 0.1  | 0.4 | 0.4 |	0.2 | 0.1 | 0.2 | 0.3 | 0.3 | 0.1 | 0   | 0.3 |	0.2 |
| Romance  | 0.05 | 0.1 | 0.4 |	0.3 | 0.2 | 0.3 | 0.5 | 0.3 | 0	  | 0.3 | 0.3 | 0.2 |
| Violence | 0.05 | 0.2 | 0   |	0.3 | 0.1 | 0.4 | 0.1 | 0.2 | 0.1 | 0.1 | 0.2 | 0.4 |

1.	Recommend one movie to U2 using non-personalized approach.
1.	Determine user profile vector for U2.
1.	Estimate ratings user U2 may give to movies M3, M8 and M9 using content based approach.
1.	Estimate ratings user U2 may give to movies M3, M8 and M9 using linear regression.
1.	Estimate ratings user U2 may give to movies M9 using user-user collaboration approach.
1.	Estimate ratings user U2 may give to movies M9 using item-item collaboration approach.
1.	Currently U8 has just finished rating M1.  What movie would you recommend using Item-association approach?


In all cases, show your work.  State your assumptions. Program when necessary.  
