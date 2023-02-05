import random

def generate_pc(pc_points):
    attributes = ["st", "dx", "ag", "co", "in", "wi", "pe", "ch"]
    pc = {}
    
    print("First Priority:")
    print("1-st", "2-dx", "3-ag", "4-co", "5-in", "6-wi", "7-pe", "8-ch")
    first_priority = int(input("Enter first priority: ")) - 1
    pc[attributes[first_priority]] = random.randint(15, 18)
    pc_points -= pc[attributes[first_priority]]
    print("REMAIN: ",pc_points)
    
    print("Second Priority:")
    print("1-st", "2-dx", "3-ag", "4-co", "5-in", "6-wi", "7-pe", "8-ch")
    second_priority = int(input("Enter second priority: ")) - 1
    pc[attributes[second_priority]] = random.randint(12,15)
    pc_points -= pc[attributes[second_priority]]
    print("REMAIN: ",pc_points)

    sum_of_points = pc[attributes[first_priority]] + pc[attributes[second_priority]]
    
    for attribute in attributes:
        if attribute != attributes[first_priority] and attribute != attributes[second_priority]:
            pc[attribute] = random.randint(8, 11)
            pc_points -= pc[attribute]
            sum_of_points += pc[attribute]
            if pc_points < 8:
                pc[attribute] += pc_points
                sum_of_points += pc_points
                break
    
    pc["name"] = input("Enter PC name: ")
    
    #Redistribute remaining points
    remaining_points =  pc_points 
    print("SUM_OF_POINTS: ", sum_of_points)
    print("PC_POINTS: ", pc_points)
    print("REMAINING_POINTS", remaining_points)
    print(f"PC Name:{pc['name']}")
    attributes = ["st", "dx", "ag", "co", "in", "wi", "pe", "ch"]
    for attribute in attributes:
        print(f"{attribute}: {pc[attribute]} TEST {pc[attribute] * 4}%")
    if remaining_points > 0:
        while remaining_points!=0:
            for attribute in attributes:
                if pc[attribute] >= 8 and pc[attribute] <18:
                    pc[attribute] += 1
                    remaining_points -= 1
                    sum_of_points += 1
#        print(remaining_points)
#        for attribute in attributes:
#            if pc[attribute] >= 8 and pc[attribute] < 18:
#                pc[attribute] += 1
#                remaining_points -= 1
#                sum_of_points += 1
#                print("SUM_OF_POINTS: ", sum_of_points)
#                print("PC_POINTS: ", pc_points)
#                print("REMAINING_POINTS-", remaining_points)
#                if remaining_points == 0:
#                    break
#                elif pc[attribute] >= 8 and pc[attribute] < 18:
#                    pc[attribute] += 1
#                    remaining_points -= 1
#                    sum_of_points += 1
#                    print("SUM_OF_POINTS: ", sum_of_points)
#                    print("PC_POINTS: ", pc_points)
#                    print("REMAINING_POINTS--", remaining_points)
#                    if remaining_points == 0:
#                        break
    
    return pc, sum_of_points
    if remaining_points < 0:
        while remaining_points!=0:
            for attribute in attributes:
                if pc[attribute] >= 8 and pc[attribute] <18:
                    pc[attribute] -= 1
                    remaining_points += 1
                    sum_of_points -= 1
#        print(remaining_points)
#        for attribute in attributes:
#            if pc[attribute] >= 8 and pc[attribute] < 18:
#                pc[attribute] -= 1
#                remaining_points += 1
#                sum_of_points -= 1
#                print("REMAINING_POINTS-", remaining_points)
#                if remaining_points == 0:
#                    break
#                elif pc[attribute] >= 8 and pc[attribute] < 18:
#                    pc[attribute] -= 1
#                    remaining_points += 1
#                    sum_of_points -= 1
#                    print("REMAINING_POINTS--", remaining_points)
#                    if remaining_points == 0:
#                        break
    return pc, sum_of_points

pc_points = input("Enter the number of PC points: ")

pc, sum_of_points = generate_pc(int(pc_points))
print("PRINT PC ALL ATTRIBUTES",pc)
print("PRINT PC -ST- : ",pc['st'])
print(f"PC Name:{pc['name']}")
attributes = ["st", "dx", "ag", "co", "in", "wi", "pe", "ch"]
for attribute in attributes:
    print(f"{attribute}: {pc[attribute]} TEST {pc[attribute] * 4}%")
    
#SAVE TO TXT

with open("PC-List.txt", "a") as file:
    file.write("###############################################\n")
    file.write(f"PC Name:{pc['name']}\n")
    for attribute in attributes:
         file.write(f"{attribute}: {pc[attribute]} TEST {pc[attribute] * 4}%\n")

print(f"Sum of points spent in attributes: {sum_of_points}")
print(f"PC points spent in attributes: {pc_points}")