class Block:
    """
    Building blocks Kata
    https://www.codewars.com/kata/55b75fcf67e558d3750000a3
    """
    def __init__(self, dimensions):
        self.width = dimensions[0]
        self.length = dimensions[1]
        self.height = dimensions[2]
        
    def get_width(self):
        return self.width
        
    def get_length(self):
        return self.length
        
    def get_height(self):
        return self.height
        
    def get_volume(self):
        return self.get_width()*self.get_length()*self.get_height()
        
    def get_surface_area(self):
        return 2*(self.get_width()*self.get_length()+self.get_height()*self.get_length()+self.get_height()*self.get_width())