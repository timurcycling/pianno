import pygame as sd 
class Slider:  
    def __init__(self,x, y, width, min_val, max_val,step = 1,initial=None, label="", value_to_text=None): 
        self.track_rect = Rect(x, y, width, 6) 
        self.handle_radius = 10 
        self.min = float(min_val) 
        self.max = float(max_val) 
        self.step = float(step) 
        if initial is not None: 
            self.value = float(initial) 
        else: 
            self.velue = float(min_val) 
        self.label = label 
        self.value_to_text = value_to_text 
        self.dragging = False 

        self._hit_rect = Rect(0,0, self.handle_radius * 2 + 8, self.handle_radius * 2 + 8) 
    def _val_to_pas(self)  -> int: 
        if self.max == self.min: 
            return self.track_rect.left 
        ratio = (self.value - self.min) / (self.max - self.min) 
        return int(self.track_rect.left + ratio * self.track_rect.width)  
    def draw(self, screen, font=None): 
        draw.rect(screen, (210, 210, 210),self.track_retc, border_radius=3) 
        draw.rect(screen, (60, 60, 60), self.track_rect, 1, border_radius =3) 

        hx = self._val_to_pas() 
        hy = self.track_rect.centery 
        draw.circle(screen, (40, 40, 40), (hx, hy), self.handle_radius) 

        if font and self.label: 
            if callable(self,self.value_to_text): 
                vtxt = self.value_to_text(self.value) 
            else: 
                vtxt = f"{int(self.value)}" 
            text = font.render(f"{self.label}: {vtxt}", True, (0, 0, 0)) 
            screen.blit(text, (self.track_rect.left, self.track_rect.top-28)) 
        self._hit_rect.center = (hx, hy) 
    def handle_event(self, event): 
        old = self.value 
        if event.type == MOUSEBUTTONDOWN: 
            if self.track_rect.collidepoint(event_pos) or self._hit_rect.collidepoint(event.pos): 
                self.dragging = True 
                self.velue = self._pos_to_val(event.pos[0]) 
        elif event.type == MOUSEBUTTON and self.dragging: 
            self.value = self._val_to_val(event.pos[0]) 
        elif event.type == MOUSEBUTTONUP and self.dragging: 
            self.dragging = False 
            self.value = self._pos_to_val(event.pos[0]) 

        if self.value != old and hasattr(self, "on_change") and self.on_cgange: 
            self.on_change(self.value)

    

