import subprocess

def execute_ls(args):
    try:
        result = subprocess.run(['ls'] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error al ejecutar "ls": {e}'

def execute_cat(args):
    try:
        result = subprocess.run(['cat'] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error al ejecutar "cat": {e}'

allowed_commands = {'ls': execute_ls, 'cat': execute_cat}

while True:
    try:
        user_input = input('JailShell >> ')
        if not user_input:
            continue

        command, *args = user_input.split()

        if command not in allowed_commands:
            print('Comando no permitido.')
            continue

        output = allowed_commands[command](args)

        print(output)

    except KeyboardInterrupt:
        print('\nClose.')
        break
    except Exception as e:
        print(f'Error: {e}')