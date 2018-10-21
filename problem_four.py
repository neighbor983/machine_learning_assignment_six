import math

'''
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
'''

ratings = [ 5, 3, 2, 4, 2, 1, 4, 3, 2 ];
#ratings = [ 5, 4, 4 ];

M1 =  [ .8, .1, .05, .05 ];
M2 =  [ .2, .4, .4, 0 ];
M4 =  [ .2, .2, .3, .3 ];
M5 =  [ .6, .1, .2, .1 ];
M6 =  [ .1, .2, .3, .4 ];
M7 =  [ .1, .3, .5, .1 ];
M10 = [ .6, 0, .3, .1 ];
M11 = [ .2, .3, .3, .2 ];
M12 = [ .2, .2, .2, .4 ];

dataList = [
    { 'rating': ratings[0], 'attributes': M1 },
    { 'rating': ratings[1], 'attributes': M2 },
    { 'rating': ratings[2], 'attributes': M4 },
    { 'rating': ratings[3], 'attributes': M5 },
    { 'rating': ratings[4], 'attributes': M6 },
    { 'rating': ratings[5], 'attributes': M7 },
    { 'rating': ratings[6], 'attributes': M10 },
    { 'rating': ratings[7], 'attributes': M11 },
    { 'rating': ratings[8], 'attributes': M12 }
];

def linearModel(attr, thetaZero, thetaOne, thetaTwo, thetaThree, thetaFour):
    return thetaZero + attr[0] * thetaOne + attr[1] * thetaTwo + attr[2] * thetaThree + attr[3] * thetaFour; 

def Cost(thetaZero, thetaOne, thetaTwo, thetaThree, thetaFour, m, dataList):
    summation = 0.0;
    for row in dataList:
        x = row['attributes'];
        y = row['rating'];
        summation += ( (linearModel(x, thetaZero, thetaOne, thetaTwo, thetaThree, thetaFour) - y) ** 2.0 );
    return ( ( .5 * m ) * summation);


def theta0_gradient(thetaZero, thetaOne, thetaTwo, thetaThree, thetaFour, alpha, m, data):
    summation = 0.0;
    for row in data:
        x = row['attributes'];
        y = row['rating'];
        summation += (linearModel(x, thetaZero, thetaOne, thetaTwo, thetaThree, thetaFour) - y);
    return thetaZero - ( alpha / m ) * summation; 

def theta1_gradient(thetaZero, thetaOne, thetaTwo, thetaThree, thetaFour, alpha, m, data):
    summation = 0.0;
    for row in data:
        x = row['attributes'];
        y = row['rating'];
        summation += ( ( linearModel(x, thetaZero, thetaOne, thetaTwo, thetaThree, thetaFour) - y) * x[0]);
    return thetaOne - ( alpha / m ) * summation; 

def theta2_gradient(thetaZero, thetaOne, thetaTwo, thetaThree, thetaFour, alpha, m, data):
    summation = 0.0;
    for row in data:
        x = row['attributes'];
        y = row['rating'];
        summation += ( ( linearModel(x, thetaZero, thetaOne, thetaTwo, thetaThree, thetaFour) - y) * x[1]);
    return thetaTwo - ( alpha / m ) * summation; 

def theta3_gradient(thetaZero, thetaOne, thetaTwo, thetaThree, thetaFour, alpha, m, data):
    summation = 0.0;
    for row in data:
        x = row['attributes'];
        y = row['rating'];
        summation += ( ( linearModel(x, thetaZero, thetaOne, thetaTwo, thetaThree, thetaFour) - y) * x[2]);
    return thetaThree - ( alpha / m ) * summation; 

def theta4_gradient(thetaZero, thetaOne, thetaTwo, thetaThree, thetaFour, alpha, m, data):
    summation = 0.0;
    for row in data:
        x = row['attributes'];
        y = row['rating'];
        summation += ( ( linearModel(x, thetaZero, thetaOne, thetaTwo, thetaThree, thetaFour) - y) * x[3]);
    return thetaFour - ( alpha / m ) * summation; 

alpha = .001;
theta0 = 1.0;
theta1 = 1.0;
theta2 = 1.0;
theta3 = 0.0;
theta4 = 0.0;
m = len(dataList);

oldCost = 1000;
newCost = oldCost * .5;
count = 0; 
runs = [];

while(  oldCost  > ( newCost * 1.0000000001) ):
    oldCost = newCost;
    new_theta0 = theta0_gradient(theta0, theta1, theta2, theta3, theta4, alpha, m, dataList);
    new_theta1 = theta1_gradient(theta0, theta1, theta2, theta3, theta4, alpha, m, dataList);
    new_theta2 = theta2_gradient(theta0, theta1, theta2, theta3, theta4, alpha, m, dataList);
    new_theta3 = theta3_gradient(theta0, theta1, theta2, theta3, theta4, alpha, m, dataList);
    new_theta4 = theta4_gradient(theta0, theta1, theta2, theta3, theta4, alpha, m, dataList);

    theta0 = new_theta0; 
    theta1 = new_theta1; 
    theta2 = new_theta2;
    theta3 = new_theta3;
    theta4 = new_theta4; 
    
    newCost = Cost(theta0, theta1, theta2, theta3, theta4, m, dataList);
    count += 1;
    runs.append({'run' : count, "J": newCost});

print('theta0: ' + str(round(theta0, 2)));
print('theta1: ' + str(round(theta1, 2)));
print('theta2: ' + str(round(theta2, 2)));
print('theta3: ' + str(round(theta3, 2)));
print('theta4: ' + str(round(theta4, 2)));
print(len(runs));



print(1.93 + 4.14 * .2 + 2.14 * .4 + (-2.35) * .4 + (-1.0) * 0);
print( 1.93 + 4.14 * .2 + 2.14 * .3 + (-2.35) * .3 + (-1.0) * .2);
print(1.93 + 4.14 * .7 + 2.14 * .1 + (-2.35) * 0 + (-1.0) * .1);