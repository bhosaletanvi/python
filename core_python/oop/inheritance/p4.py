class centralGov :
	def __init__(self):
		print("in parent constructor");
	
class StateGov(centralGov):
	def __init__(self):
		super().__init__();
		print("in child constructor");

c1=StateGov();
