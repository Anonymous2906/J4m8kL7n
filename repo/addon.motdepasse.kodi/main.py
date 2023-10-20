import xbmcgui

# Récupérer le mot de passe stocké dans votre référentiel
# Vous pouvez le stocker dans le fichier "addon.xml" de votre référentiel
repository_password = "0000"

# Demander à l'utilisateur de saisir un mot de passe
kb = xbmcgui.Keyboard("", "Saisissez le mot de passe", False)
kb.doModal()
entered_password = kb.getText()

# Comparer le mot de passe entré par l'utilisateur avec celui du référentiel
if entered_password == repository_password:
    xbmcgui.Dialog().ok("Accès autorisé", "Le mot de passe est correct.")
    xbmc.executebuiltin('ActivateWindow(videos,addons://sources/repository.repo.J4m8kL7n/)')  # Ouvrir le référentiel
else:
    xbmcgui.Dialog().ok("Accès refusé", "Le mot de passe est incorrect. Accès refusé.")
