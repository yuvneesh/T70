from bs4 import BeautifulSoup


""" loop to load xml file and parse it"""
with open("samples.txt") as f:
    soup = BeautifulSoup(f, "lxml-xml")
    #print(soup.prettify())

    """ Understanding tags and values
    # any tag can be directly accessed by soup.find(_tag_name_) or soup.find_all(_tag_name_)
    for ID in soup.find_all('id1'):

        # each tag is a bs4.element.tag object
        #print("type of 'id1' is: ",type(ID))
        
        
        # the value stored in a tag can be accessed using the _tag_.string method
        # although it is possible to have tags like: <something a1="val1" a2="val2">,
        # where a1 and a2 are attributes, T70 tags do not have any atrributes
        

        #print(ID.string)
        #print(type(ID.string))

        # to extract  the 'tag.string', use str(tag.string) to remove references to the bs4 object

        #print(str(ID.string))

        print('===========================')
    """

    """ An example of extracting what is required. 
    summary = {}

    for sample in soup.find_all("sample"):
        _id = str(sample.id1.string)
        _size = str(sample.size.string)
        _result = str(sample.result.result_value.string)

        summary[_id] = {"size": _size, "result": _result}

    print(summary)
    """

""" A class to hold data for one sample
class Sample:

    def __init__(self, sample_id, sample_size, start_time, result):
        self.ID = sample_id
        self.SIZE = sample_size
        self.time = start_time
        self.TAN = result

Note: As classes are required to add data to the database, it is probably unncessary to create a class here
"""

def read_data(raw: str) -> dict:
    soup = BeautifulSoup(raw, "lxml-xml")

    summary = {}

    for sample in soup.find_all("sample"):
        _id = str(sample.id1.string)
        _size = str(sample.size.string)
        _result = str(sample.result.result_value.string)

        summary[_id] = {"size": _size, "result": _result}

    return summary