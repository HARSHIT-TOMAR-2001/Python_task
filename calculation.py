def CalcTotalSeatCount(input2DArray):
    totalSeats=0
    for l in input2DArray:
        if l[0] <= 0 or l[1] <= 0:
           raise Exception("No. of rows and columns cannot be zero or negative ")
        totalSeats+=l[0]*l[1]
    return totalSeats


def CalculateSeatDistribution (input2DArray):
    sizeOf2DArray=len(input2DArray)
    TotalWindowSeats=0
    TotalAisleSeats=0
    TotalMiddleSeats=0
    for index, l in enumerate(input2DArray):
            if index==0:
                TotalWindowSeats+=l[0]
                # Check if only single block of seats is there(sizeOf2Darray==1). If 'yes' then Aisle seats are zero else count the aisle seats.
                if index!=sizeOf2DArray-1:
                    TotalAisleSeats+=l[0]

            if index==sizeOf2DArray-1:
                TotalWindowSeats+=l[0]
                # Check if only single block of seats is there(sizeOf2Darray==1). If 'yes' then Aisle seats are zero else count the aisle seats.
                if index!=0:
                    TotalAisleSeats+=l[0]

            if index!=0 and index!=sizeOf2DArray-1:
                TotalAisleSeats+=l[0]*2

            TotalMiddleSeats+=(l[0]*(l[1]-2))
        
    return (TotalAisleSeats,TotalWindowSeats,TotalMiddleSeats)


def CalculateSeatDistributionAmongPassenger (input2DArray,TotalPassengers):
    TotalSeatCount=CalcTotalSeatCount(input2DArray)
    print('Total seats:',TotalSeatCount)
    print('Total passengers:',TotalPassengers)
    if(TotalSeatCount>=TotalPassengers):
        TotalAisleSeats,TotalWindowSeats,TotalMiddleSeats=CalculateSeatDistribution(input2DArray)
        OccupiedAisleSeats=0
        OccupiedWindowSeats=0
        OccupiedMiddleSeats=0
        passengerRemaining=TotalPassengers
        if(TotalAisleSeats>=TotalPassengers):
            OccupiedAisleSeats=passengerRemaining
        else:
            OccupiedAisleSeats=TotalAisleSeats
            passengerRemaining=passengerRemaining-OccupiedAisleSeats
            if(TotalWindowSeats>=passengerRemaining):
                OccupiedWindowSeats=passengerRemaining
            else:
                OccupiedWindowSeats=TotalWindowSeats
                passengerRemaining=passengerRemaining-OccupiedWindowSeats
                OccupiedMiddleSeats=passengerRemaining

        print('Aisle seats->','Total:',TotalAisleSeats,',Occupied:',OccupiedAisleSeats,',Available:',TotalAisleSeats-OccupiedAisleSeats)
        print('Window seats->','Total:',TotalWindowSeats,',Occupied:',OccupiedWindowSeats,',Available:',TotalWindowSeats-OccupiedWindowSeats)
        print('Middle seats->','Total:',TotalMiddleSeats,',Occupied:',OccupiedMiddleSeats,',Available:',TotalMiddleSeats-OccupiedMiddleSeats) 

        if(OccupiedAisleSeats<0):
            raise Exception("Occupied Aisle Seats cannot be negative ")
        if(TotalAisleSeats-OccupiedAisleSeats<0):
            raise Exception("Available Aisle Seats cannot be zero or negative ")
        if(OccupiedWindowSeats<0):
            raise Exception("Occupied Window Seats cannot be negative ")
        if(TotalWindowSeats-OccupiedWindowSeats<0):
            raise Exception("Available Window Seats cannot be zero or negative ")
        if(OccupiedMiddleSeats<0):
            raise Exception("Occupied Middle Seats cannot be negative ")
        if(TotalMiddleSeats-OccupiedMiddleSeats<0):
            raise Exception("Available Middle Seats cannot be zero or negative ")

        return (OccupiedAisleSeats,OccupiedWindowSeats,OccupiedMiddleSeats)       
    else:
        raise Exception('Not Enough seats to accomodate all the passengers.')
