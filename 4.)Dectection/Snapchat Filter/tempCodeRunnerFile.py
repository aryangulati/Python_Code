	for j in range(specs2.shape[1]):
					if (specs2[i,j,3]>0):
						img[ye+i,xe+j,:]=specs2[i,j,:-1]