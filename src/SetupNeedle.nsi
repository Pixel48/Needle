; === Setup_Needle.nsi ===
; Includes
  ; MUI2
  !include "MUI2.nsh"
    ; Icons
    !define MUI_ICON "doll.ico"
    !define MUI_UNICON "doll.ico"

; Defines
!define PROG_NAME "Needle"
!define VERSION "Alpha"
!define PUBLISHER "GitHub.com/Pixel48"
!define INST_KEY "SOFTWARE\${PROG_NAME}"
!define UNINST_KEY "SOFTWARE\Microsoft\Windows\CruuentVersion\Uninstall\${PROG_NAME}"
!define DESKTOP_SHORTCUT "$DESKTOP\${PROG_NAME}.lnk"

; Settings
Name "Needle"
OutFile "pyinst\Setup ${PROG_NAME}.exe"
RequestExecutionLevel admin
InstallDir "$PROGRAMFILES64\${PROG_NAME}"
!define UNISNTDIR "$INSTDIR\Uninstall ${PROG_NAME}.exe"

; Installer
  ; Pages
  !insertmacro MUI_PAGE_DIRECTORY
  !insertmacro MUI_PAGE_INSTFILES
  ; Sections
  Section "Installer" installer
    SetOutPath "$INSTDIR"
    File /r "pyinst\dist\${PROG_NAME}\*"
    ; Reg setup
      ; Install info
      WriteRegStr HKLM "${INST_KEY}" "InstallDir" "$ISNTDIR"
      WriteRegStr HKLM "${INST_KEY}" "DisplayName" "${PROG_NAME}"
      WriteRegStr HKLM "${INST_KEY}" "DisplayVersion" "${VERSION}"
      WriteRegStr HKLM "${INST_KEY}" "Publisher" "${PUBLISHER}"
      WriteRegStr HKLM "${INST_KEY}" "UninstallSrting" "${UNINSTDIR}"
      ; Uninstaller
      WriteUninstaller "${UNINSTDIR}"
      WriteRegStr HKLM "${UNINST_KEY}" "InstallDir" "$ISNTDIR"
      WriteRegStr HKLM "${UNINST_KEY}" "DisplayName" "${PROG_NAME}"
      WriteRegStr HKLM "${UNINST_KEY}" "DisplayVersion" "${VERSION}"
      WriteRegStr HKLM "${UNINST_KEY}" "DisplayIcon" "$ISNTDIR\${PROG_NAME}.exe"
      WriteRegStr HKLM "${UNINST_KEY}" "Publisher" "${PUBLISHER}"
      WriteRegStr HKLM "${UNINST_KEY}" "UninstallSrting" "${UNINSTDIR}"
      WriteRegDWORD HKLM "${UNINST_KEY}" "NoModify" 1
      WriteRegDWORD HKLM "${UNINST_KEY}" "NoRepair" 1
  SectionEnd
  Section "Desktop Shortcut" desktop
    CreateShortCut "${DESKTOP_SHORTCUT}" "$INSTDIR\${PROG_NAME}.exe"
  SectionEnd

; Uninstaller
  ; Pages
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES
  ; Sections
  Section "Uninstall" uninstall
    Delete "${DESKTOP_SHORTCUT}"
    Delete "${UNINSTDIR}"
    RMDir /r "$INSTDIR"
    DeleteRegKey HKLM "${ISNT_KEY}"
    DeleteRegKey HKLM "${UNISNT_KEY}"
  SectionEnd
