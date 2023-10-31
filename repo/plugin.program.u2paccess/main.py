import xbmc
import hashlib

# Installation de l'addon "script.module.pyxbmct"
if not xbmc.getCondVisibility('System.HasAddon(script.module.pyxbmct)'):
    xbmc.executebuiltin("InstallAddon(script.module.pyxbmct)")
    
    # Attendre jusqu'à ce que l'addon soit installé
    while not xbmc.getCondVisibility('System.HasAddon(script.module.pyxbmct)'):
        xbmc.sleep(5000)  # Attendre une seconde (ajustez au besoin)

# Le reste du script
import xbmcaddon
import xbmcvfs
import xbmcgui
import os
import shutil

def copy_directory_contents(source, destination):
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isdir(source_path):
            if not xbmcvfs.exists(destination_path):
                xbmcvfs.mkdirs(destination_path)
            copy_directory_contents(source_path, destination_path)
        else:
            xbmcvfs.copy(source_path, destination_path)

def check_and_copy_addon():
    addon_id = "plugin.video.sendtokodiU2P"
    repStart = xbmcvfs.translatePath("special://home/addons/" + addon_id + "/")

    if xbmc.getCondVisibility('System.HasAddon(' + addon_id + ')'):
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Addons.SetAddonEnabled", "params": { "addonid": "' + addon_id + '", "enabled": false }}')
    else:
        repFileStart = xbmcvfs.translatePath("special://home/addons/plugin.program.u2paccess/resources/" + addon_id + "/")

        if xbmcvfs.exists(repFileStart):
            xbmcvfs.mkdirs(repStart)
            copy_directory_contents(repFileStart, repStart)

        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Addons.SetAddonEnabled", "params": { "addonid": "' + addon_id + '", "enabled": true }}')

# Nombre maximum d'essais
max_attempts = 3

for attempt in range(max_attempts):
    # Demander le mot de passe à l'utilisateur
    password = xbmcgui.Dialog().input("Code installation U2Pplay :", type=xbmcgui.INPUT_NUMERIC, option=xbmcgui.ALPHANUM_HIDE_INPUT)

    if password is None or password == '':  # Si l'utilisateur annule la saisie ou laisse le champ vide
        break  # Sortir de la boucle si l'opération est annulée

    # Hacher le mot de passe saisi
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    # Vérifier le mot de passe haché (remplacez le hachage du mot de passe réel)
    if hashed_password == "bd27d7b3aee8f6ea296f3d29452b3fd181deb9326209fc4fd843bb69aa2aa389":
        # Mot de passe correct, exécuter le script
        check_and_copy_addon()
        
        # Le reste du code reste inchangé
    else:
        # Mot de passe incorrect, afficher un message d'erreur
        dialog = xbmcgui.Dialog()
        if attempt < max_attempts - 1:
            dialog.ok("Mot de passe incorrect", f"Il vous reste {max_attempts - attempt - 1} essai(s).")
        else:
            dialog.ok("Mot de passe incorrect", "Vous avez épuisé tous les essais.")