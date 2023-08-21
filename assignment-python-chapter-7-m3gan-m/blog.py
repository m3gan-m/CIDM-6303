# Simulate blog posts to practice classes and objects
# Follow the instructions. Start coding here. 
#megan moore

class Blog():
    def __init__(self,message):
        #create two attributes of message and how many likes
        self.message = message
        self.likes = 0
    def post(self):
        #print the post to the terminal
        print(self.message)

#write several blog mesages and create objects of class Blog()
blog1 = Blog("What are the mains points of CHapter 7?")
blog2 = Blog("Classes are blueprints of objects")
blog3 = Blog("Objects are instances of classes.")
blog4 = Blog("THis is called Object Oriented Programming OOP")
blog5 = Blog("Classes should use Pascal naming convention")

#output blogs
blog1.post()
blog2.post()
blog3.post()
blog4.post()
blog5.post()

#set some likes on certain blogs
blog1.likes=2
blog3.likes=3
print(blog1.likes)
print(blog2.likes)
print(blog3.likes)