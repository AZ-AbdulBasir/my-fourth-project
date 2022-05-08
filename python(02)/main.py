s = 'abc<def*gh?ikl'
s.translate(None, '\/:*?"<>|')
'abcdefghikl'


#2
s = 'I mainly play footbal'
s = 'Clearly, he has no excuse for such behavior'
print(sorted(list(filter(lambda x: x.count('а') >= 2, s.split()))))


#3
my_st = "PythonTutorialAndExercises"
my_st = "ITAcademy"
print(my_st.split())



#4
string_value = "**//Python Exercises// - 12."
s = ''.join(ch for ch in string_value if ch.isalnum())
print(s)