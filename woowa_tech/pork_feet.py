def solution(history):
    answer = []
    
    for meal in history:
        if meal not in ["1.0", "1.5", "2.0", "2.5"]:
            return [-1]
        
    refrigerator = [5, 100, 10, 5, 2]
    recipe = [4, 50, 10, 10, 4]
    item_unit = [10, 100, 30, 50, 10]
    item_price = [10000, 3000, 1000, 2000, 1000]
    
    for meal in history:
        expense = 0
        item_count = 0    
        
        for i in range(len(recipe)):
            if meal[-1] == "5" and item_count == 4:
                refrigerator[i] -= (recipe[i] // 2 * float(meal))
            else:
                refrigerator[i] -= (recipe[i] * float(meal))
                
            if refrigerator[i] < 0:
                refrigerator[i] += item_unit[i]
                expense += item_price[i]
            item_count += 1
        answer.append(expense)
            
    return answer