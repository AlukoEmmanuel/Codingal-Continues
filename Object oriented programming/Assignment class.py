class Robot:
    species = "mechanical being"
    
    def __init__(self, model, c):
        self.model = model
        self.color = c
        
    def play_song(self, s):
        print(self.model, "is playing", s)
        
    def dance(self):
        print(f"I am a {self.species} of {self.color} color and perform dance routines with motorized moves")

# Create robot instances
o1 = Robot("RoboX-9000", "silver")
o1.play_song("praise song")
o1.dance()

o2 = Robot("CyberNova-5", "neon blue")
o2.play_song("Worship song")
o2.dance()