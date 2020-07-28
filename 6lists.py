spam = ['cat', 'dog', 'snake', 'cow']
spam[1] #call a value from a list

spam = [[10, 20, 50, 100], ['parrot', 'zebra', 'elephant']]
spam[1][2] #call a value from a list inside the spam list
spam[-1] #negative indeces refer to the values of the list starting from the end

del spam[0][1] 

#list concactenation, multiplication  and list()
[1, 2, 3] + [4, 5, 6]
[1, 2, 3] * 3
list('Hello')

'yes' in ['yes', 'no', 'maybe', 'not really']
#True

'yes' not in ['yes', 'no', 'maybe', 'not really']
#False