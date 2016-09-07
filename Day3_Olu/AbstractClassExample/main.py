#abstract keyword is not supported in python hence the reason we use this trick

#I want the sub class of animal (i.e. Dog and cat) to create its own speak method or get an error if not created

import animal, dog, cat

# anim = animal.Animal()
#above throws an error to show that abstract class cannot be instantiated

#create an instance of dog
dg = dog.Dog("Bingo")

#call the speak method
dg.speak()

print()

#create an instance of cat
ct = cat.Cat("Whiskey")

#call the speak method
ct.speak()