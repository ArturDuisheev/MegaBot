class UserData {
    [string]$Name
    
    UserData([string]$name) {
        $this.Name = $name
    }

    [string] GetUserInfo() {
        return "Name Of System: $($this.Name)"
    }
}

class UserDataFetcher {
    [UserData[]] $WinInformation
    
    UserDataFetcher() {
        $this.WinInformation = @()
        $WinInstances = Get-CimInstance -ClassName Win32_Desktop
        foreach ($winInstance in $WinInstances) {
            $userData = [UserData]::new($winInstance.Name)
            $this.WinInformation += $userData
        }
    }
    
    [UserData[]] GetAllDataForUser() {
        return $this.WinInformation
    }
}

class ScriptStarter {
    [UserDataFetcher] $userDataFetcher
    
    ScriptStarter() {
        $this.userDataFetcher = [UserDataFetcher]::new()
    }
    
    [void] Start() {
        # $this.SetExecutionPolicy()
        $userData = $this.userDataFetcher.GetAllDataForUser()
        foreach ($data in $userData) {
            Write-Output $data.GetUserInfo()
        }
    }
    
    # [void] SetExecutionPolicy() {
    #     Set-ExecutionPolicy Restricted
    #     Set-ExecutionPolicy AllSigned
    #     Set-ExecutionPolicy RemoteSigned
    # }
}

$starter = [ScriptStarter]::new()
$starter.Start()
