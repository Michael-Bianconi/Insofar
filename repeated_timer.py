"""Repeated Timer"""

from threading import Timer

class RepeatedTimer():
	
	def __init__(self,interval,function,*args,**kwargs):
		self.timer = None
		self.interval = interval
		self.function = function
		self.args = args
		self.kwargs = kwargs
		self.running = False
		self.start()

	def _run(self):
		self.running = False
		self.start()
		self.function(*self.args,**self.kwargs)
		
	def start(self):
		if not self.running:
			self._timer = Timer(self.interval,self._run)
			self._timer.start()
			self.running = True
			
	def stop(self):
		self._timer.cancel()
		self.running = False