#!/bin/sh

page_path_1='../spbroma.github.io/covid'
page_path_2='../spbroma.github.io/covid/days'
page_path_3='../spbroma.github.io/covid/new'

python plot_plotly.py
python plot_plotly_days.py
python plot_plotly_new.py

# cp covid.html $page_path_1/covid.html
# cp covid_days.html $page_path_2/covid.html
# cp covid_new.html $page_path_3/covid.html

# cd $page_path_1/..

# git add . && git commit -m 'upd' && git push

# read -p 'Press any key to continue...' tmpvar