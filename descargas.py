from pytube import YouTube

url = input("Inserte la URL del video: ")
print()
yt = YouTube(url)
yt.title
yt.author
quality = input("HD 22(hd) or 18(low quality): ")
print()
print("Descargando....")
print()
yt.streams.get_by_itag(quality).download(r'C:\Users\Mike\Desktop\Graficacion')
print()
print("Su descarga se ha completado con exito :) ")
print()

