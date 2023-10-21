import xbmc
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
        repFileStart = xbmcvfs.translatePath("special://home/addons/addon.motdepasse.kodi/resources/" + addon_id + "/")

        if xbmcvfs.exists(repFileStart):
            xbmcvfs.mkdirs(repStart)
            copy_directory_contents(repFileStart, repStart)
        
        xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Addons.SetAddonEnabled", "params": { "addonid": "' + addon_id + '", "enabled": true }}')

# Demander le mot de passe à l'utilisateur
password = xbmcgui.Dialog().input("Mot de passe", type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)

# Vérifier le mot de passe (changez "votre_mot_de_passe" par le mot de passe réel)
if password == "0000":
    # Mot de passe correct, exécuter le script
    check_and_copy_addon()
    
    # Afficher une boîte de dialogue pour quitter Kodi
    dialog = xbmcgui.Dialog()
    dialog.ok("Installation Réussie", "Cliquez sur OK pour quitter Kodi")
    
    # Quitter Kodi
    xbmc.executebuiltin("Quit()")
else:
    # Mot de passe incorrect, afficher un message d'erreur
    dialog = xbmcgui.Dialog()
    dialog.ok("Mot de passe incorrect", "Le mot de passe que vous avez saisi est incorrect.")
