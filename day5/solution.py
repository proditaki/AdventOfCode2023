import os
import re

seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []
#lines=[]
seeds = []
seeds2 = []
seedMap = []

def setup():
    input_filename = 'input5.txt'
    input_file = os.path.join(os.getcwd(), input_filename)

    fHandle = open(input_file, 'r')

    lines = fHandle.readlines()
    answer = 0
    
    global seeds,seeds2
    seeds = [list(map(int, x.strip()[7:].split(' '))) for x in lines if x.startswith('seeds:')][0]
    for x in range(len(seeds)):
        if x%2 == 0:
            seeds2.append([seeds[x],seeds[x+1]])
    

    seed_to_soil_map_line = [x for x, line in enumerate(lines) if 'seed-to-soil' in line][0]   
    soil_to_fertilizer_map_line = [x for x, line in enumerate(lines) if 'soil-to-fertilizer' in line][0]
    fertilizer_to_water_map_line = [x for x, line in enumerate(lines) if 'fertilizer-to-water' in line][0]
    water_to_light_map_line = [x for x, line in enumerate(lines) if 'water-to-light' in line][0]
    light_to_temperature_map_line = [x for x, line in enumerate(lines) if 'light-to-temperature' in line][0]
    temperature_to_humidity_map_line = [x for x, line in enumerate(lines) if 'temperature-to-humidity' in line][0]
    humidity_to_location_map_line = [x for x, line in enumerate(lines) if 'humidity-to-location' in line][0]  

    for x in range(seed_to_soil_map_line+1,soil_to_fertilizer_map_line):
        line = lines[x].strip()
        if len(line) > 0:
            seed_to_soil_map.append(list(map(int, line.split(' '))))
    
    for x in range(soil_to_fertilizer_map_line+1,fertilizer_to_water_map_line):
        line = lines[x].strip()
        if len(line) > 0:
            soil_to_fertilizer_map.append(list(map(int, line.split(' '))))

    for x in range(fertilizer_to_water_map_line+1,water_to_light_map_line):
        line = lines[x].strip()
        if len(line) > 0:
            fertilizer_to_water_map.append(list(map(int, line.split(' '))))

    for x in range(water_to_light_map_line+1,light_to_temperature_map_line):
        line = lines[x].strip()
        if len(line) > 0:
            water_to_light_map.append(list(map(int, line.split(' '))))

    for x in range(light_to_temperature_map_line+1,temperature_to_humidity_map_line):
        line = lines[x].strip()
        if len(line) > 0:
            light_to_temperature_map.append(list(map(int, line.split(' '))))

    for x in range(temperature_to_humidity_map_line+1,humidity_to_location_map_line):
        line = lines[x].strip()
        if len(line) > 0:
            temperature_to_humidity_map.append(list(map(int,line.split(' '))))

    for x in range(humidity_to_location_map_line+1,len(lines)):
        line = lines[x].strip()
        if len(line) > 0:
            humidity_to_location_map.append(list(map(int, line.split(' '))))

def solve2():
    global seedMap
    result = 0xFFFFFFFF
    for s, sl in seeds2:

        seedMap = [(s,s+sl-1)]
        #print(seedMap)      
        for toMap in [seed_to_soil_map,soil_to_fertilizer_map,fertilizer_to_water_map,water_to_light_map,light_to_temperature_map,temperature_to_humidity_map,humidity_to_location_map]:
            newMap =[]
            for low,high in seedMap:
                foundRange = False
                for dst,src,range in toMap: 
                    if low >= src and high < src + range:
                        newMap.append((low - src + dst, high - src + dst))
                        foundRange = True
                        break

                    elif low < src and high >= src + range:
                        seedMap.append((low, src - 1))
                        newMap.append((dst, dst + range - 1))
                        seedMap.append((src + range, high))
                        foundRange = True                
                        break

                    elif low < src and high >= src and high < src + range:
                        seedMap.append((low, src - 1))
                        newMap.append((dst, dst + high - src))
                        foundRange = True
                        break

                    elif low < src + range and high >= src + range and low >= src:
                        seedMap.append((src + range, high))
                        newMap.append((dst + low - src, dst + range - 1))
                        foundRange = True
                        break

                if not foundRange:
                    newMap.append((low, high))
            seedMap = newMap.copy()
        result = min(result, min(seedMap)[0])
    print(result)
def findRange(searchValue, map):
    value = searchValue

    for x,y,z in map:
        if value >= y and value <= y+z:
            return x+(value-y)
    return value

def findAnswer(seed):
    return findRange(
                findRange(
                    findRange(
                        findRange(
                            findRange(
                                findRange(
                                    findRange(seed,seed_to_soil_map)
                                    ,soil_to_fertilizer_map)
                                ,fertilizer_to_water_map)
                        ,water_to_light_map)
                    ,light_to_temperature_map)
                ,temperature_to_humidity_map)
           ,humidity_to_location_map)
def solve():
    #print(seeds)
    answers = {}
    for seed in seeds:
        answers[seed] = findAnswer(seed)
    #print(answers)
    #print('\n')
    #for ans in answers:
     #   print(ans, answers[ans])
    print(min(answers.values()))

if __name__ == "__main__":
    setup()
    solve()
    solve2()
    

