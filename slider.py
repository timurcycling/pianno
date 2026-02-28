class Slider: 
     def __init__(self, x, y, width, min_val, max_val, step=1, initial=None,label='', value_to_text=None): 
         self.track_rect = Rect(x, y, width, 6) 
     self.handle_radius = 10 
     self.min = float(min_val) 
     self.max = float(max_val) 
     self.step = float(step) 
     if initial is not None: 
          self.value = float(initial) 
     else: 
          self.value = float(min_val) 
     self.label = label 
     self.value_to_text = value_to_text 
     self.dragging = False 
     self._hit_rect = Rect(0,0, self.handle_radius * 2 + 8, self.handle_radius * 2 + 8)  
     def _val_to_pas(self) -> int: 
          if self.max == self.min: 
                return self.track_rect.left 
          ratio = (self.value - self.min) / (self.max - self.min) 
          return int(self.track_rect.left + ratio * self.track_rect.width
       
  
