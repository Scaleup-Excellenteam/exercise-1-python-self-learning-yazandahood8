#!/bin/bash

# List of exercise files and their branch names
declare -a files=("5.1.vinnigrete_no.py" "5.1.way_the_thats.py" "5.2.cup_of_join.py" "5.2.piece_of_cake.py" 
                  "5.3.parsle_tongue.py" "5.4.communicating_vessels.py" "6.2.running_2000.py" 
                  "6.3.long_cat_is_long.py" "6.4.remember_remember.py" "6.5.group_by.py" 
                  "7.2.turtle_sent.py")

declare -a branch_names=("exercise-5.1-vinnigrete_no" "exercise-5.1-way_the_thats" "exercise-5.2-cup_of_join" 
                          "exercise-5.2-piece_of_cake" "exercise-5.3-parsle_tongue" "exercise-5.4-communicating_vessels" 
                          "exercise-6.2-running_2000" "exercise-6.3-long_cat_is_long" "exercise-6.4-remember_remember" 
                          "exercise-6.5-group_by" "exercise-7.2-turtle_sent")

# Ensure the main branch is up to date
git checkout main
git pull origin main

# Loop over the files and branch names
for i in "${!files[@]}"; do
    # Create a new branch for each exercise
    git checkout -b "${branch_names[$i]}"

    # Add the file (make sure the file exists in your directory)
    git add "${files[$i]}"

    # Commit the changes
    git commit -m "Completed ${branch_names[$i]}"

    # Push the branch to GitHub
    git push origin "${branch_names[$i]}"

    # Go back to the main branch for the next exercise
    git checkout main
    git pull origin main
done

echo "All branches pushed! Now go to GitHub to create pull requests."
