import math
import os

print('-----Regular sphere 3D packing-----')
print('Please enter three parameters of a cubic:')
print('*Note: Length/diameter needs to be an integer and h >= d.*')
l=int(input('Length:'))
w=int(input('Width:'))
h=int(input('Height:'))
d=int(input('Diameter:'))


def hex(d,l,w,h):  

	if w <= 0 or h <= 0 or d <= 0 or l <= 0:
		print('invalid parameters')
		return

	if l%d!=0:
		print('invalid parameters')
		return
	else:
		pass
	
	num_circles=[]
	num_spheres=[]
	k=[]

	a=l/d
	b=a-1
	c=math.sqrt(2*(d**2)-2*(d**2)*(math.cos(2*math.pi/3)))
	
	if w < d:
		print('invalid parameters')
		return


	if w - int(w/c)*c+d == 0:
		circles=(int(w/c)+1)*a + int(w/c)*b
		num_circles.append(circles)
		row_a=int(w/c)+1
		row_b=int(w/c)
		k.append(min(row_a,row_b))

	if w > int(w/c)*c+d:
		circles=(int(w/c)+1)*a + int(w/c)*b
		num_circles.append(circles)
		row_a=int(w/c)+1
		row_b=int(w/c)
		k.append(min(row_a,row_b))

	if w>int(w/c)*c and w < int(w/c)*c+d:
		circles=int(w/c)*a + (int(w/c)+1)*b
		num_circles.append(circles)
		row_a=int(w/c)
		row_b=int(w/c)+1
		k.append(min(row_a,row_b))

	if w>int(w/c)*c and w < int(w/c)*c+d and w >= (int(w/c)-1)*c+int((w-(int(w/c)-1)*c)/d)*d:
		circles=int(w/c)*a+(int(w/c)-1)*b
		num_circles.append(circles)
		row_a=int(w/c)
		row_b=int(w/c)-1
		k.append(min(row_a,row_b))

	if w - (int(w/c)-1)*c-d >= 2*d:
		circles=(int(w/c)+2)*a+(int(w/c)-1)*b
		num_circles.append(circles)
		row_a=int(w/c)+2
		row_b=int(w/c)-1
		k.append(min(row_a,row_b))

	if c > w:
		print('Maximum number of spheres:',a*int(w/d)*int(h/d))
		return
	
	if w > c and w < c+d :
		print('Maximum number of spheres:',a*int(w/d)*int(h/d))
		return

	layer_a=max(num_circles)
	num_b=[]
	num_c=[]

	for i in range (0,len(k)):
		num_b.append(k[i]*((2*l/d)-3))
		num_c.append((k[i]-1)*((2*l/d)-5))
	
	layer_b=max(num_b)
	layer_c=max(num_c)

	n=int(h/((math.sqrt(2)+1)*d))
	g=h-n*(math.sqrt(2)+1)*d
	u=((math.sqrt(2)+1)/2)*d

	if int(g/u)==0:
		spheres=(layer_a+layer_b+layer_c)*n	
		num_spheres.append(spheres)

	if int(g/u)==1:
		spheres=(layer_a+layer_b+layer_c)*n+layer_a	
		num_spheres.append(spheres)

	if int(g/u)==0:
		spheres=(layer_a+layer_b+layer_c)*n+layer_a+layer_b
		num_spheres.append(spheres)

	print('Maximum number of spheres:',max(num_spheres))

hex(d,l,w,h) 
os.system('pause')