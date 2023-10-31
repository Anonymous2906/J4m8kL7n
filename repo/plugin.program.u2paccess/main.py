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

# Demander à l'utilisateur s'il souhaite continuer
dialog = xbmcgui.Dialog()
is_continue = dialog.yesno("[COLOR red]!! ATTENTION !![/COLOR]", "Voulez devez être en possession du bon mot de passe pour poursuivre l'installation.\nEn cas de 3 mauavais mot de passe, l'addon se désintallera.\n\nVoulez-vous continuer ?")

if is_continue:
    # Nombre maximum d'essais
    max_attempts = 3

    for attempt in range(max_attempts):
        # Demander le mot de passe à l'utilisateur
        password = xbmcgui.Dialog().input("Code installation U2Pplay :", type=xbmcgui.INPUT_NUMERIC, option=xbmcgui.ALPHANUM_HIDE_INPUT)

        # Hacher le mot de passe saisi
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        # Vérifier le mot de passe haché (remplacez le hachage du mot de passe réel)
        if hashed_password == "bd27d7b3aee8f6ea296f3d29452b3fd181deb9326209fc4fd843bb69aa2aa389":
            # Mot de passe correct, exécuter le script
            check_and_copy_addon()
            
            # Chemin vers le fichier texte
            path = xbmcvfs.translatePath('special://home/addons/plugin.program.u2paccess/log_updates.txt')

            # Lecture du contenu du fichier avec l'encodage utf-8
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Création de la fenêtre Kodi pour afficher le contenu du fichier texte
            dialog = xbmcgui.Dialog()
            dialog.textviewer('[COLOR deepskyblue]U2PPlay[/COLOR] - Mises à jour', content)

            # Afficher une boîte de dialogue pour quitter Kodi
            is_quit = dialog.yesno("Installation Réussie", "Voulez-vous quitter Kodi ?")

            if is_quit:
                xbmc.executebuiltin("Quit()")
                break  # Sortir de la boucle en cas de succès
            else:
                # Désactiver puis réactiver l'addon
                xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Addons.SetAddonEnabled", "params": { "addonid": "plugin.video.sendtokodi", "enabled": false }}')
                xbmc.sleep(2000)
                xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Addons.SetAddonEnabled", "params": { "addonid": "plugin.video.sendtokodi", "enabled": true }}')
                # Afficher une notification
                xbmc.executebuiltin('Notification("U2Pplay", "L\'addon a été mis à jour avec succès.")')
                break  # Sortir de la boucle en cas de succès
        else:
            # Mot de passe incorrect, afficher un message d'erreur
            dialog = xbmcgui.Dialog()
            if attempt < max_attempts - 1:
                dialog.ok("Mot de passe incorrect", f"Il vous reste {max_attempts - attempt - 1} essai(s).")
            else:
                dialog.ok("Mot de passe incorrect", "Vous avez épuisé tous les essais.")
else:
    # Sortir du script si l'utilisateur annule l'opération
    pass  # Vous n'avez pas besoin d'exécuter de code ici