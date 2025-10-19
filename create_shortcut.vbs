Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = oWS.SpecialFolders("Desktop") & "\LightMD.lnk"
Set oLink = oWS.CreateShortcut(sLinkFile)
oLink.TargetPath = WScript.ScriptFullName
oLink.Arguments = ""
oLink.WorkingDirectory = Left(WScript.ScriptFullName, InStrRev(WScript.ScriptFullName, "\") - 1)
oLink.TargetPath = oLink.WorkingDirectory & "\run_lightmd.bat"
oLink.IconLocation = "C:\Windows\System32\shell32.dll,70"
oLink.Description = "LightMD - Markdown Editor"
oLink.Save

WScript.Echo "Desktop shortcut created successfully!"
