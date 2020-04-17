page_path_1='../spbroma.github.io/covid'

python -m plot_plotly.py

cp index.html $page_path/index.html

cd $page_path

git add . && git commit -m 'upd' && git push

read -p 'Press any key to continue...' tmpvar