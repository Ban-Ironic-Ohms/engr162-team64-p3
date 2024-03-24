import numpy as np

class Map:
    def __init__(self, unit_len, notes) -> None:
        self.team = "64"
        # self.map_num = input("Map Number -> ")
        self.map_num = 0
        
        self.notes = notes
        self.unit_len = unit_len
        self.unit = "cm"
        self.origin = [0, 0]
        # self.map = [[0 for i in range(10)] for i in range(10)]
        self.map = [[5]]
        self.current_cord = [0, 0]
        self.turn_state = [[1, 0], [0, 1]]
        
    
    def _expand_x_l(self, iter=1):
        for i in range(iter):
            for lst in self.map:
                lst.insert(0, 0)
            self.current_cord[0] += 1
            self.origin[0] += 1
        
    def _expand_x_r(self, iter=1):
        for i in range(iter):
            for lst in self.map:
                lst.append(0)
        
        
    def _expand_y_u(self, iter=1):
        for i in range(iter):
            self.map.insert(0, [0 for i in self.map[0]])
        
    def _expand_y_d(self, iter=1):
        for i in range(iter):
            self.map.append([0 for i in self.map[0]])
            self.current_cord[1] += 1
            self.origin[1] += 1
        
    def _place(self, elem, x, y):
        if x > len(self.map[0]):
            self.expand_x_r()
        if y > len(self.map):
            self.expand_y_u()
        
        if elem in range(6):
            self.map[x][y] = elem
        else:
            print(f"ERROR: Cannot use symbol {elem}")
    
    def place_here(self, elem):
        if elem in range(6):
            # print(self.map)
            # print(self.current_cord)
            self.map[len(self.map) - 1 - self.current_cord[1]][self.current_cord[0]] = elem
        else:
            print(f"ERROR: Cannot use symbol {elem}")
        
    def turn(self, angle):
        
        self.turn_state = np.dot([[np.cos(np.deg2rad(angle)), -np.sin(np.deg2rad(angle))], [np.sin(np.deg2rad(angle)), np.cos(np.deg2rad(angle))]], self.turn_state)
        
    def move(self, x, y):
        # print(f"BEFORE TURN: {x}, {y}")
        turned = np.dot(self.turn_state, [x, y])
        x = int(turned[0])
        y = int(turned[1])
        
        self.current_cord[0] += x
        self.current_cord[1] += y
        
        # print(f"AFTER TURN: {x}, {y}")
        
        if self.current_cord[0] > len(self.map[0]) - 1:
            self._expand_x_r(x)
        elif self.current_cord[0] < 0:
            self._expand_x_l(-self.current_cord[0])
            self.origin[0] += -self.current_cord[0]
            self.current_cord[0] = 0
            
        
        if self.current_cord[1] > len(self.map) - 1:
            self._expand_y_u(y)
        elif self.current_cord[1] < 0:
            self._expand_y_d(-self.current_cord[1])
            self.origin[1] += -self.current_cord[1]
            self.current_cord[1] = 0
                
    # def get_origin(self):
        # for iidx, i in enumerate(self.map):
            # for jidx, j in enumerate(i):
                # if j == 5:
                    # return [jidx, iidx]
    
    def __str__(self):
        # self.origin = self.get_origin()
        # print(f"Current Cord: {self.current_cord}")
        ret = f"Team: {self.team}\nMap: {self.map_num}\nUnit Length: {self.unit_len}\nUnit: {self.unit}\nOrigin: ({self.origin[0]}, {self.origin[1]})\nNotes: {self.notes}\n"
        for i in self.map:
            ret += f"{str(i)[1:-1]}\n"
        return ret
    
    def __repr__(self):
        ret = ""
        for i in self.map:
            ret += f"{str(i)[1:-1]}\n"
        return ret
    
if __name__ == "__main__":
    map = Map(10, "hello world 2")

    map.move(1, 1)
    map.place_here(1)
    # print(map)

    map.turn(90)
    map.move(4, 0)
    map.place_here(2)
    print(map)