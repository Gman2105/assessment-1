import math

def optimal_change (item_cost, amount_paid):
    
    denominations = [100, 50, 20, 10, 5, 1, .25, .10, .05, .01]
    
    change = float(amount_paid - item_cost)
    
    statement = f'The optimal change for this item is ${item_cost} with an amount paid of ${amount_paid} is '
    
    # Check if you less than the amount of the item cost.   
    if amount_paid < item_cost:
        return ("Not Enough Money")
    
    # Check if there is change or not.    
    if amount_paid == item_cost:
        return ("No Change")
    
    if change > 0:
        for i in range(len(denominations)):
            check_amount = math.floor(change // denominations[i])
            
            #check the first half of the list.
            #check for use of plural.
            if check_amount > 1:
                if i >= 6 and check_amount > 0:
                    statement += f' , {check_amount} ${denominations[i]} cents'
                    change -= (check_amount * denominations[i])
                    continue
                elif check_amount > 0:
                    statement += f', {check_amount} ${denominations[i]} bills'
                    change -= (check_amount * denominations[i])
            
            # Check for use of single.
            elif check_amount > 0:
                if i >= 6 and check_amount > 0:
                    statement += f', {check_amount} ${denominations[i]} cent'
                    change -= (check_amount * denominations[i])
                    continue
                elif check_amount > 0:
                    statement += f', {check_amount} ${denominations[i]} bill'
                    change -= (check_amount * denominations[i])
        
        return statement + '.'
    
print(optimal_change (46.57, 100))