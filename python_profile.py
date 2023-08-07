import cProfile, pstats, io
from pstats import SortKey
import os
""" Code example: 
    from profileit import profileit    
    from pstats import SortKey
    #for more informations about keys see on sort_stats topic:
    # https://docs.python.org/3/library/profile.html
    sort_key=SortKey.NFL  
    file_path="/mnt/c/workspace" # path to save the stats file 
    @profileit(path=file_path,sort_key=sort_key)
    def func():
        a=1
        b=2
        c=a+b
        return c
    func()
    """

def profileit(path,sort_key):            
    def inner(func):
        def wrapper(*args, **kwargs):
            file_path=path
            sortby = sort_key
            file_name = func.__name__ + ".profile.txt" # Name the data file sensibly     
            pr= cProfile.Profile()
            retval = pr.runcall(func, *args, **kwargs)        
            s = io.StringIO()                            
            ps = pstats.Stats(pr,stream=s).sort_stats(sortby).strip_dirs()
            ps.print_stats()            
            with open(os.path.join(file_path,file_name), "w") as f:   
                f.write(s.getvalue())
            return retval
        return wrapper
    return inner