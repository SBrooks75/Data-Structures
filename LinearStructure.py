class LinearStructure:
    def __init__(self):
            self.items=[]
	        def isEmpty(self):
		        return self.items==[]
			    def size(self):
			            return len(self.items)
				        def printList(self):
					        for i in range(self.size()):
						            print(self.items[i])




							    class Stack(LinearStructure):
							        def __init__ (self):
								        super().__init__()

									    
									        def push(self,item):
										        self.items.append(item)
											        
												    def pop(self):
												            return self.items.pop()

													        def peek(self):
														        return self.items[len(self.items)-1]






															class Queue(LinearStructure):
															    def __init__(self):
															            super().__init__()
																        def enqueue(self,item):
																	        self.items.insert(0,item)
																		    def dequeue(self):
																		            return self.items.pop()


																			    class Deque(LinearStructure):
																			        def __init__(self):
																				        super().__init__()
																					    def addFront(self,item):
																					            self.items.append(item)
																						        def addRear(self,item):
																							        self.items.insert(0,item)
																								    def removeFront(self):
																								            return self.items.pop()
																									        def removeRear(self):
																										        return self.items.pop(0)
