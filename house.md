






si estas en linux o wsl debes instalar

    sudo apt install -y python3-venv

Poner cada proyecto en su propio ambiente, entrar en cada carpeta.

    python3 -m venv env

    o 

    python -m venv env


Activar el ambiente

    source env/bin/activate
    o:
    source env/Scripts/activate

verifica lo que tengas instalado .

pip freeze 
pasa lo instalado a requeriments.txt

pip freeze >  requeriments.txt
pip freeze >  requeriments_python3_12.txt




como exportar un env para no saturar disco! :

ejemplo :

primero abrir la terminal , bash , y lo buscas (la carpeta) y la activas :

$ pwd

L
/d/ORA_proyectos/Python_balances_v02

H
/d/Users/hpgus/Documents/Proyectos_VS/platzi/RLogísticaPython-scikit-learn

pero esta en : 
L: C:\Users\gchiappe\Desktop\Ora\BALANCES_GUS_PY

h: C:\Users\elloc\Downloads\clase_reg_li_plazti


L:
entonces en el bash pones
$ cd ~/Desktop/Ora/BALANCES_GUS_PY
$ pwd
/c/Users/gchiappe

$ cd Desktop/Ora/BALANCES_GUS_PY
gchiappe@E102202 MINGW64 ~/Desktop/Ora/BALANCES_GUS_PY (main)

H:

entonces en el bash pones
$ cd ~/Downloads/clase_reg_li_plazti
$ pwd
/c/Users/elloc/Downloads/clase_reg_li_plazti



L=>
hacer : 
1:
cd ~/Desktop/Ora/BALANCES_GUS_PY
2:
source env/Scripts/activate
3:
cd /d/ORA_proyectos/Python_balances_v02

(env) 
gchiappe@E102202 MINGW64 ~/Desktop/Ora/BALANCES_GUS_PY (main)

una vez activado instalas el Jupyter
pip install jupyter

y despues generas el env

python -m ipykernel install --user --name=env --display-name "Python (env)"

una vez terminado , cerras el vscode y lo volves abrir , abris una notebook y 
En la parte superior, donde dice "Select Kernel", elige "Python (env)".

Listo


H =>

hacer : 
1:
cd ~/Downloads/clase_reg_li_plazti
2:
source env/Scripts/activate
3:
cd /d/Users/hpgus/Documents/Proyectos_VS/platzi/RLogísticaPython-scikit-learn

(env) 
elloc@DESKTOP-9IHTN86 MINGW64 ~/Downloads/clase_reg_li_plazti (main)
$ cd /d/Users/hpgus/Documents/Proyectos_VS/platzi/RLogísticaPython-scikit-learn

una vez activado instalas el Jupyter
pip install jupyter

y despues generas el env

python -m ipykernel install --user --name=env --display-name "Python3_12 (env)clase_reg_li_plazti "

una vez terminado , cerras el vscode y lo volves abrir , abris una notebook y 
En la parte superior, donde dice "Select Kernel", elige "Python (env)".