Get-CimInstance -ClassName Win32_Desktop

Get-CimInstance -ClassName Win32_Desktop | Select-Object -ExcludeProperty "CIM*"

Get-CimInstance -ClassName Win32_BIOS

Get-CimInstance -ClassName Win32_Processor | Select-Object -ExcludeProperty "CIM*"