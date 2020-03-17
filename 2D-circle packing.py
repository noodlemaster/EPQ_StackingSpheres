import math
import os

print('Regular 2D packing')
print('Please enter three parameters of a cube:')
print('*Note: Width/diameter needs to be an integer and h >= d.*')
w=int(input('Width:'))
h=int(input('Height:'))
d=int(input('Diameter:'))


def hex(d,w,h):  #d=diameter. w=width, h=height, d|w

	if w <= 0 or h <= 0 or d <= 0:
		print('invalid parameters')
		return

	if w%d!=0:
		print('invalid parameters')
		return
	else:
		pass
	
	num_circles=[]

	a=w/d
	b=a-1
	c=math.sqrt(2*(d**2)-2*(d**2)*(math.cos(2*math.pi/3)))
	
	if h < d:
		print('invalid parameters')
		return


	if h - int(h/c)*c+d == 0:
		circles=(int(h/c)+1)*a + int(h/c)*b
		print(circles)
		return

	else:
		if h > int(h/c)*c+d:
			circles=(int(h/c)+1)*a + int(h/c)*b
			num_circles.append(circles)

			
		if h>int(h/c)*c and h < int(h/c)*c+d:
			circles=int(h/c)*a + (int(h/c)+1)*b
			num_circles.append(circles)


		if h>int(h/c)*c and h < int(h/c)*c+d and h >= (int(h/c)-1)*c+int((h-(int(h/c)-1)*c)/d)*d:
			circles=int(h/c)*a+(int(h/c)-1)*b
			num_circles.append(circles)


		if h - (int(h/c)-1)*c-d >= 2*d:
			circles=(int(h/c)+2)*a+(int(h/c)-1)*b
			num_circles.append(circles)
		

		if c > h:
			circles=a*int(h/d)
			num_circles.append(circles)


		if h > c and h < c+d :
			circles=a*int(h/d)
			num_circles.append(circles)

		#cub
		circles=int(h/d)*a

	print('Max.number of circles:', max(num_circles))

hex(d,w,h) #
os.system('pause')