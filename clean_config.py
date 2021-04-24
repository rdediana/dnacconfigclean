# edit

in_file_name = 'sample_config.log'
out_file_name = 'sample_config_clean.log'
excludes_file_name = 'excludes.txt'

begin_excludes = []
contain_excludes = []


def clean_config():
    write_lines = []
    with open(in_file_name, 'r') as f:
        lines = f.readlines()
    with open(out_file_name, 'w') as f:
        for line in lines:
            line_string = line.strip('\n')
            if not str.startswith(line_string, '!') and not str.startswith(line_string, ' '):
                if exclude(line_string) is not True:
                    write_lines.append('no ' + line_string + '\n')
                    print('no ' + line_string)
        f.writelines(write_lines)


def load_excludes():

    section = ''

    with open(excludes_file_name, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip('\n')
        line = line.strip('\t')
        if 'begins:' in line:
            section = 'begins'
        elif 'contains:' in line:
            section = 'contains'

        if not str.startswith(line, '!'):
            if section == 'begins' and line != 'begins:' and line != '':
                begin_excludes.append(line)
            elif section == 'contains' and line != 'contains:' and line != '':
                contain_excludes.append(line)


def exclude(line):
    exclude_line = False
    for item in contain_excludes:
        if item in line:
            exclude_line = True
            break

    for item in begin_excludes:
        if str.startswith(line, item):
            exclude_line = True
            break

    return exclude_line

# 1. Modify in_file_name and out_file_name variables
# 2. Modify "custom excludes" in "excludes.txt" file
# 3. Run

if __name__ == '__main__':
    load_excludes()
    clean_config()

