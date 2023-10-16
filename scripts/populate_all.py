import os

scripts_to_run = ['populate_lesson_types.py', 'populate_teachers.py', 'populate_students.py', 'populate_subscription_types.py']

# Run all scripts
def run_scripts():
    for script in scripts_to_run:
        try:
            print(f'Ejecutando el script: {script}')
            os.system(f'python manage.py shell < scripts/{script}')
        except Exception as e:
            print(f'Error al ejecutar el script {script}: {e}')

run_scripts()