import major_calculation

sizeOf2DArray=int(input("Enter the size of 2D array: "))
input2DArray=[[0]*2]*sizeOf2DArray


for x in range(sizeOf2DArray):
    rowLength=int(input('Enter the size of row: '))
    colLength=int(input('Enter the size of column: '))

    input2DArray[x]=[rowLength,colLength]

TotalPassengerCount=int(input("Enter Total no. of passengers: "))

major_calculation.CalculateSeatDistributionAmongPassenger(input2DArray,TotalPassengerCount)