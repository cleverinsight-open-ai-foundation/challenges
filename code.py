"""
Load module to filter data on fly
"""
import pandas as pd
class Load():
    """
    Load class is used for exclusive dataframe filtering
    which takes `df` a csv file and convert into dataframe
    """
    def __init__(self, filename):
        self.version = open('VERSION').readlines()[0]
        self.df = pd.read_csv(filename)
        self.data = """W_A11,2000-02,Moving average,59.66666667,50.92582302,
                        68.40751031,Injuries,Number,Assault,Validated,Whole 
                        pop,All ages,FatalW_A11,2001-03,Moving average,60,10,
                        20,30,33,31,12,51.23477459,68.76522541,Injuries,
                        Number,Assault,Validated,Whole pop,All ages,Fatale
                        50, 50, 60,pop,All ages,Fatal"""


    def get_version(self):
        """ Get current `version` of library"""
        return self.version


    def pick_numbers(self):
        """

        From self.data extract all numbers as a list
        :eg:
            data = "W_A11,2000-02,Moving average,59.66666667,50.92582302,68.40751031,
                       Injuries,Number,Assault,Validated,Whole pop,All ages,Fatal"

        :returns: [59.66666667,50.92582302,68.40751031]

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.pick_numbers()
            >> [1,2,3,4,5,6]

        """
        res = []
        for t in self.data.split(","):
            try:
                res.append(float(t))
            except ValueError:
                pass
        return res


    def sum_all_numbers(self):
        """
        From `self.data` extract all numbers and return the sum of all numbers

        :eg:
            data = "W_A11,2000-02,Moving average,59.66666667,50.92582302,68.40751031,
                       Injuries,Number,Assault,Validated,Whole pop,All ages,Fatal"
        :returns 179.0

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.sum_all_numbers()
            >> 179.0


        """

        print(sum(df.pick_numbers()))

    def extract_vowels(self):
        """
        Return all vowels in the given string `self.data`

        :returns [] all vowels as list

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.extract_vowels()
            >> ['A', 'E', 'I', 'O']
        """
        def Check_Vow(data, vowels):
            final = [each for each in data if each in vowels]
            print(final)
        vowels = "AeEeIiOoUu"
        Check_Vow(self.data, vowels)

    def pick_odd_numbers(self):
        """
        Take the string from `self.data` and extract all odd numbers and return
        list of all odd numbers from the string

        :returns: [1, 3, 5]

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.pick_odd_numbers()
            >> [1, 3, 5]

        """
        for num in df.pick_numbers():
            if round(num) % 2 != 0:
                print(num)

    def get_mean(self):
        """
        Take the string from `self.data` and extract all numbers and return
        the mean of extracted list of numbers.

        :returns: 50

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.get_mean()
            >> 50
        """
        res = df.pick_numbers()
        print(sum(res)/len(res))


    def get_all_categorical(self):
        """
        Take the pandas dataframe from `self.df` and return all
        the columns which are categorical variables

        :returns:   All categorical.
        :rtype:     List

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.get_all_categorical()
            >> ['Series_reference', 'Type']
        """
        cols = self.df.columns
        num_cols = self.df._get_numeric_data().columns
        print(list(set(cols) - set(num_cols)))


    def get_all_continuous(self):
        """
        Take the pandas dataframe from `self.df` and return all
        the columns which contain categorical variables

        :returns:   All continuous.
        :rtype:    List

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.get_all_continuous()
            >> ['Lower_CI', 'Upper_CI', 'Units']
        """
        print(self.df._get_numeric_data().columns)



    def addition(self, x, y):
        """
        Take X and Y as input and now return the sum of both

        :param      x:    { parameter_description }
        :type       x:    { type_description }
        :param      y:    { parameter_description }
        :type       y:    { type_description }

        Usage:
        ======
            >> df = Load('data.csv')
            >> df.addition(10, 20)
            >> 30
        """
        print(x+y)



if __name__ == '__main__':
    # instantiate the object
    df = Load('data.csv')
    df.sum_all_numbers()
    df.get_mean()
    df.extract_vowels()
    df.pick_odd_numbers()
    df.get_all_categorical()
    df.get_all_continuous()
    df.addition(10, 20)
