# **Obsidian Notes con Twitter**

## Descripción

Obsidian es un gestor de conocimiento usado para construir un cerebro digital. 
Twitter es una red social donde se comparte variada e interesante información de toda índole en un formato corto de 280 caracteres por post.

Este proyecto busca crear notas cortas a partir de re tuits con un comando y hacerlas disponibles en el cerebro digital automáticamente. Estas entradas rápidas se pueden crear desde la app de twitter del celular y ser analizadas en el ordenador directamente con [[Obsidian]].

## ¿Cómo funciona?

Es un bot que constantemente monitorea en Twitter buscando re tuits del mi usuario @jpcr3spo que empiezan con el texto '!n'. Este comando le indica que tuits se quieren convertir en notas.

Contiene las siguientes partes:
- Usar el API de Twitter para automatizar búsquedas.
- Crear archivos y subirlos a un repositorio con Git. Obsidian tiene un plugin 'Obsidian-git' que sincroniza el repositorio en los dispositivos donde este el cerebro digital automáticamente.
- Usar un Raspberry para correr el bot que crea notas. 

## Instalación

Para desplegar el proyecto se necesitan algunos pre requisitos:
	- Tokens de acceso al API de Twitter.
	- Raspberry Pi4 con un sistema Raspbian previamente configurado.

Al clonar el repositorio, el archivo `req.txt` contiene todos los paquetes que necesitamos en [[Python]]. Usamos [[pip]] para instalarlos en un entorno virtual.
``` shell %lenguaje
python -m venv rpibots && cd rpibots
source bin/activate
git clone
cd obsidian-notes/
pip install -r req.txt
python obs_notes.py
```

Luego de correr el script 'obs_notes.py' se crean notas en la dirección del Brain antes declarado (en el mismo script).
Por lo que se debe dar permisos para ejecutar el archivo `obs_git.sh` para sincronizar el repositorio con las notas creadas.

Para automatizar los scripts configuramos el archivo `crontab` para que se creen notas buscando nuevos re tuits con el comando 'n!' cada 15 min y que sincronice el cerebro en Obsidian cada hora.

