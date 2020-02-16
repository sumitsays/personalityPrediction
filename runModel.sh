#!/bin/bash
python3 dlatkInterface.py -d dla_tutorial -t suagarwal_new_input -c user_id -f 'feat$cat_met_a30_2000_cp_w$suagarwal_new_input$user_id$1gra' 'feat$1gram$suagarwal_new_input$user_id$16to16' --predict_regression_to_outcome_table lbp_age --load --picklefile ~/age.2000fbtopics.1to3grams.16to16.ridge1000.magic_sauce.gft500.pickle
