; SeriEx Installer
!include "MUI2.nsh"

;------------------
; defines
!define PROGRAM_NAME "Needle"
!define UNINST_KEY "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\${PROGRAM_NAME}"
!define INST_KEY "SOFTWARE\${PROGRAM_NAME}"

;------------------
; Atributes
Name "Needle"
OutFile "NeedleSetup.exe"
InstallDir "$PROGRAMFILES32\${PROGRAM_NAME}"
RequestExecutionLevel admin
; Unicode True

;------------------
; Icons
!define MUI_UNICON "doll.ico"
!define MUI_ICON "doll.ico"

;------------------
; Installer
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES

Section "Needle" Needle
  SetOutPath $INSTDIR
  File /r "pyinst\Needle\*"
  CreateDirectory "$INSTDIR\keys"

  WriteRegStr HKLM "${INST_KEY}" "InstallDir" "$INSTDIR"
  WriteRegStr HKLM "${INST_KEY}" "DisplayName" "Needle"
  WriteRegStr HKLM "${INST_KEY}" "DisplayVersion" "preAlpha"
  WriteRegStr HKLM "${INST_KEY}" "DisplayIcon" "$\"$INSTDIR\doll.ico$\""
  WriteRegStr HKLM "${INST_KEY}" "Publisher" "GitHub.com/Pixel48"
  WriteRegStr HKLM "${INST_KEY}" "UninstallString" "$INSTDIR\Uninstall.exe"

  WriteUninstaller "$INSTDIR\Uninstall.exe"

  WriteRegStr HKLM "${UNINST_KEY}" "InstallDir" "$INSTDIR"
  WriteRegStr HKLM "${UNINST_KEY}" "DisplayName" "${PROGRAM_NAME}"
  WriteRegStr HKLM "${UNINST_KEY}" "DisplayVersion" "preAlpha"
  WriteRegStr HKLM "${UNINST_KEY}" "DisplayIcon" "$\"$INSTDIR\doll.ico$\""
  WriteRegStr HKLM "${UNINST_KEY}" "Publisher" "GitHub.com/Pixel48"
  WriteRegStr HKLM "${UNINST_KEY}" "UninstallString" "$\"$INSTDIR\Uninstall.exe$\""
  WriteRegDWORD HKLM "${UNINST_KEY}" "NoModify" 1
  WriteRegDWORD HKLM "${UNINST_KEY}" "NoRepair" 1
SectionEnd

Section "Desktop shortcut"
  CreateShortcut "$DESKTOP\Needle.lnk" "$INSTDIR\Needle.exe"
SectionEnd

;------------------
; Uninstaller
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

Section "Uninstall"
  Delete "$DESKTOP\Needle.lnk"
  RMDir /r "$INSTDIR"
  DeleteRegKey HKLM "${INST_KEY}"
  DeleteRegKey HKLM "${UNINST_KEY}"
SectionEnd
