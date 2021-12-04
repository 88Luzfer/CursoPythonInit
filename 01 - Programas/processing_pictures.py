import cv2

#Función para cargar la imagen png en la variable correspondiente.
im_g=cv2.imread("archivos/smallgray.png",0)
im_brg=cv2.imread("archivos/smallgray.png",1)
#Visualización de la carga de las imágenes en las variables (cuidado en la im_brg ya que la matriz se ve traspuesta)
print(im_g)
print(im_brg)
#Ahora para crear una imágen a partir de su matriz en escala de grises o brg utilizamos la siguiente función para crear el archivo
cv2.inwrite("archivos/newsmallgray.png",im_g)