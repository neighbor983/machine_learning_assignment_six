import math

M1 =  [ 0.8 , 0.1, 0.05, 0.05 ]; 
M2 =  [ 0.3, 0.4, 0.1, 0.2 ];
M3 =  [ 0.2, 0.4, 0.4, 0.0 ];
M4 =  [ 0.2, 0.2, 0.3, 0.3 ];
M8 =  [ 0.2, 0.3, 0.3, 0.2 ];
M10 = [ 0.6, 0.0, 0.3, 0.1 ];
M11 = [ 0.2, 0.3, 0.3, 0.2 ];

def euclideanDistance(arr1, arr2):
    summation = 0.0;
    for i in range(len(arr1)):
        summation += ( ( arr1[i] - arr2[i] ) ** 2 );
    return math.sqrt(summation);
    
M2Distance = euclideanDistance(M1, M2);
M3Distance = euclideanDistance(M1, M3);
M4Distance = euclideanDistance(M1, M4);
M8Distance = euclideanDistance(M1, M8);
M10Distance = euclideanDistance(M1, M10);
M11Distance = euclideanDistance(M1, M11);

print('M2: ' + str(M2Distance));
print('M3: ' + str(M3Distance));
print('M4: ' + str(M4Distance));
print('M8: ' + str(M8Distance));
print('M10: ' + str(M10Distance));
print('M11: ' + str(M11Distance));