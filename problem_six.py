import math

'''
6. Estimate ratings user U2 may give to movies M9 using item-item collaboration approach.

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

S(u, i) = ravg(i) +  Σj ε N [(r(u, j) – ravg(j)) * w(i, j)] / Σj ε N |w(i, j)|

w(i, j) = Σu ε U [(r(u, i) -  ravg(i))*(r(u, j) – ravg(j))] / [σ(i)σ(j)]
'''

M1avg  = ( 1.0 + 5 + 4 + 2 + 4 + 5 + 4 ) / 7.0;
M2avg  = ( 5.0 + 3 + 3 + 3 + 4 + 1 + 2 ) / 7.0;
M4avg  = ( 2.0 + 5 + 1 + 4 + 1 + 4 + 5 ) / 7.0;
M5avg  = ( 4.0 + 4 + 2 + 4 + 1 + 3 + 2 + 3 ) / 8.0;
M6avg  = ( 4.0 + 2 + 1 + 1 + 4 + 2 + 4 ) / 7.0;
M7avg  = ( 2.0 + 1 + 4 + 2 + 3 + 2 + 4 + 4 ) / 8.0;
M9avg  = ( 4.0 + 4 + 2 + 3 + 4 ) / 5.0;
M10avg = ( 3.0 + 4 + 1 + 1 + 4 + 1 + 1 ) / 7.0;
M11avg = ( 2.0 + 3 + 5 + 5 + 2 ) / 5.0 ;
M12avg = ( 2.0 + 1 + 4 + 1 + 1 + 2 + 3 ) / 7.0;

M1SD  = math.sqrt( ( 1.0 / 7.0 ) * ( ( 1 - M1avg ) ** 2 + ( 5 - M1avg ) ** 2 + ( 4 - M1avg ) ** 2 + ( 2 - M1avg ) ** 2 + ( 4 - M1avg ) ** 2 + ( 5 - M1avg ) ** 2 + ( 4 - M1avg ) ** 2 ) );
M2SD  = math.sqrt( ( 1.0 / 7.0 ) * ( ( 5 - M2avg ) ** 2 + ( 3 - M2avg ) ** 2 + ( 3 - M2avg ) ** 2 + ( 3 - M2avg ) ** 2 + ( 4 - M2avg ) ** 2 + ( 1 - M2avg ) ** 2 + ( 2 - M2avg ) ** 2 ) );
M4SD  = math.sqrt( ( 1.0 / 7.0 ) * ( ( 2 - M4avg ) ** 2 + ( 5 - M4avg ) ** 2 + ( 1 - M4avg ) ** 2 + ( 4 - M4avg ) ** 2 + ( 1 - M4avg ) ** 2 + ( 4 - M4avg ) ** 2 + ( 5 - M4avg ) ** 2 ) );
M5SD  = math.sqrt( ( 1.0 / 8.0 ) * ( ( 4 - M5avg ) ** 2 + ( 4 - M5avg ) ** 2 + ( 2 - M5avg ) ** 2 + ( 4 - M5avg ) ** 2 + ( 1 - M5avg ) ** 2 + ( 3 - M5avg ) ** 2 + ( 2 - M5avg ) ** 2 + ( 3 - M5avg ) ** 2 ) );
M6SD  = math.sqrt( ( 1.0 / 7.0 ) * ( ( 4 - M6avg ) ** 2 + ( 2 - M6avg ) ** 2 + ( 1 - M6avg ) ** 2 + ( 1 - M6avg ) ** 2 + ( 4 - M6avg ) ** 2 + ( 2 - M6avg ) ** 2 + ( 4 - M6avg ) ** 2 ) );
M7SD  = math.sqrt( ( 1.0 / 8.0 ) * ( ( 2 - M7avg ) ** 2 + ( 1 - M7avg ) ** 2 + ( 4 - M7avg ) ** 2 + ( 2 - M7avg ) ** 2 + ( 3 - M7avg ) ** 2 + ( 2 - M7avg ) ** 2 + ( 4 - M7avg ) ** 2  + ( 4 - M7avg ) ** 2 ) );
M9SD  = math.sqrt( ( 1.0 / 5.0 ) * ( ( 4 - M9avg ) ** 2 + ( 4 - M9avg ) ** 2 + ( 2 - M9avg ) ** 2 + ( 3 - M9avg ) ** 2 + ( 4 - M9avg ) ** 2 ) );
M10SD = math.sqrt( ( 1.0 / 7.0 ) * ( ( 3 - M10avg ) ** 2 + ( 4 - M10avg ) ** 2 + ( 1 - M10avg ) ** 2 + ( 1 - M10avg ) ** 2 + ( 4 - M10avg ) ** 2 + ( 1 - M10avg ) ** 2 + ( 1 - M10avg ) ** 2 ) ); 
M11SD = math.sqrt( ( 1.0 / 5.0 ) * ( ( 2 - M11avg ) ** 2 + ( 3 - M11avg ) ** 2 + ( 5 - M11avg ) ** 2 + ( 5 - M11avg ) ** 2 + ( 2 - M11avg ) ** 2 ) );
M12SD = math.sqrt( ( 1.0 / 7.0 ) * ( ( 2 - M12avg ) ** 2 + ( 1 - M12avg ) ** 2 + ( 4 - M12avg ) ** 2 + ( 1 - M12avg ) ** 2 + ( 1 - M12avg ) ** 2 + ( 2 - M12avg ) ** 2 + ( 3 - M12avg ) ** 2 ) );

WM9M1  = ( ( ( 2 - M1avg ) * ( 4 - M9avg ) ) + ( ( 4 - M1avg ) * ( 3 - M9avg ) ) + ( ( 4 - M1avg ) * ( 4 - M9avg ) ) ) / ( M9SD * M1SD );
WM9M2  = ( ( ( 3 - M2avg ) * ( 4 - M9avg ) ) + ( ( 4 - M2avg ) * ( 4 - M9avg ) ) + ( ( 2 - M2avg ) * ( 4 - M9avg ) ) ) / ( M9SD * M2SD );
WM9M4  = ( ( ( 4 - M4avg ) * ( 4 - M9avg ) ) + ( ( 1 - M4avg ) * ( 2 - M9avg ) ) + ( ( 5 - M4avg ) * ( 4 - M9avg ) ) ) / ( M9SD * M4SD );
WM9M5  = ( ( ( 1 - M5avg ) * ( 2 - M9avg ) ) + ( ( 3 - M5avg ) * ( 3 - M9avg ) ) + ( ( 3 - M5avg ) * ( 4 - M9avg ) ) ) / ( M9SD * M5SD );
WM9M6  = ( ( ( 1 - M6avg ) * ( 4 - M9avg ) ) + ( ( 4 - M6avg ) * ( 2 - M9avg ) ) + ( ( 2 - M6avg ) * ( 3 - M9avg ) ) ) / ( M9SD * M6SD );
WM9M7  = ( ( ( 2 - M7avg ) * ( 4 - M9avg ) ) + ( ( 3 - M7avg ) * ( 4 - M9avg ) ) + ( ( 2 - M7avg ) * ( 3 - M9avg ) ) + ( ( 4 - M7avg ) * ( 4 - M9avg ) ) ) / ( M9SD * M7avg );
WM9M10 = ( ( ( 4 - M10avg ) * ( 4 - M9avg ) ) + ( ( 1 - M10avg ) * ( 2 - M9avg ) ) ) / ( M9SD * M10SD );
WM9M11 = ( ( 5 - M11avg ) * ( 4 - M9avg ) ) / ( M9SD * M11SD );
WM9M12 = ( ( ( 4 - M12avg ) * ( 4 - M9avg ) ) + ( ( 1 - M12avg ) * ( 4 - M9avg ) ) + ( ( 2 - M12avg ) * ( 3 - M9avg ) ) ) / ( M9SD * M12SD );

SumAbsWij = abs( WM9M1 ) + abs( WM9M2) + abs( WM9M4 ) + abs( WM9M5 ) + abs( WM9M6 ) + abs( WM9M7 ) + abs( WM9M10 ) + abs( WM9M11 ) + abs( WM9M12 );
SumAdjRating = ( ( 5 - M1avg ) * WM9M1 ) + ( ( 3 - M2avg ) * WM9M2 ) + ( ( 2 - M4avg ) * WM9M4 ) + ( ( 4 - M5avg ) * WM9M5 ) + ( ( 2 - M6avg ) * WM9M6 ) + ( ( 1 - M7avg ) * WM9M7 ) + ( ( 4 - M10avg ) * WM9M10 ) + ( ( 3 - M11avg ) * WM9M11 ) + ( ( 2 - M12avg ) * WM9M12 );
rating = M9avg + ( SumAdjRating / SumAbsWij );
print(rating);
