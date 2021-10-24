x=['5-Nov-18','25-Mar-17','1-Nov-18','7-Mar-17']
from datetime import datetime
x.sort(key=lambda d:datetime.strptime(d,"%d-%b-%y"))
print(x)
