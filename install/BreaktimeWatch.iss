#define MyAppVersion "2.0"
#define MyName "Baumgartner Rene Mario"

[Setup]
SignedUninstaller=yes
SignTool=Certum
SetupIconFile=Icon\btwbgr_white_FIz_3.ico
AppName=BreaktimeWatch
AppVersion={#MyAppVersion}
AppVerName=BreaktimeWatch {#MyAppVersion}
AppCopyright={#MyName}
WizardStyle=modern
WizardImageFile=Icon\BtWbgr_white.bmp
WizardImageStretch=no
OutputBaseFilename=BreaktimeWatch{#MyAppVersion}_setup
DefaultDirName={autopf}\BreaktimeWatch
DefaultGroupName=BreaktimeWatch
UninstallDisplayIcon="C:\Users\baumg\Documents\GitHub\Ned84\BreaktimeWatch\install\Icon\btwbgr_white_FIz_3.ico"
UninstallDisplayName=BreaktimeWatch
OutputDir="C:\Users\baumg\Documents\GitHub\Ned84\BreaktimeWatch\install\Output\BreaktimeWatch_V{#MyAppVersion}"
Compression=lzma2
SolidCompression=yes

[Files]
Source: "Breaktimewatch_V{#MyAppVersion}\BreaktimeWatch.py\*"; DestDir: "{app}"; Flags: recursesubdirs
Source: "BreaktimeWatch_V{#MyAppVersion}\BreaktimeWatch.py\BreaktimeWatch.py.exe"; DestDir: "{app}"; Flags: sign


[Icons]
Name: "{group}\BreaktimeWatch"; Filename: "{app}\BreaktimeWatch.py.exe"; IconFilename: "C:\Users\baumg\Documents\GitHub\Ned84\BreaktimeWatch\install\Icon\btwbgr_white_FIz_3.ico"; IconIndex: 0
Name: "{commondesktop}\BreaktimeWatch"; Filename: "{app}\BreaktimeWatch.py.exe"; IconFilename: "C:\Users\baumg\Documents\GitHub\Ned84\BreaktimeWatch\install\Icon\btwbgr_white_FIz_3.ico"; IconIndex: 0
Name: "{commonstartup}\BreaktimeWatch"; Filename: "{app}\BreaktimeWatch.py.exe"; IconFilename: "C:\Users\baumg\Documents\GitHub\Ned84\BreaktimeWatch\install\Icon\btwbgr_white_FIz_3.ico"; IconIndex: 0