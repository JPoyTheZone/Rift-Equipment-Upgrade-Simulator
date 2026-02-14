#_______Version 0.9 _______

import kivy
import UpgradeModule
import EffectModule

from EffectModule import ShaderWidget
from UpgradeModule import RiftEquipment

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import *
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.clock import Clock



from kivy.utils import get_color_from_hex


from kivy.lang import Builder

InitialLevel = 0
TargetLevel = NumericProperty(0)
SimulationNumber = 0
Status = "!!Success!!"
Successes = 0
Fails = 0

def update_text(widget,text,lvl):
		widget.text= text+str(lvl)
		
class SimulatorSettings(Screen):
	
	global TargetLevel
	global SimulationNumber
	
	initlvl = ObjectProperty(None)
	tarlvl = ObjectProperty(None)
	simno = ObjectProperty(None)

	def __Init__(self,**kwargs):
		super(self).__init__(**kwargs)
		self.initlvl = self.initlvl.text
		self.tarlvl = self.tarlvl.text
		self.target_widget = target_widget
		self.simno = self.simno.text
		
	def Start_Consecutive_Upgrade(self,btn):
		InitialLevel = self.initlvl.text
		TargetLevel = self.tarlvl.text
		SimulationNumber = self.simno.text
		#	btn.text = App.InitialLevel
		UpgradeScreen = self.parent.ids['UpgSim']
		UpgradeScreen.start_upgrading()
			
	pass





class UpgradeSimulator(Screen):
	c = get_color_from_hex('#333333')
	color = ColorProperty(c)
	curlvl = ObjectProperty(None)
	stat = ObjectProperty(None)
	succ = ObjectProperty(None)
	fail = ObjectProperty(None)
	atcount = ObjectProperty(None)
	
	feed = ObjectProperty(None)
	interv = 2
		
	def __Init__(self,**kwargs):
		super(self).__init__(**kwargs)
		
	def start_upgrading(self):
		
		InitialLevel = int(self.manager.ids['SimSet'].ids['Initlvl'].text)
		
		self.curlvl.text = f"Current Lvl:  {InitialLevel}"
		self.stat.text = "Status:  -/-/-/-/-/- "
		
		update_text(self.curlvl,f"Current Lvl: ",InitialLevel)
		self.myRiftEquipment = RiftEquipment(InitialLevel)
		self.UpgradeEffect = ShaderWidget()
		self.add_widget(self.UpgradeEffect)
		self.UpgradeEffect.color = self.color

		Clock.schedule_once(self.upgrade,2)
	def upgrade(self,dt):
		
		

		
		if self.myRiftEquipment.status:
			self.UpgradeEffect.time = 0.0
			self.myRiftEquipment.upgrade()
		
			CLevel = self.myRiftEquipment.level
			Stat = self.myRiftEquipment.feedback
			Att = self.myRiftEquipment.getAttempts()
			SCS = self.myRiftEquipment.successes
			FLS = self.myRiftEquipment.fails
			
			if Stat == "-Upgrade Success!--":
				self.color = (get_color_from_hex('#718E54'))
				self.UpgradeEffect.color = self.color	
			elif Stat == "--'UpgradeFailed'--":
				self.color = (get_color_from_hex('#8C5E54'))
				self.UpgradeEffect.color = self.color
			else:
				self.color = self.c
				self.UpgradeEffect.color = self.color
				
				
			self.atcount.text =f"--Attempt {Att}--"
			self.curlvl.text = f"Current Lvl: {CLevel}"
			self.stat.text = f"Status:{Stat}"
			self.succ.text = f"Successes: {SCS} "
			self.fail.text = f"Fails:  {FLS}"
	
			#add a text to feed every upgrade
			self.feed.text += f"Rift Equipment Lvl ({CLevel}) {Stat} \n"
			if self.interv >= 0.3:
				self.interv -= 0.2
				self.UpgradeEffect.mod = 1/self.interv
			Clock.schedule_once(self.upgrade,self.interv)
		

		
	

class WindowManager(ScreenManager):
	pass
	

class myLayout(Widget):
	pass

kv = Builder.load_file('REKV.kv')

class MyApp(App):
	def build(self):
		InitialLevel = NumericProperty(0)
		UpgSimu = UpgradeSimulator()
		SimSett = SimulatorSettings()
		return kv


if __name__ == '__main__':
	MyApp().run()
	