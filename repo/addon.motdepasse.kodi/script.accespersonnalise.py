import xbmcaddon
import xbmc

def open_custom_access_addon():
    # Insérer ici la logique de votre addon d'accès personnalisé
    # Par exemple, lancer l'addon ouvrir l'interface de saisie du mot de passe
    xbmc.executebuiltin('RunScript(script.addon.motdepasse.kodi)')

# Appeler la fonction lorsque l'utilisateur clique sur le référentiel
xbmc.executebuiltin('RunScript(script.accespersonnalise.open_custom_access_addon)')