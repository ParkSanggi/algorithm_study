def solution(infos, actions):
    answer = []
    database = {}
    login_status = False
    cart = []
    for info in infos:
        name, pwd = info.split(" ")
        database[name] = pwd
    
    for action in actions:
        if action[0] == "L":
            _, name, pwd = action.split(" ")
            if login_status == False and name in database and database[name] == pwd:
                login_status = True
                answer.append(True)
            else:
                answer.append(False)
                
        elif action[0] == "A":
            _, item_id = action.split(" ")
            if login_status == False:
                answer.append(False)
            else:
                cart.append(item_id)
                answer.append(True)
                
        elif action[0] == "O":
            if not cart:
                answer.append(False)
            else:
                cart = []
                answer.append(True)
            
    return answer