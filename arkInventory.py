#importing random library to generate random numbers
import random

#creating Cat class  
class Cat():
    #constructing the class
    def __init__(self, a, g, bP):
        self.age = a
        self.gender = g
        self.birthPeriod = bP

    #updating cats ages when time pass
    def updateAge(self):
        self.age += 1
    #it is time to give birth for female cats (male or female is random)
    def giveBirth(self):
        global Cats
        randomNumber = random.randint(0,1)
        if self.gender == True:
            if self.age % self.birthPeriod == 0 and self.age != 0:
                if randomNumber == 0:
                    Cats.append(Cat(-1, False, 12))
                elif randomNumber == 1:
                    Cats.append(Cat(-1, True, 12))
    #returning string to display features of the cat
    def __str__(self):
        if self.gender == True:
            gender = "female cat, "
        else:
            gender = "male cat, "
        return "I am a {} {} months old".format(gender, self.age)  
class Dog():
    #constructing the class
    def __init__(self, a, g, bP):
        self.age = a
        self.gender = g
        self.birthPeriod = bP

    #updating dogs ages when time pass
    def updateAge(self):
        self.age += 1
    #it is time to give birth for female dogs (male or female is random)
    def giveBirth(self):
        global Dogs
        randomNumber = random.randint(0,1)
        if self.gender == True:
            if self.age % self.birthPeriod == 0 and self.age != 0:
                if randomNumber == 0:
                    Dogs.append(Dog(-1, False, 12))
                elif randomNumber == 1:
                    Dogs.append(Dog(-1, True, 12))
    #returning string to display features of the dog
    def __str__(self):
        if self.gender == True:
            gender = "female dog, "
        else:
            gender = "male dog, "
        return "I am a {} {} months old".format(gender, self.age)
class Shark():
    #constructing the class
    def __init__(self, a, g, bP):
        self.age = a
        self.gender = g
        self.birthPeriod = bP

    #updating Sharks ages when time pass
    def updateAge(self):
        self.age += 1
    #it is time to give birth for female sharks (male or female is random)
    def giveBirth(self):
        global Sharks
        randomNumber = random.randint(0,1)
        if self.gender == True:
            if self.age % self.birthPeriod == 0 and self.age != 0:
                if randomNumber == 0:
                    Sharks.append(Shark(-1, False, 6))
                elif randomNumber == 1:
                    Sharks.append(Shark(-1, True, 6))
    #returning string to display features of the shark
    def __str__(self):
        if self.gender == True:
            gender = "female Shark, "
        else:
            gender = "male Shark, "
        return "I am a {} {} months old".format(gender, self.age)
class Goldfish():
    #constructing the class
    def __init__(self, a, g, bP):
        self.age = a
        self.gender = g
        self.birthPeriod = bP

    #updating Goldfishs ages when time pass
    def updateAge(self):
        self.age += 1
    #it is time to give birth for female goldfishs (male or female is random)
    def giveBirth(self):
        global Goldfishs
        randomNumber = random.randint(0,1)
        if self.gender == True:
            if self.age % self.birthPeriod == 0 and self.age != 0:
                if randomNumber == 0:
                    Goldfishs.append(Goldfish(-1, False, 6))
                elif randomNumber == 1:
                    Goldfishs.append(Goldfish(-1, True, 6))
    #returning string to display features of the goldfish
    def __str__(self):
        if self.gender == True:
            gender = "female Goldfish, "
        else:
            gender = "male Goldfish, "
        return "I am a {} {} months old".format(gender, self.age)
class Eagle():
    #constructing the class
    def __init__(self, a, g, bP):
        self.age = a
        self.gender = g
        self.birthPeriod = bP

    #updating eagles ages when time pass
    def updateAge(self):
        self.age += 1
    #it is time to give birth for female eagles (male or female is random)
    def giveBirth(self):
        global Eagles
        randomNumber = random.randint(0,1)
        if self.gender == True:
            if self.age % self.birthPeriod == 0 and self.age != 0:
                if randomNumber == 0:
                    Eagles.append(Eagle(-1, False, 9))
                elif randomNumber == 1:
                    Eagles.append(Eagle(-1, True, 9))
    #returning string to display features of the eagle
    def __str__(self):
        if self.gender == True:
            gender = "female Eagle, "
        else:
            gender = "male Eagle, "
        return "I am a {} {} months old".format(gender, self.age)
class Parakeet():
    #constructing the class
    def __init__(self, a, g, bP):
        self.age = a
        self.gender = g
        self.birthPeriod = bP

    #updating parakeets ages when time pass
    def updateAge(self):
        self.age += 1
    #it is time to give birth for female parakeets (male or female is random)
    def giveBirth(self):
        global Parakeets
        randomNumber = random.randint(0,1)
        if self.gender == True:
            if self.age % self.birthPeriod == 0 and self.age != 0:
                if randomNumber == 0:
                    Parakeets.append(Parakeet(-1, False, 9))
                elif randomNumber == 1:
                    Parakeets.append(Parakeet(-1, True, 9))
    #returning string to display features of the parakeet
    def __str__(self):
        if self.gender == True:
            gender = "female Parakeet, "
        else:
            gender = "male Parakeet, "
        return "I am a {} {} months old".format(gender, self.age)

#creating the starting animals and lists for animals
Cat1 = Cat(0, True, 12)
Cat2 = Cat(0, False, 12)
Cats = [Cat1, Cat2]

Dog1 = Dog(0, True, 12)
Dog2 = Dog(0, False, 12)
Dogs = [Dog1, Dog2]

Shark1 = Shark(0, True, 6)
Shark2 = Shark(0, False, 6)
Sharks = [Shark1, Shark2]

Goldfish1 = Goldfish(0, True, 6)
Goldfish2 = Goldfish(0, False, 6)
Goldfishs = [Goldfish1, Goldfish2]

Eagle1 = Eagle(0, True, 9)
Eagle2 = Eagle(0, False, 9)
Eagles = [Eagle1, Eagle2]

Parakeet1 = Parakeet(0, True, 9)
Parakeet2 = Parakeet(0, False, 9)
Parakeets = [Parakeet1, Parakeet2]

#take user input and run the program 
running = True
months = 0

while running:
    print("\nYou have been on the ark for", months, "months. Would you like to:")
    ui = input("1 - Let another month pass\n2 - Check inventory\n3 - Quit\n")
    print("\n")
    if ui == "1":
        months += 1
        for cat in Cats:
            cat.updateAge()
            cat.giveBirth()
        for dog in Dogs:
            dog.updateAge()
            dog.giveBirth()
        for shark in Sharks:
            shark.updateAge()
            shark.giveBirth()
        for goldfish in Goldfishs:
            goldfish.updateAge()
            goldfish.giveBirth()
        for eagle in Eagles:
            eagle.updateAge()
            eagle.giveBirth()
        for parakeet in Parakeets:
            parakeet.updateAge()
            parakeet.giveBirth()
    elif ui == "2":
        animalNumber = 1
        for i in Cats:
            print("Animal #", animalNumber, " ", i)
            animalNumber += 1
        for i in Dogs:
            print("Animal #", animalNumber, " ", i)
            animalNumber += 1
        for i in Sharks:
            print("Animal #", animalNumber, " ", i)
            animalNumber += 1
        for i in Goldfishs:
            print("Animal #", animalNumber, " ", i)
            animalNumber += 1
        for i in Eagles:
            print("Animal #", animalNumber, " ", i)
            animalNumber += 1
        for i in Parakeets:
            print("Animal #", animalNumber, " ", i)
            animalNumber += 1
    elif ui == "3":
        running = False
        
        