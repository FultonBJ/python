import pprint
import keyboard
import rich
from rich import print as rprint


'''
rich provides support for IPython and Jupyter

inspect() function: lets you examine deeply nested data.

'''

superhero = {"person": {"name": "John Jones", "age":30,"address":{"street": "123 Main St", "city": "Gotham",
"state":"NY", "zip_code": "12345"},"superpowers":{"leaps_buildings":True,"factorizes_polynomials":False},"contacts":[{"type":"email","value":"john.jones@heroes.are.us"},
{"type":"phone","value":"555-123-4567"}],"hobbies": ["reading","hiking","coding","crimefighting"],
"family":{"spouse": {"name":"Griselda Jones", "age":28},"children":[{"name":"Bellatrix", "age":5, "name":"Draco", "age":8}
]}}}

from rich import inspect
'''The inspect() function is quite powerful. You can get a comprehensive 
description of its parameters by typing inspect(inspect) as suggested in 
the output above.

Python's inspect module is more complex but lacks syntax highlighting
https://docs.python.org/3/library/inspect.html#module-inspect
'''
# inspect(superhero, methods=True)
import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release()
cv2.destroyWindow("preview")
