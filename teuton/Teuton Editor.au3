#NoTrayIcon
#include <GUIConstants.au3>

#Region ### START Koda GUI section ### Form=g:\teuton4win\teuton editor.kxf
$Form1 = GUICreate("Teuton Editor", 633, 447, 194, 124)
$Edit1 = GUICtrlCreateEdit("", 8, 64, 609, 369)
GUICtrlSetData(-1, StringFormat("fuer i im bereich(10):\r\n    drucke "&Chr(34)&"Hallo Welt"&Chr(34)&""))
GUICtrlSetFont(-1, 10, 800, 0, "System")
GUICtrlSetColor(-1, 0x0000FF)
$Button1 = GUICtrlCreateButton("Ausführen", 8, 16, 75, 25, 0)
$Button2 = GUICtrlCreateButton("Öffnen", 112, 16, 75, 25, 0)
$Button3 = GUICtrlCreateButton("Speichern", 200, 16, 75, 25, 0)
$Label1 = GUICtrlCreateLabel("Entwickler: Philipp Mayr", 496, 16, 116, 17)
$Button4 = GUICtrlCreateButton("Neu", 288, 16, 75, 25, 0)
GUISetState(@SW_SHOW)
#EndRegion ### END Koda GUI section ###


Global $pathToTeutonScript = ""


While 1
	$nMsg = GUIGetMsg()
	Switch $nMsg
		Case $GUI_EVENT_CLOSE
			Exit
		 case $Button1
			runTeu()
		 case $Button2
			open()
		 case $Button3
			save()
		 case $Button4
			new()
	EndSwitch
WEnd


Func open()
   Local $message = "Teuton Öffnen"
   Local $path = FileOpenDialog($message, @ScriptDir & "\", "Teuton (*.teu)", 1)
   If @error Then
	  MsgBox(4096, "", "Keine Datei ausgewählt.")
   Else
	  $file = FileOpen($path, 0)
	  $soup = FileRead($file)
	  GUICtrlSetData($Edit1, $soup)
	  FileClose($file)
   EndIf
EndFunc


Func save()
   If $pathToTeutonScript == "" Then
	  Local $message = "Teuton Speichern"
	  $pathToTeutonScript = FileSaveDialog($message, @ScriptDir & "\", "Teuton (*.teu)", 2, "", $Form1)
   EndIf
   $file = FileOpen($pathToTeutonScript, 2 + 8) ; 2 -> erase prev, 8 -> create dirs
   $soup = GUICtrlRead($Edit1)
   FileWrite($file, $soup)
   FileClose($file)
EndFunc


Func runTeu()
   save()

   Local $pathToPython = @ScriptDir & "\Python\python.exe"
   Local $pathToTeuton = @ScriptDir & "\teuton\teuton.py"

   $keys = $pathToPython & " " & $pathToTeuton & " " & $pathToTeutonScript
   BlockInput(1)
   ShellExecute("cmd.exe")
   Sleep(1000)
   Send($keys)
   Send("{ENTER}")
   BlockInput(0)
EndFunc

Func new()
   ShellExecute(@ScriptDir & "\" & @ScriptName)
EndFunc
