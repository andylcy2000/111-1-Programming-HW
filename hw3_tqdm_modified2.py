from tqdm import tqdm, trange
#我把tqdm的range設成目前遇到跑最久的，所以可能會出現進度條還沒跑完就已經跑出結果的情況

class Maze:
	

	space_symbol = " "
	obstacle_symbol = "X"
	path_symbol = "•"

	def __init__(self,args):
		if args.endswith("txt"):
			with open (args,"r") as content:
				self.maze=content.read()
			
		else:
			self.maze=args
		"""(9 pts)
		Using input input_str to construct your maze, and any other resource that can help you find the
		shortest path, such as adjacency list, predecessor list...

		Your conctructer will take one parameter input_str, which can be either a filename or a whole graph,
		so you need to deal with constructor overloading here.
		"""
	def __str__(self):
		"""(5 pts)
		Print the whole 20*20 maze using "X" or " " by operator overloading, no spaces is needed between
		two characters.
		"""
		return self.maze

	@classmethod
	def set_space_symbol(cls,args):
		"""(2 pts)
		This Method should take one parameter with string type and replace the original space_symbol with it.
		Note that using Maze.space_symbol = ... is prohibited.

		Hint: Function decorator.
		"""
		cls.space_symbol=args

	@classmethod
	def set_obstacle_symbol(cls,args):
		"""(2 pts)
		This Method should take one parameter with string type and replace the original obstacle_symbol with it.
		Note that using Maze.obstacle_symbol = ... is prohibited.

		Hint: Function decorator.
		"""
		cls.obstacle_symbol=args
		

	@classmethod	
	def set_path_symbol(cls,args):
		"""(2 pts)
		This Method should take one parameter with string type and replace the original path_symbol with it.
		Note that using Maze.path_symbol = ... is prohibited.

		Hint: Function decorator.
		"""
		cls.path_symbol=args
	
	def find_shortest_path(self):
		"""(35 pts)
		Using either BFS/Dijkstra or any other algorithms you desire to find the
		shortest path and its length in the maze.

		The points of this part will be automatically given if the results of dis_of_shortest_path and 
		print_shortest_path is both correct, so for those who thinks that your code will 100% pass, feel 
		free to move the algorithm part from this function to any where else you desire.

		But IF your code fail, I will judge your code in this function to give you partial credits from 
		these 35 points, so it's better for you to write the algorithm in this function no matter what. 
		"""
        
		point_visited=[]
		current_loc=(0,0)
        
		#current_steps=0
		#surrounding_steps=[]
		self.dist_maze=[]
		for i in range(20):
			v=[]
			for k in range(20):
				v.append(1000)
			self.dist_maze.append(v)
		self.real_maze=[]
		
		queue=[]
        
		row=self.maze.split("\n")
		for i in range(len(row)) :
			now_row=[]
			for j in range(len(row[i])):
				now_row.append(row[i][j])
				if row[i][j]=="S":
					current_loc=(j,i)
                                      
					queue.append((j,i,0))
                    
					self.dist_maze[i][j]=0

				elif row[i][j]=="T":
					f_loc=(j,i)
			self.real_maze.append(now_row)
		#print(real_maze)
		#print(current_loc)
		self.s=current_loc
		self.f=f_loc
		progress = tqdm(total=24000)
		#step=0
		while check:
			progress.update(1)
			#step+=1
			min=1000000000
			for i in queue:
				if i[2]<min:
					min=i[2]

			for i in range(len(queue)):
				if min==queue[i][2]:
					current_loc=queue.pop(i)
					break
			x=current_loc[0]
			y=current_loc[1]
			
			point_visited.append((x,y))
			
			if (x+1,y) not in point_visited and x+1<20:
                if self.real_maze[y][x+1]==Maze.space_symbol:
                    self.dist_maze[y][x+1]=self.dist_maze[y][x]+1
                    if (x+1,y,self.dist_maze[y][x+1]) not in queue:
                        queue.append((x+1,y,self.dist_maze[y][x+1]))

                elif self.real_maze[y][x+1]=="T":

					self.dis=current_loc[2]
					check=False


			if (x-1,y) not in point_visited and x-1>-1:
					#if self.real_maze[y][x-1]==Maze.obstacle_symbol:
						#self.dist_maze[y][x-1]=self.dist_maze[y][x]+1000000
				if self.real_maze[y][x-1]==Maze.space_symbol:
					self.dist_maze[y][x-1]=self.dist_maze[y][x]+1
                    if (x-1,y,self.dist_maze[y][x-1]) not in queue:
						queue.append((x-1,y,self.dist_maze[y][x-1]))

                elif self.real_maze[y][x-1]=="T":
						#print(step)
					self.dis=current_loc[2]
					check=False
			if (x,y+1) not in point_visited and y+1<20:
				
					#if self.real_maze[y+1][x]==Maze.obstacle_symbol:
						#self.dist_maze[y+1][x]=self.dist_maze[y][x]+1000000
				if self.real_maze[y+1][x]==Maze.space_symbol:
					self.dist_maze[y+1][x]=self.dist_maze[y][x]+1
                    if (x,y+1,self.dist_maze[y+1][x]) not in queue:
						queue.append((x,y+1,self.dist_maze[y+1][x]))

				elif self.real_maze[y+1][x]=="T":
						#print(step)
					self.dis=current_loc[2]
					check=False
			if (x,y-1) not in point_visited and y-1>-1:
					#if self.real_maze[y-1][x]==Maze.obstacle_symbol:
						#self.dist_maze[y-1][x]=self.dist_maze[y][x]+1000000
				if self.real_maze[y-1][x]==Maze.space_symbol:
					self.dist_maze[y-1][x]=self.dist_maze[y][x]+1		
                    if (x,y-1,self.dist_maze[y-1][x]) not in queue:
						queue.append((x,y-1,self.dist_maze[y-1][x]))

				elif self.real_maze[y-1][x]=="T":
						#print(step)
					self.dis=current_loc[2]
					check=False

	def dis_of_shortest_path(self):
		"""(20 pts)
		Print the length of shortest path. The length should not include "S" or "T".
		For example, 
			S•••••••T -> path's distance:7
			
			S••
			  •  ••T  -> path's distance:9
			  ••••
		"""
		return self.dis
	def print_shortest_path(self):
		"""(25 pts)
		Print the oringinal maze plus the shortest path. The shortest path should be
		composed of path_symbol(by default, it should be "•"), for example:

			XXXXXXXXX
			S•••••XXX
			X XXX•X•T
			X X  •••X
			X   XXXXX
			XXXXXXXXX

		If there is more than one shortest path, you only need to display one of them.
		"""
		current_loc=self.f
		x=current_loc[0]
		y=current_loc[1]
		self.dist_maze[y][x]=self.dis+1
		#for i in self.dist_maze:
			#print(i)
		
		while True:
			x=current_loc[0]
			y=current_loc[1]
			#print(current_loc)
			check=0
			if x+1<20:
				if self.real_maze[y][x+1]=="S":
					break

				elif self.dist_maze[y][x+1]==(self.dist_maze[y][x]-1):
						check=1
						self.real_maze[y][x+1]=self.path_symbol
						current_loc=(x+1,y)
						
			if x-1>-1 and check==0:
				if self.real_maze[y][x-1]=="S":
					break

				elif self.dist_maze[y][x-1]==(self.dist_maze[y][x]-1):
						check=1
						self.real_maze[y][x-1]=self.path_symbol
						current_loc=(x-1,y)
			if y+1<20 and check==0:
				if self.real_maze[y+1][x]=="S":
					break

				elif self.dist_maze[y+1][x]==(self.dist_maze[y][x]-1):
						check=1
						self.real_maze[y+1][x]=self.path_symbol
						current_loc=(x,y+1)
			if y-1>-1 and check==0:
				if self.real_maze[y-1][x]=="S":
					break

				elif self.dist_maze[y-1][x]==(self.dist_maze[y][x]-1):
						check=1
						self.real_maze[y-1][x]=self.path_symbol
						current_loc=(x,y-1)

		for i in self.real_maze:
			for j in i:
				print(j,end="")

			print()




maze_graph_input =  "OOOOOOOOOOOOOOOOOOOO\n"  \
 					"SCOCCOCOCCCOCCCOOCOO\n"  \
 					"OCCOCCOCCCCCCOOOCCOO\n"  \
 					"OOCCCCCCCOOCOCOOCCOO\n"  \
 					"OCOCCOCOCCCCOOCOCOCO\n"  \
 					"OCOOCCCCOOCCCCCCCCCO\n"  \
 					"OCCCCCCCOOOOCCOOCOOO\n"  \
 					"OCCCOOCCCOCCCOOCCCCO\n"  \
 					"OCCOCCOOCOCOOCCOCOCO\n"  \
 					"OCOOCCCOCCCCCCCCOOCO\n"  \
 					"OCCCCCOOCCOCCOCOCCCO\n"  \
 					"OOOCOCCOOCOCOOCCCCOO\n"  \
 					"OCCCCCOOOCCCCCOCCCOO\n"  \
 					"OOCCCCCCOOCCCCCCOCCO\n"  \
 					"OOOCCCCCOOCCCCCOCOOO\n"  \
 					"OCCCCOCCOCOOOOOOOOOO\n"  \
 					"OCOCCCOOCCOCOCCCCCCO\n"  \
 					"OOCOCCCCCOOOOCOOOCOO\n"  \
 					"OOCOCOOCCCCCCCCCOCCT\n"  \
 					"OOOOOOOOOOOOOOOOOOOO\n"



if __name__=="__main__":
	#Maze.set_obstacle_symbol("O")
	Maze.set_obstacle_symbol("O")
	Maze.set_space_symbol("C")
	Maze.set_path_symbol(" ")
	m=Maze(maze_graph_input)
	# print(m)
	m.find_shortest_path()
	print(m.dis)
	#for i in m.dist_maze:
		#print(i)
	m.print_shortest_path()
	#m.find_shortest_path()
	#print(m.obstacle_symbol)
	