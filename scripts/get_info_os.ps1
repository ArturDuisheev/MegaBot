

function GetUserInfo {
    param (
        [String]$username,
        [string]$WindowsInfo
    )
    return @(
        "Username: $($username)",
        "WindowsInfo: $($WindowsInfo)"

        )
}

function Starter {
    # $windows = Get-CimInstance -ClassName Win32_Desktop
    GetUserInfo -username $env:USERNAME
    
}

Starter
