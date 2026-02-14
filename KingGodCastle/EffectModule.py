#_______Version 0.9 _______
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import RenderContext, Rectangle
from kivy.clock import Clock
from kivy.uix.label import Label

from kivy.utils import get_color_from_hex


class ShaderWidget(Widget):
		
	time = 0.0
	strength = 0.17
	mod = 1.0
	
	color = (get_color_from_hex('#718E54'))
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.opacity = self.strength
		# Create a render context with shader
		
		#self.color = (get_color_from_hex('#718E54'))
		#self.color = (get_color_from_hex('#8C5E54'))
		
		self.canvas = RenderContext(use_parent_projection=True)

		self.canvas.shader.source = 'Effect.glsl'
		with self.canvas:
			self._rect = Rectangle(pos=self.pos, size=self.size)
			# Bind widget properties to update methods
			self.bind(pos=self.update_rect,size=self.update_rect)
			Clock.schedule_interval(self.update_time, 1/60.)
			self.canvas['strength'] = self.strength
			
	def update_rect(self, *args):
		# Update rectangle position and size
		self._rect.pos = self.pos
		self._rect.size = self.size
	
	def update_time(self,dt):
		self.time+=dt
		if self.time <= 1.1:
			self.canvas['time'] = self.time
			self.canvas['colour']=[
			
			round(self.color[0],1),
			round(self.color[1],1),
			round(self.color[2],1)
			
			]
			self.canvas['speedmodifier'] = self.mod
			
        
        
class MyApp(App):
	def build(self):
		return ShaderWidget()
		
if __name__=='__main__':
	MyApp().run()