'''when ever the setup.py runs
 and find_packages runs then it will go find 
in how many folders we hace __init__.py it will
directly considers this suource(src) as 
package itself and then it tried to build this, 
then after building we can inport this where 
ever we want like how we import seaborn,pandas,numpy etc...
(for that we need to put this in PyPI package) 
in our case we are using this src & __init__ because 
we just want to build this at package itself '''


# entire project developemt will be happeing in this particular folder src
