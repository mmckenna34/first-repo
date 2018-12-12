from math import sqrt
2	
3	print('Pythagorean theorem calculator! Calculate your triangle sides.')
4	print('Assume the sides are a, b, c and c is the hypotenuse (the side opposite the right angle')
5	formula = input('Which side (a, b, c) do you wish to calculate? side> ')
6	
7	if formula == 'c':
8	    side_a = int(input('Input the length of side a: '))
9	    side_b = int(input('Input the length of side b: '))
10	
11	    side_c = sqrt(side_a * side_a + side_b * side_b)
12	    
13	    print('The length of side c is: ' )
14	    print(side_c)
15	
16	elif formula == 'a':
17	    side_b = int(input('Input the length of side b: '))
18	    side_c = int(input('Input the length of side c: '))
19	    
20	    side_a = sqrt((side_c * side_c) - (side_b * side_b))
21	    
22	    print('The length of side a is' )
23	    print(side_a)
24	
25	elif formula == 'b':
26	    side_a = int(input('Input the length of side a: '))
27	    side_b = int(input('Input the length of side c: '))
28	        
29	    side_c = sqrt(side_c * side_c - side_a * side_a)
30	    
31	    print('The length of side b is')
32	    print(side_c)
33	
34	else:
