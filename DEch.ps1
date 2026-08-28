function DEch {
    param (
        [string]$DiffEq,
        [string]$ProposedSol,
        [switch]$h
    )
    
    if ($h) {
        Write-Host ""
        Write-Host "DEch - Differential Equation Checker" -ForegroundColor Cyan
        Write-Host "------------------------------------" -ForegroundColor Cyan
        Write-Host "Usage:   DEch `"differential_equation`" `"proposed_solution`""
        Write-Host "Example: DEch `"y' = 2y`" `"y = E**(2t)`""
        Write-Host "Format:  Use 't' as the independent variable and 'y' as the dependent function."
        Write-Host "         Derivatives can be typed as y', y'', dy/dt, etc."
        Write-Host ""
        return
    }
    
    if ([string]::IsNullOrWhiteSpace($DiffEq) -or [string]::IsNullOrWhiteSpace($ProposedSol)) {
        Write-Host "Error: Missing arguments. Type 'DEch -h' for help." -ForegroundColor Red
        return
    }
    
    $scriptPath = $PSScriptRoot
    
    python "$scriptPath\parser.py" $DiffEq $ProposedSol | Out-Null
    python "$scriptPath\checker.py"
}