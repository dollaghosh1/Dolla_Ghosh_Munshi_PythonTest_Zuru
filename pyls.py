import sys
import json
from datetime import datetime

#print(sys.argv)

f = open("structure.json", "r")
json_data = f.read()
data = json.loads(json_data)
split_val = sys.argv[4:]

if '-A' in sys.argv: #Subtask 2: ls -A (2 points)
    list_name = []
    for each in data['contents']:
        y=each.get('name')
        list_name.append(each.get('name'))
    print(list_name)
elif '-l' in sys.argv and '-r' in sys.argv and '-t' in sys.argv:#Subtask 6: ls -l -r -t --filter=<option> (5 points)
    filter=[i.split('=', 1)[1] for i in sys.argv[4:]]
    if(len(filter) != 0):
        if '--filter=dir' in sys.argv:
            result6 = data['contents']
            dir=[]
            
            for each in result6:
                    # print(x)
                    size_value=each.get('size')
                    if size_value>=4096:
                            dir.append(each)
                            for y in dir:
                                    y=each.get('name')
                                    if not y.startswith("."):
                                            name=each.get('name')
                                            size=each.get('size')
                                            time_modified=each.get('time_modified')
                                            date_val = datetime.fromtimestamp(time_modified)
                                            date_val_format =date_val.strftime("%b %d %H:%M")
                                            permissions=each.get('permissions')
                                            print(permissions,size,date_val_format,name)
                                            break     
        elif '--filter=file' in sys.argv:
            result6 = data['contents']
            file=[]
            
            for each in result6:
                    # print(x)
                    size_value=each.get('size')
                    if size_value<4096:
                            file.append(each)
                            for y in file:
                                    y=each.get('name')
                                    if not y.startswith("."):
                                            name=each.get('name')
                                            size=each.get('size')
                                            time_modified=each.get('time_modified')
                                            date_val = datetime.fromtimestamp(time_modified)
                                            date_val_format =date_val.strftime("%b %d %H:%M")
                                            permissions=each.get('permissions')
                                            print(permissions,size,date_val_format,name)
                                            break    
        else:
            print(filter,"is not a valid filter criteria. Available filters are 'dir' and 'file'")

    else:#Subtask 5: ls -l -r -t (5 points)
        result5 = data['contents']
        sorted_data = sorted(result5, key=lambda x: x['time_modified'])
        sorted_json = json.dumps(sorted_data)
        for each in sorted_data:
            y=each.get('name')
            if not y.startswith("."):
                name=each.get('name')
                size=each.get('size')
                time_modified=each.get('time_modified')
                date_val = datetime.fromtimestamp(time_modified)
                date_val_format =date_val.strftime("%b %d %H:%M")
                permissions=each.get('permissions')
                print(permissions,size,date_val_format,name)

elif '-l' in sys.argv and '-r' in sys.argv:#Subtask 4: ls -l -r (3 points)
    result4 = data['contents']
    for each in reversed(result4):
        #print(each)
        y=each.get('name')
        if not y.startswith("."):
            name=each.get('name')
            size=each.get('size')
            time_modified=each.get('time_modified')
            date_val = datetime.fromtimestamp(time_modified)
            date_val_format =date_val.strftime("%b %d %H:%M")
            permissions=each.get('permissions')
            print(permissions,size,date_val_format,name)
elif '-l' in sys.argv and 'parser' in sys.argv:#Subtask 8: ls -h (5 points)
    result8=data['contents'][7]['contents']
    for each in result8:
        size_value=each.get('size')
        B =  float(size_value)
        KB = float(1024)
        MB = float(KB ** 2) # 1,048,576
        GB = float(KB ** 3) # 1,073,741,824
        TB = float(KB ** 4) # 1,099,511,627,776
        if B < KB:
            size_value='{0} {1}'.format(B,'Byte' if 0 == B > 1 else 'Bytes')
        elif KB <= B < MB:
            size_value='{0:.1f} KB'.format(B / KB)
        elif MB <= B < GB:
            size_value='{0:.1f} MB'.format(B / MB)
        elif GB <= B < TB:
            size_value='{0:.1f} GB'.format(B / GB)
        elif TB <= B:
            size_value='{0:.1f} TB'.format(B / TB)
        name=each.get('name')
        time_modified=each.get('time_modified')
        date_val = datetime.fromtimestamp(time_modified)
        date_val_format =date_val.strftime("%b %d %H:%M")
        permissions=each.get('permissions')
        print(permissions,size_value,date_val_format,name)    
elif '-l' in sys.argv:#Subtask 3: ls -l (10 points)
    for each in data['contents']:
        y=each.get('name')
        if not y.startswith("."):
            name=each.get('name')
            size=each.get('size')
            time_modified=each.get('time_modified')
            date_val = datetime.fromtimestamp(time_modified)
            date_val_format =date_val.strftime("%b %d %H:%M")
            permissions=each.get('permissions')
            print(permissions,size,date_val_format,name) 
elif '--help' in sys.argv:#Subtask 3: ls -l (10 points)
    help_message = "This python program has been executed by reading a json file (which contains the information of a directory in nested structure). The content of this program has been printed in the console in the style of ls (linux utility).\n\nThe commands which have been used to execute the program are listed below:"
    description_command_message="\n\nsys.argv - The sys module provides functions and variables used to manipulate different parts of the Python runtime environment.\n\nopen()- The open() function opens a file, and returns it as a file object.\n\nf.read() -The read() method returns the specified number of bytes from the file.\n\njson.loads() - The json. loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.\n\nappend() - The append() method appends an element to the end of the list.\n\nsplit() - The split() method splits a string into a list.\n\nlen() - When the object is a string, the len() function returns the number of characters in the string.\n\ndatetime() - The datetime module has many methods to return information about the date object.\n\nfromtimestamp() - The fromtimestamp() function of the Python datetime.date class is useful for converting a timestamp into a date object.\n\nstrftime()- The strftime() method returns a string representing date and time using date, time or datetime object.\n\nsorted() - The sorted() function returns a sorted list of the specified iterable object.\n\njson.dumps() - json.dumps() function will convert a subset of Python objects into a json string.\n\nlambda - A lambda function can take any number of arguments, but can only have one expression.\n\nreversed() - Python reversed() method returns an iterator that accesses the given sequence in the reverse order.\n\nfloat()- The float() function converts the specified value into a floating point number."
    print(help_message,description_command_message)  

else: #Subtask 1: ls (10 points)
    list_name = []
    for each in data['contents']:
        y=each.get('name')
        if not y.startswith("."):
            list_name.append(each.get('name'))
    print(list_name)


