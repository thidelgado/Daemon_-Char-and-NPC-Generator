import random
import sys

monster_type = int(input("Type of monster (1- very common, 2- common, 3- uncommon, 4- rare, 5- unique): "))

attribute = "Type of monster"
value = monster_type

print(f"{attribute}: {value} - ", end="")

if monster_type == 1:
    npc_points = 70
    m_type = ("very common ", npc_points)
    print(m_type)
elif monster_type == 2:
    npc_points = 80
    m_type = ("common ", npc_points)
    print(m_type)
elif monster_type == 3:
    npc_points = 95
    m_type = ("uncommon ", npc_points)
    print(m_type)
elif monster_type == 4:
    npc_points = 105
    m_type = ("rare ", npc_points)
    print(m_type)
elif monster_type == 5:
    npc_points = 115
    m_type = ("unique ", npc_points)
    print(m_type)
else:
    npc_points = 0
    print("Invalid input")

########### NPC Generation

def generate_npc(npc_points):
    attributes = ["st", "dx", "ag", "co", "in", "wi", "pe", "ch"]
    npc = {}
    global total_spent
    total_points = npc_points
    for attribute in attributes:
        if npc_points <= 80:
            attribute_points = random.randint(7, 13)
        else:
            attribute_points = random.randint(8, 15)
        if total_points - attribute_points < 0:
            attribute_points = total_points
        npc[attribute] = attribute_points
        total_points -= attribute_points

    npc["name"] = input("Enter NPC name: ")
    
    total_spent = sum(value for attribute, value in npc.items() if isinstance(value, int))
    if total_spent != npc_points:
        while total_spent != npc_points:
            for attribute in attributes:
                if total_spent > npc_points:
                    npc[attribute] -= 1
                    total_spent -= 1
                elif total_spent < npc_points:
                    npc[attribute] += 1
                    total_spent += 1
                
    return npc

#### PRINT NPC STATS

npc = generate_npc(npc_points)
print(f"NPC Name: {npc['name']}")
for attribute, value in npc.items():
    #print(len(str(value)))
        if attribute != "name":
            if (len(str(value)))==2:
                print(f"{attribute}: {value} TEST {value * 4}%")
            elif (len(str(value)))==1:
                print(f"{attribute}: {value}  TEST {value * 4}%")
print(total_spent)

        
#### SAVE NPC STATS TO THE FILE

with open("NPC-List.txt", "a") as file:
    file.write("###############################################\n")
    file.write(f"Monster type: {monster_type} {m_type}\n")
    file.write(f"NPC Name: {npc['name']}\n")
    for attribute, value in npc.items():
        if attribute != "name":
            if (len(str(value)))==2:
                file.write(f"{attribute}: {value} TEST {value * 4}%\n")
            elif (len(str(value)))==1:
                file.write(f"{attribute}: {value}  TEST {value * 4}%\n")