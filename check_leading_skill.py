# 프로그래머스 2018 윈터코딩 선행스킬트리


def solution(skill, skill_trees):
    skill_dic = {}

    right_tree_count = 0

    for i in range(len(skill)):
        skill_dic[skill[i]] = {"is_preceded": False, "index": i}

    for skill_tree in skill_trees:

        for a_skill in skill_tree:
            if a_skill in skill_dic:
                leading_skill_idx = skill_dic[a_skill]["index"] - 1
                if leading_skill_idx == -1:
                    skill_dic[skill[0]]["is_preceded"] = True
                else:
                    if not skill_dic[skill[leading_skill_idx]]["is_preceded"]:
                        break
                    else:
                        skill_dic[skill[leading_skill_idx + 1]]["is_preceded"] = True

        for j in skill_dic.keys():
            skill_dic[j]["is_preceded"] = False

        if a_skill == skill_tree[-1]:
            right_tree_count += 1

    return right_tree_count
