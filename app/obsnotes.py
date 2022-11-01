
def crear_nota(tuit):
    brain= '/home/ghost/mybrain/jcrespo/Twitter/'
    with open(brain+tuit._json['id_str']+'.md','w',newline='',encoding='utf-8') as f:
        f.write('---\n')
        f.write('Título: =='+tuit._json['id_str']+'==\n')
        f.write('tags: [\'#Obsidian\',\'#Notas\',\'#Twitter\']\n')
        f.write('aliases: []\n')
        f.write('---\n')
        link='https://twitter.com/user/status/'
        f.write('Link Referencia: '+link+tuit._json['id_str'])
        f.write('\n---\n')
        in_txt=tuit._json['display_text_range'][0]
        f.write('\n'+tuit._json['full_text'][in_txt:]+'\n')


if __name__ == '__main__':
#path del .env 
#p1 = '/home/ghost/rpibots/'
   crear_nota()