'''
Abstraction in Python
Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of the function, but inner working is hidden. User is familiar with that "what function does" but they don't know "how it does."

In simple words, we all use the smartphone and very much familiar with its functions such as camera, voice-recorder, call-dialing, etc., but we don't know how these operations are happening in the background. Let's take another example - When we use the TV remote to increase the volume. We don't know how pressing a key increases the volume of the TV. We only know to press the "+" button to increase the volume.

That is exactly the abstraction that works in the object-oriented concept.

Why Abstraction is Important?
In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity. It also enhances the application efficiency. Next, we will learn how we can achieve abstraction using the Python program.

'''

'''
** Abstraction vs Encapsulation :-
----------------------------------
Data Abstraction :-  
- Abstraction is the method of hiding the unwanted information.
- We can implement abstraction using abstract class and interfaces.
- In abstraction, implementation complexities are hidden using abstract classes and interfaces.
- The objects that help to perform abstraction are encapsulated.
- Abstraction provides access to specific part of data.

Data Encapsulation:-
- Whereas encapsulation is a method to hide the data in a single entity or unit along with a method to protect information from outside.
- Whereas encapsulation can be implemented using by access modifier i.e. private, protected and public.
- While in encapsulation, the data is hidden using methods of getters and setters.

'''

# Data Abstraction for class attribute 
class Ecpl:
    name="Debabrata"
    __emp_id="9559"
    
    def __fun__(self):
        print("Name : ", self.name )
        print("Emp_Id :", self.__emp_id)



obj=Ecpl()
obj.name="Asish Mani"
obj.__emp_id="2299"
obj.__fun__()


