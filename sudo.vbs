dim fso: set fso = CreateObject("Scripting.FileSystemObject")

Set UAC = CreateObject("Shell.Application")

Directory = fso.GetAbsolutePathName(".")
strArgs   = ""
If WScript.Arguments.Count > 0 Then
    For i = 0 To WScript.Arguments.Count - 1
        strArgs = strArgs & " " & WScript.Arguments.Item(i)
    Next
End If
cmdx = "/a /k pushd " + Directory + " & " + strArgs
UAC.ShellExecute "cmd.exe", cmdx, "", "runas", 1
