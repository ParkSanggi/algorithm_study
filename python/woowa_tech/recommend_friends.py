import operator

def solution(user, friends, visitors):
    answer = []
    members = {}
    member_relations = {}
    for friend in friends:
        if friend[0] not in member_relations:
            member_relations[friend[0]] = {friend[1]:1}
        else:
            member_relations[friend[0]][friend[1]] = 1
        
        if friend[1] not in member_relations:
            member_relations[friend[1]] = {friend[0]:1}
        else:
            member_relations[friend[1]][friend[0]] = 1
    
    friends_of_user = [friend_of_user for friend_of_user in member_relations[user].keys()]
    
    for friend_of_user in friends_of_user:
        for friend_of_friend in member_relations[friend_of_user].keys():
            if friend_of_friend not in members:
                members[friend_of_friend] = 10
            else:
                members[friend_of_friend] += 10
                
    for visitor in visitors:
        if visitor not in members:
            members[visitor] = 1
        else:
            members[visitor] += 1
    
    members_items = sorted(members.items(), key=operator.itemgetter(1))
    
    recommend_count = 0
    temp = []
    while members_items and recommend_count < 5:
        _max = members_items.pop()
        if _max[0] not in friends_of_user and _max[0] != user:
            if temp:
                if temp[-1][1] == _max[1]:
                    temp.append(_max)
                    recommend_count += 1
                else:
                    temp.sort()
                    for i in temp:
                        answer.append(i[0])
                    temp = [_max]
            else:
                temp.append(_max)
                recommend_count += 1
    if temp:
        temp.sort()
        for i in temp:
            answer.append(i[0])
    return answer
