def monster(atk_power:int, def_power:int, hp:int, level:int):
    if 2 <= level <= 5 :
        add = 1 + ((level - 1) * 0.1)
        atk_power *= add
        def_power *= add
        hp *= add
    return int(atk_power), int(def_power), int(hp)

#print(monster)