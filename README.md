
# Startup sequence:
````
cd <project_name>/Backend
docker build -t assembler-python-sdk:dev .

cd ..
npx create-next-app@15.5.4 frontend

cd frontend
npx shadcn@3.3.1 init
npx shadcn@3.3.1 add --all

cd ..
python Startup/StartAll.py
````