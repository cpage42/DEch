# DEch — Differential Equation Checker

A command-line tool that checks whether a proposed solution satisfies a given differential equation. Type in an equation and a candidate solution, and DEch tells you `yes` or `no`.

Under the hood, it uses [SymPy](https://www.sympy.org/) to parse both expressions, substitute the proposed solution into the differential equation, take derivatives symbolically, and simplify to check if both sides match.

## Requirements

- Windows with PowerShell
- [Python 3](https://www.python.org/downloads/) installed and available on your `PATH`
- The `sympy` package:
  ```powershell
  pip install sympy
  ```

## Installation

1. Clone the repo:
   ```powershell
   git clone https://github.com/cpage42/DEch.git
   cd DEch
   ```

2. Run the installer:
   ```powershell
   .\install.ps1
   ```
   This adds a single line to your PowerShell `$PROFILE` that loads the `DEch` function automatically in every new terminal. It's safe to run more than once — it won't duplicate the line if it's already there.

3. Restart your terminal, or run:
   ```powershell
   . $PROFILE
   ```
   to load `DEch` into your current session right away.

From here on, `DEch` is available in every new PowerShell window — no extra steps.

### If scripts are blocked

Fresh Windows installs sometimes block running `.ps1` files by default. If `install.ps1` fails with a message about running scripts being disabled, run this once first:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

## Usage

```powershell
DEch "differential_equation" "proposed_solution"
```

**Example:**
```powershell
DEch "y'' + 9y = 0" "y = cos(3t)"
```
Output:
```
yes
```

### Format

- Use `t` as the independent variable and `y` as the dependent function.
- Derivatives can be written as `y'`, `y''`, `dy/dt`, or `d^2y/dt^2`.
- Implicit multiplication is supported — `3t` is read as `3*t`.

### Help

```powershell
DEch -h
```
Prints usage instructions without running anything.

## How it works

1. `DEch.ps1` — the PowerShell function you call. Validates your input, then runs the two Python scripts below.
2. `parser.py` — parses your raw equation strings (converting notation like `y''` or `dy/dt`) into SymPy syntax, and writes the results to `def.txt` and `prop.txt`.
3. `checker.py` — reads `def.txt`/`prop.txt`, substitutes the proposed solution into the differential equation, evaluates the derivatives, and simplifies both sides to check for equality.

`def.txt` and `prop.txt` are regenerated on every run and are not tracked in git.

## Repo contents

| File | Purpose |
|---|---|
| `DEch.ps1` | Defines the `DEch` PowerShell function |
| `install.ps1` | One-time setup — registers `DEch` in your `$PROFILE` |
| `parser.py` | Parses input equations into SymPy syntax |
| `checker.py` | Verifies the proposed solution against the differential equation |
