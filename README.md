
# Startup sequence:
````
cd <project_name>/Backend
docker build -t assembler-python-sdk:dev .

cd ..
npx create-next-app@15.5.4 frontend
# TypeScript - yes
# Linter - any
# Tailwind CSS - yes
# `src/` directory - yes
# App Router - yes
# Turbopack - yes
# import alias - no

cd frontend
npx shadcn@3.3.1 init
npx shadcn@3.3.1 add --all

npm i @prisma/client
npx prisma init --db --output ../app/generated/prisma

# Generate Prisma Client
npx prisma generate

python Startup/StartAll.py
````