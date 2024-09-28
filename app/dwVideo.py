import yt_dlp
import streamlit as st


def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Descargando: {d['_percent_str']} - {d['_eta_str']} restantes")
    elif d['status'] == 'finished':
        print(f"\nDescarga completada: {d['filename']}")


def download_video(video_url, path="."):
    try:
        ydl_opts = {
            'format': 'bestaudio+bestvideo/best',
            'outtmpl': f'{path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'progress_hooks': [progress_hook],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            getPermissionToContinue(ydl, info_dict, video_url)

        print(f"Download video en {path}")
    except Exception as e:
        print(f"Error downloading: {e}")


def getPermissionToContinue(ydl, info_dict, video_url):
    video_title = info_dict.get('title', 'Título no disponible')
    st.write(f"**titulo:** {video_title}")
    if st.button("Download"):
        # Descarga la miniatura
        thumbnail_url = info_dict.get('thumbnail')
        if thumbnail_url:
            print("***************************************")
            print("***************************************")
            print("***************************************")
            print(f"Descargando miniatura: {thumbnail_url}")
            print("***************************************")
            print("***************************************")
            print("***************************************")
            ydl.download([thumbnail_url])
        else:
            print("***************************************")
            print("No se encontró una miniatura.")
        ydl.download([video_url])




if __name__ == "__main__":

    st.title("Descarga de videos de Youtube con Python")
    url = st.text_input("Ingrese la URL del video: ")

    if url:
        downloader = download_video(url, "static/videos")

    #url = "https://www.youtube.com/watch?v=8aJTBBva78U"
    #downloader = download_video(url, "D:/Documents/PruebasTecnicas/AppinIT/videoAppinIT/videos")