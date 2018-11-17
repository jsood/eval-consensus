class Driver: 
	def setup():
		self.start_time = None
		self.end_time = None
		self.start_ctime = None
		self.end_ctime = None
		
	def calc_elapsed_time():
		# end_time - start_time
		return self.end_time - self.start_time

	def calc_cpu_time():
		# end_ctime - start_ctime
		return self.end_ctime - self.start_ctime
	
	def calc_memory():
		# calc memory utilised
		
# Receive handlers to receive messages from implementaions we chose
	def receive_start_statistics(msg=('start', start_time, start_ctime)):
		# start_time, start_ctime
		self.start_time = start_time
		self.start_ctime = start_ctime
	
	def receive_end_statistics(msg=('end', end_time, end_ctime)):
		# end_time, end_ctime
		self.end_time = end_time
		self.end_ctime = end_ctime
		
	def run():
		
		send(('done', self), to = parent())
		print("ELAPSED TIME:", calc_elapsed_time())
		print("CPU TIME:", calc_cpu_time())
		print("MEMORY UTILIZED:", calc_memory())
        	await(received(('done',), from_ = parent()))
			
def main():
	# n_proposers, n_learners, n_acceptors, repetitions
	# setup and start processes
