Local $pathToPython = @ScriptDir & "\Python\python.exe"
Local $pathToTeuton = @ScriptDir & "\teuton\teuton.py"

Local $message = "Teuton Ausführen"
Local $var = FileOpenDialog($message, @ScriptDir & "\", "Teuton (*.teu)", 1)

If @error Then
   MsgBox(4096, "", "Keine Datei ausgewählt.")
Else
   runTeuton($var)
EndIf


Func runTeuton($pathToTeutonScript)
   $keys = $pathToPython & " " & $pathToTeuton & " " & $pathToTeutonScript
   BlockInput(1)
   ShellExecute("cmd.exe")
   Sleep(1000)
   Send($keys)
   Send("{ENTER}")
   BlockInput(0)
EndFunc