set curtmpdir=mater_tmp_git_789
git clone -n https://github.com/mater789/pyproj.git %curtmpdir%
cd %curtmpdir%
git config core.sparsecheckout true
echo materdp/* >> .git/info/sparse-checkout
git checkout master
rd /q /s .git
