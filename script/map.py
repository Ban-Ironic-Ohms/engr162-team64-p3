class Map:
    def __init__(self, unit_len, notes) -> None:
        self.team = "64"
        # self.map_num = input("Map Number -> ")
        self.map_num = 0
        
        self.notes = notes
        self.unit_len = unit_len
        self.unit = "cm"
        self.origin = [0, 0]
        self.map = [[0 for i in range(10)] for i in range(10)]
        self.current_cord = [0, 0]
    
    def expand_x_l(self):
        for lst in self.map:
            lst.insert(0, 0)
        self.current_cord[0] += 1
        
    def expand_x_r(self):
        for lst in self.map:
            lst.append(0)
        
    def expand_y_u(self):
        self.map.insert(0, [0 for i in self.map[0]])
        
    def expand_y_d(self):
        self.map.append([0 for i in self.map[0]])
        self.current_cord[1] += 1
    
    def place(self, elem, x, y):
        if x > len(self.map[0]):
            self.expand_x_r()
        if y > len(self.map):
            self.expand_y_u()
        
        if elem in range(6):
            self.map[x][y] = elem
        else:
            print(f"ERROR: Cannot use symbol {elem}")
    
    def move(self, x, y):
        self.current_cord[0] += x
        self.current_cord[1] += y
    
    def get_origin(self):
        for iidx, i in self.map:
            for jidx, j in i:
                if j == 5:
                    return [jidx, iidx]
    
    def __str__(self):
        ret = f"Team: {self.team}\nMap: {self.map_num}\nUnit Length: {self.unit_len}\nUnit: {self.unit}\nOrigin: ({self.origin[0]}, {self.origin[1]})\nNotes: {self.notes}\n"
        for i in self.map:
            ret += f"{i}\n"
        return ret