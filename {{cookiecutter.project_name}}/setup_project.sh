#!/bin/sh
# Author : {{cookiecutter.author}}

echo "Starting to install project dependencies."
poetry install
echo "Project dependencies installed."
echo "Initializing git repositiry for {{cookiecutter.project_name}} locally."
git init
echo "git repository for {{cookiecutter.project_name}} has been created locally please add an origin of your empty repository to push this project up online for version control."
git remote add origin {{cookiecutter.repository_remote}}
git add .
git commit -m "Project Setup"
git branch -M main
git push -u origin main
