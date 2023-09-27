class Person():
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
if __name__ == "__main__":
    print(Person("Jim", "Stuart", "12-11-1985").full_name())
