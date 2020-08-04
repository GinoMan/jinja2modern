class ParserError(Exception):
	def __init__(self, msg, response=None):
		self.response = response
		super().__init__(self, msg)
