import data

#importing the main file

x=data.DataStore()

x.create('Ankit','33',8)
#to create a key with key_name,value given and with no time-to-live property
x.create('raj','66',5)
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)
x.read('Ankit')
#it returns the value of the respective key in Jsonobject
x.read("singh")
#it returns the value of the respective key in Jsonobject
x.read('raj')
#it returns the value of the respective key in Jsonobject
x.create("Ankit",'22')
#it returns an ERROR since the key_name already exists in the database
x.delete("Ankit")
#it will delete the key and value in Json object
