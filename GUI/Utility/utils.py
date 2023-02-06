class Utility:
    """
    Class for exporting general utility methods.
    """
    
    @staticmethod
    def flatten(arr:list):
        arr = [i for j in arr for i in j]
        return arr    
    
