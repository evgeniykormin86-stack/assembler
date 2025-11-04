
# Startup sequence:
````
cd <project_name>/Backend
docker build -t assembler-python-sdk:dev .
cd ..
npx create-next-app@15.5.4 frontend
# Typerscript -yes
# Linter -any
# Tailwind CSS -yes
# `scr/` directory -yes
# App Router -yes
# Turbopack -yes
# import alias -no

cd frontend
npx shadcn@3.3.1 init
npx shadcn@3.3.1 add --all
python Startup/StartAll.py
````