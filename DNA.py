# define a class that holds DNA methods
class DNA:
    def __init__(self):
        #define an empty dictionary
        self.dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    #define a property function that asks for the string of DNA
    @property
    def string(self):
        string = input("Enter the DNA string: ")
        return string.upper()

    #define function that counts the number of each letter in self.string to the dictionary
    def counter(self):
        for letter in self.string:
            if letter in self.dict.keys():
                self.dict[letter] += 1
            else:
                return "This is not a DNA string"
        return self.dict

if __name__ == "__main__":
    # create a dna object
    dna_sample = DNA()

    #print the counter function
    print(dna_sample.counter())