creator is a virtual environment from bash loadable from VS code
for -help in creator, /creator/bin]$ open activate, activate.csh, activate.fish
<!--- BASH STEPS
Open terminal and cd
[~/Users/"me"/pythonWS/creator/bin]
[~/Users/"me"/pythonWS/creator/bin] source/bin/activate
SHOULD RESULT IN.........(creator) (base) [/users/"me"/pythonWS/creator]$
(creator) (base) [/users/"me"/pythonWS/creator]$ pip install -m "name of python module"


deactivate () {
    unset -f pydoc >/dev/null 2>&1 || true

    # reset old environment variables
    # ! [ -z ${VAR+_} ] returns true if VAR is declared at all
    if ! [ -z "${_OLD_VIRTUAL_PATH:+_}" ] ; then
        PATH="$_OLD_VIRTUAL_PATH"
        export PATH
        unset _OLD_VIRTUAL_PATH
    fi
    if ! [ -z "${_OLD_VIRTUAL_PYTHONHOME+_}" ] ; then
        PYTHONHOME="$_OLD_VIRTUAL_PYTHONHOME"
        export PYTHONHOME
        unset _OLD_VIRTUAL_PYTHONHOME
    fi
    
