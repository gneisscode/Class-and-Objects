class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = [tracks]
        self.score = float(score)
        
    def get_score(self):
       print(self.score)

    def add_track(self, tracks):
        self.tracks.append(tracks)

    def change_age(self, age):
        self.age=age

    def change_name(self, name):
        self.name=name
        


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
