# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
- MObject is a concrete class because it isn't marked explicitly abstract and there are no indications like 'abc' module.

2. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
- Since the method is commented out there is no code that is executable by the program. The __del__ is a method known as the "destructor" and it is automatically called when an object is about to be destroyed, usually when there are no more references to the object. It can be used to perform cleanup operations before the object is removed from memory. 

3. What class does Texture inherit from?
- The Texture class inherits from the Image class

4. What methods and attributes does the Texture class inherit from 'Image'? 
- It inherits all the methods and attributes from Image such as constructor __init__, as well as all the methods like getWidth, getHeight, getPixelColorR, getPixels, and setPixelsToRandomValue. It also inherits the attributes m_width, m_height, m_colorChannels, and m_Pixels. 

5. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
- I feel that Texture should have a 'has-a' relationship with Image because that implies that Texture contains Image as one of its components or an interface it can build off on and that kind of aligns with real world examples of textures in computer graphics. Texture not only has properties inherited from Image but also its own additional components that make it distinct. By using composition, we can encapsulate the Image object within the Texture class and provide access to its methods and attributes when needed. This allows us to extend the Texture class with its own unique methods and properties without the constraints and complexities that come with inheritance.
Refactoring code: 
import random

class MObject:
    def __init__(self):
        pass

class Image:
    def __init__(self, w, h):
        print("Constructor called")
        self.m_width = w
        self.m_height = h
        self.m_colorChannels = 3  # Assume we support RGB channels only.
        self.m_Pixels = [random.randint(0, 255) for _ in range(w * h * self.m_colorChannels)]

    def getWidth(self):
        return self.m_width

    def getHeight(self):
        return self.m_height

    def getPixelColorR(self, x, y):
        return self.m_Pixels[self.m_width * self.m_colorChannels * y + x]

    def getPixels(self):
        return self.m_Pixels

    def setPixelsToRandomValue(self):
        value = random.randint(0, 255)
        self.m_Pixels = [value] * (self.m_width * self.m_height * self.m_colorChannels)

class Texture:
    def __init__(self, image):
        self.image = image

    def getWidth(self):
        return self.image.getWidth()

    def getHeight(self):
        return self.image.getHeight()

    def getPixelColorR(self, x, y):
        return self.image.getPixelColorR(x, y)

    def getPixels(self):
        return self.image.getPixels()

    def setPixelsToRandomValue(self):
        self.image.setPixelsToRandomValue()

def main():
    random.seed()

    # Create a first image
    image1 = Image(100, 200)
    # Create a second image
    image2 = Image(image1.getWidth(), image1.getHeight())

    # Create a texture with image1
    texture = Texture(image1)

    print(f"image1: {image1.getWidth()}, {image1.getHeight()}")
    print(f"image1 red color at (0, 0): {image1.getPixelColorR(0, 0)}")
    print(f"image2: {image2.getWidth()}, {image2.getHeight()}")
    print(f"image2 red color at (0, 0): {image2.getPixelColorR(0, 0)}")

    # Accessing image properties through the texture
    print(f"Texture width: {texture.getWidth()}")
    print(f"Texture height: {texture.getHeight()}")
    print(f"Texture red color at (0, 0): {texture.getPixelColorR(0, 0)}")

if __name__ == "__main__":
    main()


6. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
- In Python, if we don't declare a constructor for a class, Python will automatically create a default constructor for us. This doesn't do anything other than initialize the object. In the case of the Texture class, it inherits the constructor from the Image class, so we can create instances of Texture without explicitly defining a constructor for it. 

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?
Singletons in Python are not thread safe by default but it depends on implementation. Since most singleton implementations create the instance is only when it is first requested, so in a multi-threaded environment, multiple threads can simultaneously request the instance and potentially create multiple instances if not properly synchronized.
Race conditions can also occur when multiple threads access and modify shared resources like the singleton instance simultaneously. This can lead to unexpected behavior.  
