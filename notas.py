from app.twlogin import login
from app.obsnotes import crear_nota
import numpy as np
import os, tweepy

#Twitter tiene el límite de recuperar hasta 3200 tuits de un timeline.
#La primera vez que corre el script hace una busqueda completa y se
#crea un log con el id del último tuit con los que creó notas.
#Para que las recuperaciones sean desde ese último tuit.

#revisamos si existe el log

if(os.path.exists('log_notes.npy')):
	aux         = np.load('app/log_notes.npy', allow_pickle='TRUE') 
	last_tuit  = aux
else:
    aux = 0
    np.save('app/log_notes.npy',aux)

api = login(path='/home/ghost/rpibots/')

historial = []
target = 'jpcr3spo'


if not aux:
    for status in tweepy.Cursor(api.user_timeline,screen_name=target,tweet_mode="extended",count=100).items():
        historial.append(status)
else:
    for status in api.user_timeline(screen_name=target,since_id=aux,tweet_mode="extended"):
        historial.append(status)


for tuit in historial:
    in_txt=tuit._json['display_text_range'][0]
    if tuit._json['full_text'][in_txt:in_txt+2]=='n!':
        crear_nota(tuit)
        aux = tuit._json['id']
        np.save('app/log_notes.npy',aux)

