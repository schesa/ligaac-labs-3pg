from collections import Counter 


def count1(s = ''):
    """
        Return tuples of numbers and occurenses in string s 
        Ordered by least common

        Parameters
        ----------
        s : str, optional (default is '')
            Input string who's numbers to count 
    """
    words = s.split()
    words = [ x for x in words if x.isnumeric()]
    least_common = Counter(words).most_common()
    least_common.reverse()
    return least_common


if __name__ == "__main__":
    text = """ We are having 3 numbers of 5 pieces and each of them are having 3 stars. We also add an 1 to the end 
                of 5 to make 
                it equal with 7 or 3 """    

    help(count1)
    print(count1(text))