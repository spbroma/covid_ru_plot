page_path_1='../spbroma.github.io/covid'
page_path_2='../spbroma.github.io/covid_days'

python -m plot_plotly.py
python -m plot_plotly_days.py

cp covid.html $page_path_1/covid.html
cp covid_days.html $page_path_2/covid.html

cd $page_path_1/..

git add . && git commit -m 'upd' && git push

read -p 'Press any key to continue...' tmpvar